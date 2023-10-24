#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/18 13:12
# @Author  : yinhai
# @File    : plug_manage.py
# @Project : AUTO_UI
import json
import sys
import time
from threading import Thread
from PySide6 import QtGui, QtWidgets, QtCore
from pathlib import Path
from manage import HaiProMax
from module import AutoTree, PlugFactory
from cmw import model_image_canvas
import importlib
import shutil


class PlugManage(AutoTree.Tree):
    """
    插件管理
    """

    def __init__(self, main_ui: HaiProMax):
        super().__init__(main_ui)
        self.module = None
        self.entirety = {}
        self.itemDoubleClicked.connect(self.openModule)
        self.plug_path = Path().cwd() / 'plug'
        for plug_file in self.plug_path.joinpath('temp').glob('*.pyd'):
            plug_file.unlink()
        self.plug_path.mkdir(exist_ok=True, parents=True)

    def initModuleButton(self):
        """
        初始化插件按钮
        :return:
        """
        for item in self.module.getShowButton():
            self.main_ui.addMenuButton(**item)

    @QtCore.Slot(QtWidgets.QTreeWidgetItem, int)
    def openModule(self, item, column_no=0):
        """
        打开插件
        :param item:
        :param column_no:
        :return:
        """
        if not self.main_ui.tools_temp.OPEN_DIR_PATH:
            # 提示没有打开文件
            return
        if self.main_ui.project_settings is None: return
        if item.childCount(): return
        self.startModule(item.text(1))

    def startModule(self, module_name):
        """
        启动插件
        :param module_name:
        :return:
        """
        # TODO:需要保证启动模块的通用性， 有点是打开文件，有的是打开文件夹
        module = importlib.import_module('plug.tools.{}'.format(module_name))
        if self.module:
            self.main_ui.canvas_layout.removeWidget(self.module)
        self.module = module.Module(self.main_ui.project_settings.value('PROJECT'))

        if self.module.expiration_date < time.time():
            self.module = None
            self.main_ui.widget_toast.showError(self.main_ui.getTr('授权失效,请重写授权'))
            return

        if not self.module.sidebar:
            self.main_ui.external_tool_display.hide()
        else:
            self.main_ui.external_tool_display.show()
            widgets = self.initEntirety(self.module.plugOption.image_options)
            self.main_ui.addToolListButton(widgets)
        self.main_ui.canvas_layout.addWidget(self.module)
        self.initModuleButton()
        last_filename = self.main_ui.project_settings.value('LASTFILENAME')
        if last_filename: self.openFile(Path(last_filename))
        self.main_ui.widget_toast.showSucceed(self.main_ui.getTr('打开成功'))

    def initEntirety(self, options: list):
        """
        初始整体选项
        :param options:
        :return:
        """
        language = self.main_ui.tools_tr.language
        widget_list = []
        for option in options:
            item_option = option[f'{language}_options']
            if option['type'] == 'select':
                widget = QtWidgets.QComboBox()
                widget.addItems(item_option)
                widget.currentIndexChanged.connect(self.entiretyValue)
            else:
                widget = QtWidgets.QPushButton(item_option[0])
                widget.setCheckable(True)
                widget.toggled.connect(self.entiretyValue)
            self.entirety[option['name']] = {'widget': widget, 'option': item_option}
            widget_list.append(widget)
        return widget_list

    def entiretyValue(self, *args, **kwargs):
        """
        整体选项值改变
        :param args:
        :param kwargs:
        :return:
        """
        image_entirety = {}
        for name, widget_data in self.entirety.items():
            widget: QtWidgets.QComboBox | QtWidgets.QPushButton = widget_data['widget']
            option = widget_data['option']
            if isinstance(widget, QtWidgets.QComboBox):
                image_entirety[name] = widget.currentText()
            else:
                widget.setText(option[int(widget.isChecked())])
                image_entirety[name] = widget.text()
        if not self.module.draw_store: return
        self.module.draw_store.setImageEntirety(image_entirety)

    def treeMenus(self, pos: QtCore.QPoint) -> None:
        """
        文件菜单的右键菜单
        :param pos:
        :return:
        """
        item = self.currentItem()
        if not item: return
        click_path = Path(item.text(1))
        if click_path.is_dir(): return
        popMenu = QtWidgets.QMenu()
        itemMenu = popMenu.addAction(self.main_ui.getTr('打开'))
        itemMenu.triggered.connect(lambda: self.openModule(item))
        itemMenu = popMenu.addAction(self.main_ui.getTr('删除'))
        itemMenu.triggered.connect(lambda: self.delModule(item))
        popMenu.exec(QtGui.QCursor.pos())
        popMenu.show()

    def openFile(self, path: Path):
        """
        打开文件
        :param path:
        :return:
        """
        if self.module is None:
            self.main_ui.widget_toast.showError('工具尚未打开')
            return
        self.module.selectFile(path)
        if not self.module.draw_store: return
        if self.main_ui.project_settings:
            self.main_ui.project_settings.setValue('LASTFILENAME', str(path))
            self.main_ui.project_settings.sync()

        for name, value in self.module.draw_store.image_entirety.items():
            widget: QtWidgets.QComboBox | QtWidgets.QPushButton = self.entirety[name]['widget']
            option: list = self.entirety[name]['option']
            if isinstance(widget, QtWidgets.QComboBox):
                widget.setCurrentIndex(option.index(value))
            else:
                widget.setChecked(bool(option.index(value)))

    def initTreeItem(self):
        """
        初始化树形菜单项
        :return:
        """
        language = self.main_ui.tools_tr.language
        self.clear()

        def threadFunc():
            manage_file = Path().cwd() / 'plug' / 'manage.json'
            if not manage_file.exists():
                manage_file.parent.mkdir(exist_ok=True, parents=True)
                with manage_file.open('w', encoding='utf-8') as f:
                    f.write(json.dumps({}))
                return

            with manage_file.open('r', encoding='utf-8') as f:
                manage_data = json.loads(f.read())
                type_dict = {}
                for plug_data in manage_data:
                    type_key = f'tool_{language}_type'
                    name_key = f'tool_{language}_info'
                    if type_key not in type_dict:
                        plug_type = QtWidgets.QTreeWidgetItem(self)
                        plug_type.setText(0, plug_data[type_key])
                        plug_type.setIcon(0, QtGui.QIcon('icons:分类管理_category-management.svg'))
                        type_dict[type_key] = plug_type
                    plug = QtWidgets.QTreeWidgetItem(type_dict[type_key])
                    name = plug_data[name_key]
                    plug.setText(0, name)
                    plug.setText(1, plug_data['path'])
                    plug.setIcon(0, QtGui.QIcon('icons:模块箭头_blocks-and-arrows.svg'))
                    plug.setToolTip(0, name)

        loading_thread = Thread(target=threadFunc, daemon=True)
        loading_thread.start()
        self.main_ui.showWindowToast(self.main_ui.getTr('插件操作'), self.main_ui.getTr('读取插件完成'))

    def addModule(self):
        """
        添加模块
        :return:
        """
        path = QtWidgets.QFileDialog.getOpenFileName(
            self,
            self.main_ui.getTr('选择文件'),
            self.main_ui.path_temp.getCache(),
            filter='插件文件(*.cp311-win_amd64.pyd)'
        )
        if not path:
            self.main_ui.widget_toast.showInfo(self.main_ui.getTr('取消'))
            return
        path = Path(path[0])
        temp_plug_path = self.plug_path / 'temp' / path.name
        temp_plug_path.parent.mkdir(exist_ok=True, parents=True)
        shutil.copyfile(path, temp_plug_path)
        sys.path.insert(0, str(Path.cwd()))
        module = importlib.import_module('plug.temp.{}'.format(path.name.split('.')[0]))
        if module.Module.expiration_date < time.time():
            self.main_ui.widget_toast.showError(self.main_ui.getTr('授权失效,请重写授权'))
            return
        plug_options: model_image_canvas.Canvas = module.Module

        tool_plug_path = self.plug_path / 'tools' / path.name
        tool_plug_path.parent.mkdir(exist_ok=True, parents=True)

        with open(self.plug_path / 'manage.json', 'r+', encoding='utf-8') as f:
            manage_data = json.loads(f.read())
            plug_data = {
                'tool_中文_type': plug_options.tool_cn_type,
                'tool_English_type': plug_options.tool_en_type,
                'tool_中文_info': plug_options.tool_cn_info,
                'tool_English_info': plug_options.tool_en_info,
                'path': 'plug.tools.{}'.format(path.name.split('.')[0]),
            }
            if manage_data:
                if plug_data in manage_data:
                    del manage_data[manage_data.index(plug_data)]
                manage_data.append(plug_data)
            else:
                manage_data = [plug_data, ]
            f.seek(0)
            f.truncate()
            f.write(json.dumps(manage_data, ensure_ascii=False, indent=4))
        shutil.copyfile(path, tool_plug_path)
        self.main_ui.widget_toast.showSucceed(self.main_ui.getTr('读取安装完成'))
        del module
        self.initTreeItem()

    def delModule(self, item):
        """
        删除模块
        :param item:
        :return:
        """
        plug_file_path = self.plug_path.parent / f'{item.text(1).replace(".", "/")}.cp311-win_amd64.pyd'
        with open(self.plug_path / 'manage.json', 'r+', encoding='utf-8') as f:
            manage_data = json.loads(f.read())
            del manage_data[[i['path'] for i in manage_data].index(item.text(1))]
            f.seek(0)
            f.truncate()
            f.write(json.dumps(manage_data, ensure_ascii=False, indent=4))
            self.main_ui.widget_toast.showSucceed(self.main_ui.getTr('删除成功'))
            plug_file_path.unlink()
        self.initTreeItem()
