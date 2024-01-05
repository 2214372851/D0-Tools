#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/19 16:19
# @Author  : yinhai
# @File    : data_proxy.py
# @Project : V0.0.1-alpha
from pathlib import Path
from threading import RLock

from PySide6 import QtWidgets, QtCore, QtGui

from cmw.model_data import Store
from cmw.model_selected import Selected
from utils.translate import Translate
from utils.yun_type import YunType


class DataStateManage(metaclass=YunType):
    """
    数据状态管理器
    """
    single_lock = RLock()
    selected = None
    store = None
    data_list_widget = None
    data_count_widget = None
    cache_item: None | QtWidgets.QListWidgetItem = None
    file_path_func = None
    translate = Translate()

    @QtCore.Slot()
    def storeAlter(self):
        """
        store数据改变时，刷新数据列表
        :return:
        """
        if self.data_list_widget is None: return
        self.data_list_widget.clear()
        self.data_list_widget.itemClicked.connect(self.listItemClick)
        data = self.store.readData()
        for index, item in enumerate(data):
            listItem = QtWidgets.QListWidgetItem()
            if item['mode'] == 'rect':
                listItem.setIcon(QtGui.QIcon('icons:选中焦点_selected-focus.svg'))
            elif item['mode'] == 'poly':
                listItem.setIcon(QtGui.QIcon('icons:八边形_octagon.svg'))
            elif item['mode'] == 'line':
                listItem.setIcon(QtGui.QIcon('icons:两点连接_connection-point-two.svg'))
            elif item['mode'] == 'point':
                listItem.setIcon(QtGui.QIcon('icons:点_dot.svg'))
            listItem.setData(QtCore.Qt.ItemDataRole.UserRole, index)
            info = '{}-->{}'.format(
                str(index + 1).zfill(3),
                '-|-'.join([f'{k}:{v}' for k, v in item['options'].items()])
            )
            listItem.setText(info)
            listItem.setToolTip(info)
            self.data_list_widget.addItem(listItem)
            self.data_count_widget.setText(str(index + 1).zfill(5))
        if not data: self.data_count_widget.setText('0'.zfill(5))
        self.cache_item = None
        pass

    def listItemClick(self, item: QtWidgets.QListWidgetItem):
        """
        列表项点击时，刷新选中状态
        :param item:
        :return:
        """
        if self.selected is None: return
        index = item.data(QtCore.Qt.ItemDataRole.UserRole)
        self.selected.setSelect(int(index))

    def listItemMenus(self, pos: QtCore.QPoint) -> None:
        """
        文件菜单的右键菜单
        :param pos:
        :return:
        """
        item = self.data_list_widget.currentItem()
        if self.store is None: return
        index = int(item.data(QtCore.Qt.ItemDataRole.UserRole))
        if item:
            self.selected.clearSelect()
            popMenu = QtWidgets.QMenu()
            popMenu.setStyleSheet('''
                            QMenu {
                                background-color: rgb(43, 45, 48); 
                                color: rgb(223, 225, 229); 
                                background: rgb(43, 45, 48);
                                border: 1px solid rgb(79, 80, 83);
                                border-radius: 5px;
                                padding: 2px;
                            }
                            QMenu::item {
                              padding: 5px;
                            }
                            QMenu::item:selected {
                                  background: rgb(46, 67, 110);
                                  border-radius: 2px;
                            }
                            ''')
            itemMenu = popMenu.addAction(self.translate.get_tr('删除'))
            itemMenu.triggered.connect(lambda: self.store.delData(index))
            itemMenu = popMenu.addAction(self.translate.get_tr('上移图层'))
            itemMenu.triggered.connect(lambda: self.store.movingLayer('+', index))
            itemMenu = popMenu.addAction(self.translate.get_tr('下移图层'))
            itemMenu.triggered.connect(lambda: self.store.movingLayer('-', index))

            popMenu.exec(QtGui.QCursor.pos())
            popMenu.show()

    @QtCore.Slot()
    def selectedAlter(self):
        """
        选择状态改变时，刷新数据列表
        :return:
        """
        if self.data_list_widget is None: return
        if self.cache_item is not None:
            self.cache_item.setBackground(QtGui.QColor(0, 0, 0, 0))
        item = self.data_list_widget.item(self.selected.polyIndex)
        item.setBackground(QtGui.QColor(240, 69, 74))
        self.cache_item = item
        pass

    def setListWidget(self, list_widget: QtWidgets.QListWidget):
        """
        设置数据列表组件
        :param list_widget:
        :return:
        """
        list_widget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        list_widget.customContextMenuRequested.connect(self.listItemMenus)
        self.data_list_widget = list_widget
        return self

    def setCountWidget(self, count_widget: QtWidgets.QLabel):
        """
        设置数据列表组件
        :param count_widget:
        :return:
        """
        self.data_count_widget = count_widget
        return self

    def setFilePath(self, set_func):
        self.file_path_func = set_func

    def setSelected(self, selected: Selected):
        """
        设置选择状态器
        :param selected:
        :return:
        """
        self.selected = selected
        self.selected.setSignal(self.selectedAlter)
        return self

    def setStore(self, store: Store):
        """
        设置数据存储器
        :param store:
        :return:
        """
        self.store = store
        self.store.setSignal(self.storeAlter)
        self.file_path_func(Path(store.filename))
        return self
