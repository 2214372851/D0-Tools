import logging
import os
import shutil
import subprocess
import sys
from datetime import datetime
from functools import partial
from pathlib import Path
from threading import Thread

import filetype
from PySide6 import QtGui, QtWidgets, QtCore

from style import HaiWindowsUi
from style.setting_ui import Ui_Setting
from utils import tools, tools_temp, translate, path_temp, window_event, plug_manage
from utils.data_proxy import DataStateManage


# pyside6-lupdate .\manage.py -ts eng-chs.ts 翻译文件
# self.showFullScreen() 全屏
class HaiProMax(HaiWindowsUi.Ui_window):
    # 进度条状态
    progress_bar_store = QtCore.Signal(bool)

    def __init__(self):
        """
        界面初始化配置
        """
        super(HaiProMax, self).__init__()
        self.tools_tr = translate.Translate()
        self.setting_window = None
        self.widget_toast = tools.WidgetMessage().setFocusWidget(self)
        self.tools_temp = tools_temp.ToolsTemp()
        self.path_temp = path_temp.CachePath()
        self.initLog()
        self.setupUi(self)
        self.initIcons()
        self.model = QtWidgets.QFileSystemModel()
        self.proxy_model = tools.YunProxyModel()
        self.global_progress_bar = QtWidgets.QProgressBar()
        self.progress_bar_store.connect(self.progressBarLoad)
        tools.Loading().setProgressSignal(self.progress_bar_store)
        self.initUi()
        self.left_menu_map = {
            0: self.project_button
        }
        self.tools_menu_map = []
        self.initTip()
        self.temp_open_path = set()
        self.settings = QtCore.QSettings("config.ini", QtCore.QSettings.IniFormat)
        self.project_settings: QtCore.QSettings | None = None
        self.setWindowStyle()
        self.loading_thread: Thread | None = None
        self.old_hook = sys.excepthook
        sys.excepthook = self.catchExceptions
        self.plugManage = self.initPlug()
        self.initMenus()
        self.initSetting()
        self.dataManage = (
            DataStateManage()
            .setListWidget(self.canvas_tool_list)
            .setCountWidget(self.count_value)
            .setFilePath(self.setFilePath)
        )

    def setTranslate(self, language: str = '中文'):
        """
        切换语言
        :param language: 语言
        :return:
        """
        self.tools_tr.setLanguage(language)
        self.initTip()
        self.initMenus()
        self.widget_toast.showSucceed(self.getTr('语言切换成功'), call_back=lambda: print("回调函数"))
        self.settings.setValue("language", language)
        self.addToolListButton(self.plugManage.initEntirety())

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        按键按下事件
        :param event:
        :return:
        """
        if event.key() == QtCore.Qt.Key.Key_F11:
            if self.isFullScreen():
                self.top_menus.show()
                self.showNormal()
            else:
                self.top_menus.hide()
                self.showFullScreen()
        if event.key() == QtCore.Qt.Key.Key_AsciiTilde:
            if not self.external_tool_display.isHidden():
                self.showCanvasListWindow()

    @staticmethod
    def initLog():
        """
        初始化日志系统
        :return:
        """
        Path('./log').mkdir(exist_ok=True, parents=True)
        logging.basicConfig(
            filename=f"./log/{datetime.now().date()}.log",
            filemode="a",
            encoding='utf-8',
            format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
            datefmt="%d-%M-%Y %H:%M:%S", level=logging.INFO
        )

    def getTr(self, text: str) -> str:
        """
        获取多语言文本
        :param text: 文本
        :return:
        """
        return self.tools_tr.get_tr(text)

    @QtCore.Slot()
    def closeProject(self):
        """
        关闭当前项目
        :return:
        """
        if not self.tools_temp.OPEN_DIR_PATH:
            self.widget_toast.showInfo(self.getTr('当前未打开文件夹'))
            return
        self.tools_temp = tools_temp.ToolsTemp()
        self.dir_tree.clear()
        self.file_path.setText('')
        self.recently_lately_button.setText('')
        self.clearModuleElement()
        self.widget_toast.showSucceed(message=self.getTr('项目已关闭'))

    def clearModuleElement(self):
        """
        清除上一个模块遗留的控件
        :return:
        """
        item_list = list(range(self.tools_menus_layout.count()))
        item_list.reverse()
        for index in item_list:
            item = self.tools_menus_layout.itemAt(index)
            item.widget().deleteLater()
            self.tools_menus_layout.removeItem(item)
        if self.canvas_layout.count():
            canvas_item = self.canvas_layout.takeAt(0)
            if canvas_item.widget():
                canvas_item.widget().deleteLater()
        self.canvas_tool_list.clear()
        self.external_tool_display.hide()
        self.tools_menus_background.hide()
        self.canvas_list.hide()
        self.setMenusIcon(self.external_tool_display, 'icons:预览-关闭_preview-close-one.svg')

    def catchExceptions(self, ty, value, traceback):
        """
        捕获异常，并弹窗显示
        :param ty: 异常的类型
        :param value: 异常的对象
        :param traceback: 异常的traceback
        """
        self.widget_toast.showError(str(value))
        self.popUpWindowsMessage(1, self.getTr('错误'), str(value))
        logging.error('{}:未处理异常错误:{}'.format(
            traceback.tb_frame,
            value
        ))
        self.old_hook(ty, value, traceback)

    def initSetting(self):
        """
        初始化配置文件
        :return:
        """
        self.setTranslate(language=str(self.settings.value("language")))

    def saveSetting(self):
        """
        保存配置选项
        :return:
        """
        self.settings.sync()

    def setWindowStyle(self):
        """
        设置窗口样式表
        :return:
        """
        style_file = Path(str(self.settings.value('themes')))
        if style_file.exists():
            with style_file.open(mode='r', encoding='utf-8') as f:
                self.setStyleSheet(f.read())
            self.update()
        else:
            self.widget_toast.showInfo(self.getTr('未找到样式文件'))
            self.popUpWindowsMessage(message_type=1, title=self.getTr('错误'), message=self.getTr('未找到样式文件'))

    def initUi(self):
        """
        初始化窗口组件事件
        :return:
        """
        self.proxy_model.setSourceModel(self.model)
        self.dir_tree.setModel(self.proxy_model)
        for i in range(1, self.model.columnCount()):
            self.dir_tree.hideColumn(i)
        self.setWindowIcon(QtGui.QIcon('icons:logo.ico'))
        self.setWindowTitle('D0 Tools')
        self.initRecentlyMenus()
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.close_button.clicked.connect(self.closeWindow)
        self.max_button.clicked.connect(self.maximizeWindow)
        self.min_button.clicked.connect(self.showMinimized)
        self.external_tool_display.clicked.connect(self.showCanvasListWindow)
        self.project_button.clicked.connect(lambda: self.showLeftMenu(menu_page_index=0))
        self.menus_button.clicked.connect(self.menus_button.showMenu)
        self.canvas_list.hide()
        self.tree_menus.hide()
        self.tools_menus_background.hide()
        self.dir_tree.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.dir_tree.customContextMenuRequested.connect(self.treeMenus)
        self.dir_tree.doubleClicked.connect(self.fileTreeClickItem)
        # self.dir_tree.clear()
        self.file_path.setText('')
        self.setting_button.clicked.connect(self.openSetting)
        self.plob_search_button.clicked.connect(self.openSearch)
        self.update_button.clicked.connect(self.updateUi)
        self.update_button.setShortcut(QtCore.Qt.Key.Key_F5)
        self.cooperate_with_button.clicked.connect(self.showMsg)
        self.external_tool_display.hide()
        self.notice_button.clicked.connect(lambda: self.widget_toast.showSucceed('路漫漫其修远兮，吾将上下而求索'))
        self.bottom_right_menus_layout.addWidget(self.global_progress_bar)
        self.global_progress_bar.setMinimum(0)
        self.global_progress_bar.setMaximum(0)
        self.global_progress_bar.setRange(0, 0)
        self.global_progress_bar.hide()

    @QtCore.Slot(bool)
    def progressBarLoad(self, store):
        """
        切换进度条状态
        :param store: 状态 False 结束 True 继续
        :return:
        """
        if store:
            self.global_progress_bar.show()
            self.file_count.hide()
            self.setEnabled(False)
        else:
            self.global_progress_bar.hide()
            self.file_count.show()
            self.setEnabled(True)

    def selectCanvas(self, file: Path):
        """
        test
        :param file:
        :return:
        """
        text = QtWidgets.QTextEdit()
        with file.open('r', encoding='utf-8') as f:
            text.setText(f.read())
        self.canvas_layout.addWidget(text)

    def addToolListButton(self, widgets: None | list[QtWidgets.QPushButton | QtWidgets.QComboBox]):
        """
        添加画布菜单栏按钮
        :param widgets:
        :return:
        """
        if not widgets: return
        item_list = list(range(2, self.canvas_tool_list_layout.count()))
        item_list.reverse()
        for index in item_list:
            item = self.canvas_tool_list_layout.itemAt(index)
            item.widget().deleteLater()
            self.canvas_tool_list_layout.removeItem(item)
        self.tools_menu_map.clear()
        for widget in widgets:
            if isinstance(widget, QtWidgets.QPushButton):
                widget.setObjectName('canvas_tool_list_button')
            else:
                widget.setObjectName('canvas_tool_list_select')
            self.canvas_tool_list_layout.addWidget(widget)

    @QtCore.Slot(int, int)
    def fileTreeClickItem(self, index):
        """
        文件树点击事件
        :param index:
        :return:
        """
        path = Path(self.model.filePath(self.proxy_model.mapToSource(index)))
        self.setFilePath(path)
        if path.is_dir(): return
        self.plugManage.openFile(path)

    @QtCore.Slot()
    def showMsg(self):
        """
        协同功能暂时回调
        :return:
        """
        # TODO: 协调功能待完成
        self.widget_toast.showSucceed(
            '路漫漫其修远兮\n吾将上下而求索\n协同功能开发中{}'.format(len(self.widget_toast.STACK)))

    @QtCore.Slot()
    def updateUi(self):
        """
        刷新当前UI
        :return:
        """
        if not self.tools_temp.OPEN_DIR_PATH:
            self.widget_toast.showInfo(self.getTr('当前未打开文件夹'))
            return
        self.openDir(self.tools_temp.OPEN_DIR_PATH)
        self.update()

    @QtCore.Slot()
    def openSearch(self):
        """
        打开搜索
        :return:
        """
        value = tools.WidgetDialog().getText(title=self.getTr('输入名称'), pos=self.getDialogPos())
        if not value: return
        if not self.tools_temp.OPEN_DIR_PATH:
            self.widget_toast.showInfo(self.getTr('当前未打开文件夹'))
            return
        self.openDir(self.tools_temp.OPEN_DIR_PATH, value)

    def getDialogPos(self) -> tuple:
        """
        主窗口中心,用于弹窗位置
        :return: (x中心点, y中心点)
        """
        return self.pos().x() + (self.width() / 2), self.pos().y() + (self.height() / 2)

    def showFullScreen(self) -> None:
        """
        窗口全屏
        :return: None
        """
        super(HaiProMax, self).showFullScreen()
        self.setMenusIcon(self.max_button, 'icons:复制_copy.svg')
        self.background.setStyleSheet('#background{border-radius: 0px;}')
        self.max_button.hide()
        self.min_button.hide()

    def showNormal(self) -> None:
        """
        窗口正常
        :return:
        """
        super(HaiProMax, self).showNormal()
        self.setMenusIcon(self.max_button, 'icons:方形_square.svg')
        self.background.setStyleSheet('#background{border-radius: 8px;}')
        self.max_button.show()
        self.min_button.show()

    def showMaximized(self) -> None:
        """
        窗口最大化
        :return:
        """
        super(HaiProMax, self).showMaximized()
        self.setMenusIcon(self.max_button, 'icons:复制_copy.svg')
        self.background.setStyleSheet('#background{border-radius: 0px;}')

    @QtCore.Slot()
    def openSetting(self):
        """
        显示设置页面
        :return:
        """
        self.setting_window = Ui_Setting()
        self.setting_window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.setting_window.setupUi(self.setting_window, self.setTranslate, self.settings.value("language"))
        self.setting_window.show()

    def initTip(self):
        """
        初始化提示
        :return:
        """
        self.close_button.setToolTip(self.getTr('关闭'))
        self.max_button.setToolTip(self.getTr('最大化'))
        self.min_button.setToolTip(self.getTr('最小化'))
        self.setting_button.setToolTip(self.getTr('设置'))
        self.plob_search_button.setToolTip(self.getTr('搜索'))
        self.cooperate_with_button.setToolTip(self.getTr('协同'))
        self.menus_button.setToolTip(self.getTr('主菜单'))
        self.project_button.setToolTip(self.getTr('项目'))
        self.notice_button.setToolTip(self.getTr('信息'))
        self.external_tool_display.setToolTip(self.getTr('工具栏'))
        self.problem_button.setToolTip(self.getTr('帮助'))
        self.update_button.setToolTip(self.getTr('刷新'))
        self.recently_lately_button.setToolTip(self.getTr('最近项目'))
        self.count_label.setText(self.getTr('数量'))
        for widget_id, button in self.left_menu_map.items():
            if button == self.project_button: continue
            button.setToolTip(self.getTr(button.objectName()))
        for button in self.tools_menu_map:
            button.setToolTip(self.getTr(button.objectName()))

        pass

    def __initButtonTip(self, btn: QtWidgets.QPushButton, language_options: dict):
        """
        添加菜单按钮的
        :param btn:
        :param language_options:
        :return:
        """
        btn.setObjectName(list(language_options.keys())[0])
        self.tools_tr.add_tr(language_options)
        btn.setToolTip(self.getTr(btn.objectName()))
        self.tools_menu_map.append(btn)

    @QtCore.Slot()
    def restart(self):
        """
        界面重启
        :return:
        """
        # TODO: 校验当前状态是否保存
        QtWidgets.QApplication.quit()
        python = sys.executable
        script = Path(__file__).absolute()
        subprocess.Popen([python, script])
        self.widget_toast.showSucceed(self.getTr('重启成功'))
        sys.exit()

    def initMenus(self):
        """
        初始化下拉菜单
        :return:
        """
        self.menus_button.setMenu(None)
        menu = QtWidgets.QMenu(self.menus_button)
        menu.setMinimumSize(150, 0)
        # 文件子菜单
        file_menu = QtWidgets.QMenu(self.getTr('文件'), menu)
        open_dir = QtGui.QAction(self.getTr('打开目录'), file_menu)
        open_dir.triggered.connect(self.openDir)
        open_dir.setShortcut('Ctrl+O')
        setting = QtGui.QAction(self.getTr('设置'), file_menu)
        setting.setShortcut('Ctrl+Alt+S')
        setting.setIcon(QtGui.QIcon('icons:setting.png'))
        setting.triggered.connect(self.openSetting)
        close_project = QtGui.QAction(self.getTr('关闭项目'), file_menu)
        close_project.triggered.connect(self.closeProject)
        # save_data = QtGui.QAction(self.getTr('保存'), file_menu)
        restart = QtGui.QAction(self.getTr('重启'), file_menu)
        restart.triggered.connect(self.restart)
        # save_data.triggered.connect(self.saveData)
        # save_data.setShortcut('Ctrl+S')
        file_menu.addAction(open_dir)
        file_menu.addAction(setting)
        file_menu.addAction(close_project)
        # file_menu.addAction(save_data)
        file_menu.addAction(restart)
        menu.addMenu(file_menu)
        # 工具子菜单
        external_tools = QtWidgets.QMenu(self.getTr('工具'), menu)
        add_tools = QtGui.QAction(self.getTr('添加工具'), external_tools)
        add_tools.setIcon(QtGui.QIcon('icons:add.png'))
        add_tools.triggered.connect(self.plugManage.addModule)
        update_tools = QtGui.QAction(self.getTr('刷新工具'), external_tools)
        update_tools.setIcon(QtGui.QIcon('icons:刷新_refresh.svg'))
        update_tools.triggered.connect(self.plugManage.initTreeItem)
        external_tools.addAction(add_tools)
        external_tools.addAction(update_tools)
        menu.addMenu(external_tools)
        # 帮助子菜单
        helps = QtWidgets.QMenu(self.getTr('帮助'), menu)
        shortcut_help = QtGui.QAction(self.getTr('帮助文档'), helps)
        shortcut_help.setIcon(QtGui.QIcon('icons:help.png'))
        shortcut_help.setShortcut('Ctrl+Alt+H')
        # shortcut_help.triggered.connect(lambda: os.system('start {}'.format(help_website)))  # 直接跳转浏览器工具帮助页面
        official_website = QtGui.QAction(self.getTr('工具官网'), helps)
        # official_website.triggered.connect(lambda: os.system('start {}'.format(tool_website)))
        helps.addAction(shortcut_help)
        helps.addAction(official_website)
        menu.addMenu(helps)
        # self.menus_button.setPopupMode(QtWidgets.QToolButton.D)
        self.menus_button.setMenu(menu)

    def initRecentlyMenus(self):
        """
        初始化下拉菜单
        :return:
        """
        if not self.path_temp.cache_list: return
        menu = QtWidgets.QMenu(self.recently_lately_button)
        menu.setMinimumSize(150, 0)
        for i in self.path_temp.cache_list:
            shortcut = QtGui.QAction(i, menu)
            file_path = i.replace('\n', '')
            shortcut.triggered.connect(partial(self.recentlyProjectOpen, file_path))
            menu.addAction(shortcut)
        self.recently_lately_button.setMenu(menu)

    @QtCore.Slot(str)
    def recentlyProjectOpen(self, path: str):
        """
        最近打开项目
        :param path:
        :return:
        """
        is_open = tools.WidgetDialog().getInquire(
            title=self.getTr('打开项目'),
            text=self.getTr('是否打开此项目'),
            pos=self.getDialogPos()
        )
        if not is_open:
            return
        self.openDir(path)

    def addMenuButton(self, function, icon: str, menu_id: int, tip: dict | None = None, shortcut: str = None):
        """
        菜单添加按钮
        :param function: 按钮回调函数
        :param menu_id: 1：上左|2：上右|3：右上|4：右下|5：下右|6：下左|7：左下|8：左上|9:工具栏
        :param icon: 图标字符串
        :param tip: 图标提示
        :param shortcut: 按钮快捷键
        :return:
        """
        if any([True for menu in self.left_menu_map.values() if menu.objectName() == icon]):
            logging.warning('菜单添加重复请检查：{}'.format(icon))
            return
        match menu_id:
            case 1:
                button = QtWidgets.QPushButton(self.top_right_menu)
                button.setMinimumSize(QtCore.QSize(36, 36))
                button.setMaximumSize(QtCore.QSize(36, 36))
                self.top_right_menus_layout.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            case 2:
                button = None
                msg = f'{menu_id}对应菜单位置禁止添加,请检查'
                # button = QtWidgets.QPushButton(self.top_left_menu)
                # button.setMinimumSize(QtCore.QSize(36, 36))
                # button.setMaximumSize(QtCore.QSize(36, 36))
                # self.top_left_menus_layout.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            case 3:
                button = QtWidgets.QPushButton(self.right_top_menus)
                button.setMinimumSize(QtCore.QSize(26, 26))
                button.setMaximumSize(QtCore.QSize(26, 26))
                self.right_top_menus_layout.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            case 4:
                button = QtWidgets.QPushButton(self.right_bottom_menus)
                button.setMinimumSize(QtCore.QSize(26, 26))
                button.setMaximumSize(QtCore.QSize(26, 26))
                self.right_bottom_menus_layout.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            case 5:
                button = QtWidgets.QPushButton(self.bottom_right_menus)
                button.setMinimumSize(QtCore.QSize(26, 26))
                button.setMaximumSize(QtCore.QSize(26, 26))
                self.bottom_right_menus_layout.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            case 6:
                button = QtWidgets.QPushButton(self.bottom_left_menus)
                button.setMinimumSize(QtCore.QSize(26, 26))
                button.setMaximumSize(QtCore.QSize(26, 26))
                self.bottom_left_menus_layout.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            case 7:
                button = QtWidgets.QPushButton(self.left_bottom_menus)
                button.setMinimumSize(QtCore.QSize(26, 26))
                button.setMaximumSize(QtCore.QSize(26, 26))
                self.left_bottom_menus_layout.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            case 8:
                button = QtWidgets.QPushButton(self.left_top_menus)
                button.setMinimumSize(QtCore.QSize(26, 26))
                button.setMaximumSize(QtCore.QSize(26, 26))
                self.left_top_menus_layout.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            case 9:
                button = QtWidgets.QPushButton(self.tools_menus)
                button.setMinimumSize(QtCore.QSize(24, 24))
                button.setMaximumSize(QtCore.QSize(24, 24))
                self.tools_menus_layout.addWidget(button, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            case _:
                button = None
                msg = f'未找到{menu_id}对应菜单位置,请检查'

        if button:
            self.setMenusIcon(button, icon)
            button.setObjectName(icon)
            if shortcut:
                # shortcut = 'ALT+H'
                button.setShortcut(shortcut)
            button.clicked.connect(function)
            button.setStyleSheet(self.tools_temp.MENU_BUTTON_STYLE)
            if tip is None: return button
            self.__initButtonTip(button, tip)
            return button
        else:
            # noinspection PyUnboundLocalVariable
            logging.error(msg)
            self.widget_toast.showError(msg)
            return button

    @QtCore.Slot()
    def updateFiles(self) -> None:
        """
        更新文件列表
        :return:
        """
        if not self.tools_temp.OPEN_DIR_PATH:
            self.widget_toast.showInfo(self.getTr('当前未打开文件夹'))
            return
        self.openDir(self.tools_temp.OPEN_DIR_PATH)

    def treeMenus(self, pos: QtCore.QPoint) -> None:
        """
        文件菜单的右键菜单
        :param pos:
        :return:
        """
        index = self.dir_tree.currentIndex()
        file_path = Path(self.model.filePath(self.proxy_model.mapToSource(index)))
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
        itemMenu = popMenu.addAction(self.getTr('删除'))
        itemMenu.triggered.connect(
            lambda: os.remove(file_path) if Path(file_path).is_file() else shutil.rmtree(file_path))
        itemMenu = popMenu.addAction(self.getTr('复制文件路径'))
        itemMenu.triggered.connect(
            lambda: QtWidgets.QApplication.clipboard().setText(str(file_path)))
        itemMenu = popMenu.addAction(self.getTr('打开于资源管理器'))
        itemMenu.triggered.connect(
            lambda: os.system('explorer /select,"{}"'.format(str(file_path))))
        popMenu.exec(QtGui.QCursor.pos())
        popMenu.show()

    @QtCore.Slot(int)
    def showLeftMenu(self, menu_page_index=0) -> None:
        """
        显示与隐藏项目组件
        :return:
        """
        if self.tree_menus.isHidden():
            self.tree_menus.show()
            self.menu_stacked.setCurrentIndex(menu_page_index)
            self.left_menu_map[menu_page_index].setStyleSheet(self.tools_temp.MENU_BUTTON_CLICK_STYLE)
        else:
            show_stack_index = self.menu_stacked.currentIndex()
            self.left_menu_map[show_stack_index].setStyleSheet(self.tools_temp.MENU_BUTTON_STYLE)
            if menu_page_index == show_stack_index:
                self.tree_menus.hide()
            else:
                self.menu_stacked.setCurrentIndex(menu_page_index)
                self.left_menu_map[menu_page_index].setStyleSheet(self.tools_temp.MENU_BUTTON_CLICK_STYLE)

    @QtCore.Slot(str, str)
    def openDir(self, path=None, expression=None) -> None:
        """
        打开工作目录,多线程
        :param path: 打开的路径 str
        :param expression: 文件匹配式 rglob
        :return:
        """
        if not path:
            path = QtWidgets.QFileDialog.getExistingDirectory(self, self.getTr('选择文件夹'), self.path_temp.getCache())
        path_push = Path(path)
        if not path_push.exists():
            self.widget_toast.showError(self.getTr('文件夹不存在'))
        self.model.setRootPath(path)
        source_index = self.model.index(self.model.rootPath())
        self.proxy_model.setSourceModel(self.model)
        proxy_index = self.proxy_model.mapFromSource(source_index)
        self.dir_tree.setRootIndex(proxy_index)
        self.proxy_model.setFilterString(expression, path)

        file_count = len(list(path_push.rglob('*.*')))
        self.file_count.setText(str(file_count).zfill(5))
        self.path_temp.addCache(path)
        self.tools_temp.OPEN_DIR_PATH = str(path)
        project_settings_path = path_push / 'D0.ini'
        if project_settings_path.exists():
            self.project_settings = QtCore.QSettings(str(project_settings_path), QtCore.QSettings.IniFormat)
            tools_module = self.project_settings.value('MODULE')
            if tools_module:
                self.plugManage.startModule(tools_module)
        else:
            self.project_settings = None
        self.settings.setValue('lastOpenPath', path)
        self.setFilePath(path_push)
        self.recently_lately_button.setText(path_push.name)

        #     if path in self.path_temp.cache_list:
        #         del self.path_temp.cache_list[self.path_temp.cache_list.index(path)]
        #         self.initRecentlyMenus()
        #     return
        # root = QtWidgets.QTreeWidgetItem(self.dir_tree)
        # root.setText(0, path_push.name)
        # root.setText(1, str(path_push))
        # root.setIcon(0, QtGui.QIcon('icons:文件夹-关_folder-close.svg'))
        #
        # def threadFunc(path_dir):
        #     def recursionTree(node_path, node):
        #         count = 0
        #         for item in node_path.iterdir():
        #             if item.is_dir():
        #                 if expression and not list(item.rglob(f'*{expression}*')).__len__():
        #                     continue
        #                 dirs = QtWidgets.QTreeWidgetItem(node)
        #                 dirs.setText(0, item.name)
        #                 dirs.setText(1, item.__str__())
        #                 dirs.setIcon(0, QtGui.QIcon('icons:文件夹-关_folder-close.svg'))
        #                 count += recursionTree(item, dirs)
        #             else:
        #                 if expression and expression not in item.name: continue
        #                 file_type = filetype.guess(item.__str__()).mime if filetype.guess(item.__str__()) else ''
        #                 files = QtWidgets.QTreeWidgetItem(node)
        #                 files.setText(0, item.name)
        #                 files.setText(1, item.__str__())
        #                 open_dir_files.append(item.__str__())
        #                 if 'image' in file_type:
        #                     files.setIcon(0, QtGui.QIcon('icons:图片文件_image-files.svg'))
        #                 elif 'video' in file_type:
        #                     files.setIcon(0, QtGui.QIcon('icons:视频文件_video-file.svg'))
        #                 elif 'zip' in file_type:
        #                     files.setIcon(0, QtGui.QIcon('icons:压缩文件_file-zip.svg'))
        #                 elif item.suffix == '.txt':
        #                     files.setIcon(0, QtGui.QIcon('icons:txt文件_file-txt-one.svg'))
        #                 elif item.suffix == '.ini':
        #                     files.setIcon(0, QtGui.QIcon('icons:设置配置_setting-config.svg'))
        #                 elif item.suffix == '.d0':
        #                     files.setIcon(0, QtGui.QIcon('icons:数据文件_data-file.svg'))
        #                 else:
        #                     files.setIcon(0, QtGui.QIcon('icons:存疑文件_file-question.svg'))
        #                 count += 1
        #         return count
        #
        #     open_dir_files = []
        #     with tools.Loading():
        #         file_count = recursionTree(Path(path_dir), root)
        #     self.tools_temp.OPEN_DIR_FILES = open_dir_files
        #     self.file_count.setText(str(file_count).zfill(5))
        #
        # self.loading_thread = Thread(target=threadFunc, args=(path_push,), daemon=True)
        # self.loading_thread.start()
        # print(self.dir_tree.model())
        # self.path_temp.addCache(str(path_push))
        # self.tools_temp.OPEN_DIR_PATH = str(path_push)
        # project_settings_path = path_push / 'D0.ini'
        # if project_settings_path.exists():
        #     self.project_settings = QtCore.QSettings(str(project_settings_path), QtCore.QSettings.IniFormat)
        #     tools_module = self.project_settings.value('MODULE')
        #     if tools_module:
        #         self.plugManage.startModule(tools_module)
        #
        # else:
        #     self.project_settings = None
        # self.settings.setValue('lastOpenPath', str(path_push))
        # self.setFilePath(path_push)
        # self.recently_lately_button.setText(path_push.name)
        # self.widget_toast.showSucceed(self.getTr('文件夹读取成功'))

    def initPlug(self):
        """
        打开插件,多线程异步
        :return:
        """
        table = plug_manage.PlugManage(self)
        self.menu_stacked.addWidget(table)
        item = int(self.menu_stacked.count()) - 1
        btn = self.addMenuButton(
            lambda: self.showLeftMenu(menu_page_index=item),
            icon='icons:组件_components.svg',
            tip={'插件': {'English': 'plug'}},
            menu_id=8)
        self.left_menu_map[self.menu_stacked.count() - 1] = btn
        return table

    def showCanvasListWindow(self) -> None:
        """
        工具列表显示
        :return:
        """
        # TODO: 插件未打开或插件无需使用时无法打开
        if self.canvas_list.isHidden():
            self.canvas_list.show()
            self.tools_menus_background.show()
            self.setMenusIcon(self.external_tool_display, 'icons:预览-打开_preview-open.svg')
        else:
            self.canvas_list.hide()
            self.tools_menus_background.hide()
            self.setMenusIcon(self.external_tool_display, 'icons:预览-关闭_preview-close-one.svg')

    def setFilePath(self, path: Path) -> None:
        """
        设置文件路径
        :param path:
        :return:
        """
        self.file_path.setText(
            '<span style="color:#fbdc3e"> > </span>'.join(list(path.relative_to(self.tools_temp.OPEN_DIR_PATH).parts)))

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        鼠标点击事件
        :param event:
        :return:
        """
        self.tools_temp.MOVE_WINDOW_POSITION = window_event.isWindowMove(event)
        if self.tools_temp.IS_WINDOW_SIZE: self.tools_temp.IS_CLICK_WINDOW_SIZE = True

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        鼠标移动事件
        :param event:
        :return:
        """
        self.setFocus()
        self.moveWindow(event)
        self.setWindowSizeMouse(window_event.isWindowSize(self.width(), self.height(), event, self.isMaximized()))
        self.setWindowSize(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        鼠标松开事件
        :param event:
        :return:
        """
        self.tools_temp.MOVE_WINDOW_POSITION = None
        self.tools_temp.IS_CLICK_WINDOW_SIZE = False
        self.tools_temp.IS_MOVE_WINDOW = False
        self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)

    def setWindowSize(self, event: QtGui.QMouseEvent) -> None:
        """
        窗口大小改变
        :param event:
        :return:
        """
        if self.isFullScreen(): return
        if not self.tools_temp.IS_WINDOW_SIZE: return
        if not self.tools_temp.IS_CLICK_WINDOW_SIZE: return
        mouse_position = event.position().toPoint()
        match self.tools_temp.IS_WINDOW_SIZE:
            case 1:
                mouse_position += QtCore.QPoint(-3, -3)
                self.move(self.x() + mouse_position.x(), self.y() + mouse_position.y())
                self.resize(self.width() - mouse_position.x(), self.height() - mouse_position.y())
            case 2:
                mouse_position += QtCore.QPoint(3, -3)
                self.move(self.x(), self.y() + mouse_position.y())
                self.resize(mouse_position.x(), self.height() - mouse_position.y())
            case 3:
                mouse_position += QtCore.QPoint(-3, 3)
                self.move(self.x() + mouse_position.x(), self.y())
                self.resize(self.width() - mouse_position.x(), mouse_position.y())
            case 4:
                mouse_position += QtCore.QPoint(3, 3)
                self.resize(mouse_position.x(), mouse_position.y())
            case 5:
                mouse_position += QtCore.QPoint(0, -3)
                self.resize(self.width(), self.height() - mouse_position.y())
                self.move(self.x(), self.y() + mouse_position.y())
            case 6:
                mouse_position += QtCore.QPoint(0, 3)
                self.resize(self.width(), mouse_position.y())
            case 7:
                mouse_position += QtCore.QPoint(-3, 0)
                self.move(self.x() + mouse_position.x(), self.y())
                self.resize(self.width() - mouse_position.x(), self.height())
            case 8:
                mouse_position += QtCore.QPoint(3, 0)
                self.resize(mouse_position.x(), self.height())

    def moveWindow(self, event: QtGui.QMouseEvent) -> None:
        """
        窗口移动
        :param event:
        :return:
        """
        if self.isFullScreen(): return
        if not self.tools_temp.MOVE_WINDOW_POSITION: return
        if self.tools_temp.IS_CLICK_WINDOW_SIZE: return
        if self.isMaximized(): return
        self.tools_temp.IS_MOVE_WINDOW = True
        self.width()
        move_position = self.tools_temp.MOVE_WINDOW_POSITION - event.position()
        self.move(self.x() - move_position.x(), self.y() - move_position.y())

    def setWindowSizeMouse(self, pos_type: int) -> None:
        """
        窗口边缘鼠标样式
        :param pos_type:
        :return:
        """
        if self.isFullScreen(): return
        if self.tools_temp.IS_CLICK_WINDOW_SIZE: return
        self.tools_temp.IS_WINDOW_SIZE = pos_type
        match pos_type:
            case 1:
                self.setCursor(QtCore.Qt.CursorShape.SizeFDiagCursor)
            case 2:
                self.setCursor(QtCore.Qt.CursorShape.SizeBDiagCursor)
            case 3:
                self.setCursor(QtCore.Qt.CursorShape.SizeBDiagCursor)
            case 4:
                self.setCursor(QtCore.Qt.CursorShape.SizeFDiagCursor)
            case 5:
                self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
            case 6:
                self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
            case 7:
                self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
            case 8:
                self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
            case 0:
                self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)

    def initIcons(self) -> None:
        """
        窗口图标设置
        :return:
        """
        # 设置引用路径
        QtCore.QDir.addSearchPath('icons', Path(__file__).parent.joinpath('static/black_theme').__str__())
        # QtCore.QDir.addSearchPath('icons', Path(__file__).parent.joinpath('static/white_theme').__str__())
        menus_button = [
            (self.close_button, 'icons:关闭_close.svg'),
            (self.max_button, 'icons:方形_square.svg'),
            (self.min_button, 'icons:减_minus.svg'),
            (self.setting_button, 'icons:设置_setting.svg'),
            (self.plob_search_button, 'icons:搜索_search.svg'),
            (self.cooperate_with_button, 'icons:连接点_connection-point.svg'),
            (self.menus_button, 'icons:汉堡图标_hamburger-button.svg'),
            (self.recently_lately_button, 'icons:下_down.svg'),
            (self.notice_button, 'icons:消息_message-one.svg'),
            (self.external_tool_display, 'icons:预览-关闭_preview-close-one.svg'),
            (self.update_button, 'icons:刷新_refresh.svg'),
            (self.problem_button, 'icons:帮助中心_helpcenter.svg'),
            (self.project_button, 'icons:文件夹-关_folder-close.svg'),
            (self.icons_button, 'icons:logo.ico'),
        ]
        for btn, icon in menus_button:
            self.setMenusIcon(btn, icon)

    @staticmethod
    def setMenusIcon(button: QtWidgets.QPushButton, icon: str) -> None:
        """
        菜单按钮图标设置
        :param button: 菜单图标
        :param icon: 图标位置
        :return:
        """
        button.setIcon(QtGui.QIcon('{}'.format(icon)))

    @QtCore.Slot()
    def closeWindow(self) -> None:
        """
        窗口关闭事件
        :return:
        """
        self.saveSetting()
        self.path_temp.saveCache()
        self.close()

    @QtCore.Slot()
    def maximizeWindow(self) -> None:
        """
        窗口最大化事件
        :return:
        """
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def popUpWindowsMessage(self, message_type, title, message, call_back_fun=None) -> None:
        """
        窗口消息弹窗事件
        :param message_type: 消息类型 1:错误|2:警告|3:提示|4:询问
        :param title: 消息标题
        :param message: 消息内容
        :param call_back_fun: 询问成功回调函数,其余类型无用
        :return:
        """
        msg_box = QtWidgets.QMessageBox()
        match message_type:
            case 1:
                # 错误
                msg_box.critical(self, title, message)
            case 2:
                # 警告
                msg_box.warning(self, title, message)
            case 3:
                # 提示
                msg_box.information(self, title, message)
            case 4:
                # 确认继续
                choice = msg_box.question(self, title, message)
                if str(choice) == 'StandardButton.Yes':
                    if call_back_fun is None: return
                    call_back_fun()


def main():
    app = QtWidgets.QApplication(sys.argv)
    lockFile = QtCore.QLockFile("./D0.app.lock")
    if lockFile.tryLock(2000):
        win = HaiProMax()
        win.show()
        sys.exit(app.exec())
    else:
        print('已经运行')
        sys.exit(-1)


if __name__ == '__main__':
    main()
