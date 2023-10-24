# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HaiWindows.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QStackedWidget, QToolButton, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget, QSplitter)

class Ui_window(QWidget):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(714, 462)
        window.setMouseTracking(True)
        window.setStyleSheet(u"* {\n"
"    color: #fff;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgba(250, 0, 0);\n"
"}\n"
"\n"
"#centralwidget {\n"
"    border-radius: 8px;\n"
"}\n"
"#background {\n"
"    background-color: rgb(43, 45, 48);\n"
"    border-radius: 8px;\n"
"}\n"
"#top_menus {\n"
"    border-bottom: 2px solid rgb(30, 31, 34);\n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;\n"
"    margin-left: 2px;\n"
"    padding-right: 2px;\n"
"}\n"
"#right_menus {\n"
"    border-left: 1px solid rgb(30, 31, 34);\n"
"}\n"
"#left_menus, #tree_menus {\n"
"    border-right: 1px solid rgb(30, 31, 34);\n"
"}\n"
"#bottom_menus {\n"
"    border-top: 1px solid rgb(30, 31, 34);\n"
"}\n"
"#tools_menus_background {\n"
"    border-bottom: 1px solid rgb(30, 31, 34);\n"
"}\n"
"#close_button, #max_button, \n"
"#min_button, #setting_button, \n"
"#plob_search_button, #cooperate_with_button, \n"
"#icons_button, #menus_button, \n"
"#recently_lately_button {\n"
"    background-color: rgba(30, 30, 30, 0);\n"
"    margin-bottom:"
                        " 2px;\n"
"}\n"
"#close_button:hover {\n"
"    background-color: rgb(232, 17, 35);\n"
"    border-top-right-radius: 8px;\n"
"    margin-bottom: 2px;\n"
"}\n"
"#max_button:hover, \n"
"#recently_lately_button:hover, \n"
"#menus_button:hover, \n"
"#min_button:hover, \n"
"#setting_button:hover, \n"
"#plob_search_button:hover, \n"
"#cooperate_with_button:hover,\n"
"#project_button:hover {\n"
"    background-color: rgb(56, 58, 61);\n"
"    border-radius:none;\n"
"}\n"
"#project_button, #problem_button, \n"
"#notice_button, #update_button,\n"
"#external_tool_display {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(30, 30, 30, 0);\n"
"}\n"
"#project_button:hover, #problem_button:hover, \n"
"#notice_button:hover, #update_button:hover,\n"
"#external_tool_display:hover {\n"
"    /* background-color: rgb(53, 116, 239); \u9009\u4e2d\u989c\u8272*/\n"
"    background-color: rgb(56, 58, 61);\n"
"    border-radius:5px;\n"
"}\n"
"#dir_tree {\n"
"    background-color: rgba(30, 30, 30, 0);\n"
"    border: none;\n"
""
                        "}\n"
"QTreeWidget {\n"
"    outline: none;\n"
"}\n"
"QTreeWidget::item:selected {\n"
"    color: #fff;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(46, 67, 110, 1);\n"
"}\n"
"QTreeWidget::item {\n"
"    border: none;\n"
"    height: 20px;\n"
"    show-decoration-selected: 1;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    height:8px;\n"
"    background:rgba(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"    border-radius:4px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    width:8px;\n"
"    background:rgba(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"    border-radius:4px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    height:8px;\n"
"    background:rgba(255, 255, 255, 0.17);\n"
"    border-radius:4px;   \n"
"    min-width:20;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    width:8px;\n"
"    background:rgba(255, 255, 255, 0.17);\n"
"    border-radius:4px;   \n"
"    min-height:20;\n"
"}\n"
"QScrollBar::handle:horizontal:hover,\n"
"QScrollBar::handle:vertical:hover {\n"
"    background:rgba(255, 255, 255"
                        ", 0.3);\n"
"}\n"
"QScrollBar::sub-page:horizontal,\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-line:horizontal, \n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-line:vertical, \n"
"QScrollBar::add-line:vertical {\n"
"    background: rgba(255, 0, 0, 0);\n"
"}\n"
"QListWidget:vertical {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    border: none;\n"
"}\n"
"QListWidget::item {\n"
"    height: 20px;\n"
"}\n"
"#canvas {\n"
"    background-color: rgb(30, 31, 34);\n"
"}\n"
"#canvas_tool_list {\n"
"    border-top: 1px solid red(30, 31, 34);\n"
"}\n"
"QSplitter::handle {\n"
"    background: rgb(30, 31, 34);\n"
"}\n"
"#menus_button {\n"
"    background-color: rgba(0,0,0,0);\n"
"	border-radius:none;\n"
"    /* padding-right:3px; */\n"
"}\n"
"#menus_button::menu-indicator {\n"
"    image: none;\n"
"}\n"
".QToolTip {\n"
"    background-color: #f30000; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272 */\n"
"    color: #d30000; /* \u8bbe\u7f6e"
                        "\u6587\u672c\u989c\u8272 */\n"
"    border: 1px solid #180000; /* \u8bbe\u7f6e\u8fb9\u6846 */\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"    font-size: 12px; /* \u8bbe\u7f6e\u5b57\u4f53\u5927\u5c0f */\n"
"}")
        self.horizontalLayout = QHBoxLayout(window)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QWidget(window)
        self.background.setObjectName(u"background")
        self.background.setMouseTracking(True)
        self.background.setStyleSheet(u"")
        self.background_layout = QVBoxLayout(self.background)
        self.background_layout.setSpacing(0)
        self.background_layout.setObjectName(u"background_layout")
        self.background_layout.setContentsMargins(2, 2, 2, 2)
        self.top_menus = QWidget(self.background)
        self.top_menus.setObjectName(u"top_menus")
        self.top_menus.setMinimumSize(QSize(0, 36))
        self.top_menus.setMaximumSize(QSize(16777215, 36))
        self.top_menus.setMouseTracking(True)
        self.horizontalLayout_3 = QHBoxLayout(self.top_menus)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_right_menu = QWidget(self.top_menus)
        self.top_right_menu.setObjectName(u"top_right_menu")
        self.top_right_menu.setMinimumSize(QSize(36, 36))
        self.top_right_menu.setMaximumSize(QSize(16777215, 16777215))
        self.top_right_menu.setMouseTracking(True)
        self.top_right_menus_layout = QHBoxLayout(self.top_right_menu)
        self.top_right_menus_layout.setSpacing(8)
        self.top_right_menus_layout.setObjectName(u"top_right_menus_layout")
        self.top_right_menus_layout.setContentsMargins(0, 0, 0, 0)
        self.icons_button = QPushButton(self.top_right_menu)
        self.icons_button.setObjectName(u"icons_button")
        self.icons_button.setMinimumSize(QSize(36, 36))
        self.icons_button.setMaximumSize(QSize(36, 36))
        self.icons_button.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u"../static/black_theme/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.icons_button.setIcon(icon)
        self.icons_button.setIconSize(QSize(36, 36))

        self.top_right_menus_layout.addWidget(self.icons_button)

        self.menus_button = QToolButton(self.top_right_menu)
        self.menus_button.setObjectName(u"menus_button")
        self.menus_button.setMinimumSize(QSize(36, 36))
        self.menus_button.setMaximumSize(QSize(36, 36))
        icon1 = QIcon()
        icon1.addFile(u"../static/black_theme/\u6c49\u5821\u56fe\u6807_hamburger-button.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menus_button.setIcon(icon1)
        self.menus_button.setIconSize(QSize(16, 16))

        self.top_right_menus_layout.addWidget(self.menus_button)

        self.recently_lately_button = QPushButton(self.top_right_menu)
        self.recently_lately_button.setObjectName(u"recently_lately_button")
        self.recently_lately_button.setMinimumSize(QSize(36, 36))
        self.recently_lately_button.setMaximumSize(QSize(960, 36))
        self.recently_lately_button.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/22143/.designer/backup/staitc/black_theme/\u4e0b_down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recently_lately_button.setIcon(icon2)
        self.recently_lately_button.setIconSize(QSize(16, 16))
        self.recently_lately_button.setCheckable(False)
        self.recently_lately_button.setChecked(False)
        self.recently_lately_button.setAutoRepeat(False)
        self.recently_lately_button.setAutoExclusive(False)
        self.recently_lately_button.setAutoDefault(False)
        self.recently_lately_button.setFlat(False)

        self.top_right_menus_layout.addWidget(self.recently_lately_button, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.top_right_menu, 0, Qt.AlignLeft)

        self.top_left_menu = QWidget(self.top_menus)
        self.top_left_menu.setObjectName(u"top_left_menu")
        self.top_left_menu.setMouseTracking(True)
        self.top_left_menus_layout = QHBoxLayout(self.top_left_menu)
        self.top_left_menus_layout.setSpacing(8)
        self.top_left_menus_layout.setObjectName(u"top_left_menus_layout")
        self.top_left_menus_layout.setContentsMargins(0, 0, 0, 0)
        self.cooperate_with_button = QPushButton(self.top_left_menu)
        self.cooperate_with_button.setObjectName(u"cooperate_with_button")
        self.cooperate_with_button.setMinimumSize(QSize(36, 36))
        self.cooperate_with_button.setMaximumSize(QSize(36, 36))
        icon3 = QIcon()
        icon3.addFile(u"../static/black_theme/\u8fde\u63a5\u70b9_connection-point.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cooperate_with_button.setIcon(icon3)

        self.top_left_menus_layout.addWidget(self.cooperate_with_button)

        self.plob_search_button = QPushButton(self.top_left_menu)
        self.plob_search_button.setObjectName(u"plob_search_button")
        self.plob_search_button.setMinimumSize(QSize(36, 36))
        self.plob_search_button.setMaximumSize(QSize(36, 36))
        icon4 = QIcon()
        icon4.addFile(u"../static/black_theme/\u641c\u7d22_search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.plob_search_button.setIcon(icon4)

        self.top_left_menus_layout.addWidget(self.plob_search_button)

        self.setting_button = QPushButton(self.top_left_menu)
        self.setting_button.setObjectName(u"setting_button")
        self.setting_button.setMinimumSize(QSize(36, 36))
        self.setting_button.setMaximumSize(QSize(36, 36))
        icon5 = QIcon()
        icon5.addFile(u"../static/black_theme/\u8bbe\u7f6e_setting.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_button.setIcon(icon5)
        self.setting_button.setIconSize(QSize(20, 16))

        self.top_left_menus_layout.addWidget(self.setting_button)

        self.min_button = QPushButton(self.top_left_menu)
        self.min_button.setObjectName(u"min_button")
        self.min_button.setMinimumSize(QSize(35, 36))
        self.min_button.setMaximumSize(QSize(4525, 12425))
        icon6 = QIcon()
        icon6.addFile(u"../static/black_theme/\u51cf_minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.min_button.setIcon(icon6)

        self.top_left_menus_layout.addWidget(self.min_button, 0, Qt.AlignVCenter)

        self.max_button = QPushButton(self.top_left_menu)
        self.max_button.setObjectName(u"max_button")
        self.max_button.setMinimumSize(QSize(36, 36))
        self.max_button.setMaximumSize(QSize(36, 36))
        icon7 = QIcon()
        icon7.addFile(u"../static/black_theme/\u65b9\u5f62_square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.max_button.setIcon(icon7)
        self.max_button.setCheckable(False)

        self.top_left_menus_layout.addWidget(self.max_button)

        self.close_button = QPushButton(self.top_left_menu)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(36, 36))
        self.close_button.setMaximumSize(QSize(36, 36))
        self.close_button.setFocusPolicy(Qt.NoFocus)
        icon8 = QIcon()
        icon8.addFile(u"../static/black_theme/\u5173\u95ed_close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon8)
        self.close_button.setIconSize(QSize(16, 16))

        self.top_left_menus_layout.addWidget(self.close_button, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.top_left_menu, 0, Qt.AlignRight)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.background_layout.addWidget(self.top_menus)

        self.window_content_layout = QHBoxLayout()
        self.window_content_layout.setSpacing(0)
        self.window_content_layout.setObjectName(u"window_content_layout")
        self.left_menus = QWidget(self.background)
        self.left_menus.setObjectName(u"left_menus")
        self.left_menus.setMinimumSize(QSize(32, 0))
        self.left_menus.setMaximumSize(QSize(32, 16777215))
        self.left_menus.setMouseTracking(True)
        self.left_menus.setStyleSheet(u"")
        self.left_menus_layout = QVBoxLayout(self.left_menus)
        self.left_menus_layout.setSpacing(10)
        self.left_menus_layout.setObjectName(u"left_menus_layout")
        self.left_menus_layout.setContentsMargins(0, 0, 0, 0)
        self.left_top_menus = QWidget(self.left_menus)
        self.left_top_menus.setObjectName(u"left_top_menus")
        self.left_top_menus.setMinimumSize(QSize(32, 0))
        self.left_top_menus.setMaximumSize(QSize(32, 16777215))
        self.left_top_menus.setMouseTracking(True)
        self.left_top_menus_layout = QVBoxLayout(self.left_top_menus)
        self.left_top_menus_layout.setSpacing(8)
        self.left_top_menus_layout.setObjectName(u"left_top_menus_layout")
        self.left_top_menus_layout.setContentsMargins(0, 0, 0, 0)
        self.project_button = QPushButton(self.left_top_menus)
        self.project_button.setObjectName(u"project_button")
        self.project_button.setMinimumSize(QSize(26, 26))
        self.project_button.setMaximumSize(QSize(26, 26))
        icon9 = QIcon()
        icon9.addFile(u"../static/black_theme/\u6587\u4ef6\u5939-\u5173_folder-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.project_button.setIcon(icon9)
        self.project_button.setIconSize(QSize(16, 16))

        self.left_top_menus_layout.addWidget(self.project_button, 0, Qt.AlignHCenter)


        self.left_menus_layout.addWidget(self.left_top_menus, 0, Qt.AlignTop)

        self.left_bottom_menus = QWidget(self.left_menus)
        self.left_bottom_menus.setObjectName(u"left_bottom_menus")
        self.left_bottom_menus.setMouseTracking(True)
        self.left_bottom_menus_layout = QVBoxLayout(self.left_bottom_menus)
        self.left_bottom_menus_layout.setSpacing(8)
        self.left_bottom_menus_layout.setObjectName(u"left_bottom_menus_layout")
        self.left_bottom_menus_layout.setContentsMargins(0, 0, 0, 0)
        self.problem_button = QPushButton(self.left_bottom_menus)
        self.problem_button.setObjectName(u"problem_button")
        self.problem_button.setMinimumSize(QSize(26, 26))
        self.problem_button.setMaximumSize(QSize(26, 26))
        icon10 = QIcon()
        icon10.addFile(u"../static/black_theme/\u5e2e\u52a9\u4e2d\u5fc3_helpcenter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.problem_button.setIcon(icon10)
        self.problem_button.setIconSize(QSize(16, 16))

        self.left_bottom_menus_layout.addWidget(self.problem_button, 0, Qt.AlignHCenter)


        self.left_menus_layout.addWidget(self.left_bottom_menus, 0, Qt.AlignBottom)


        self.window_content_layout.addWidget(self.left_menus)

        self.center = QWidget(self.background)
        self.center.setObjectName(u"center")
        self.center.setMouseTracking(True)
        self.centent_layout = QVBoxLayout(self.center)
        self.centent_layout.setSpacing(0)
        self.centent_layout.setObjectName(u"centent_layout")
        self.centent_layout.setContentsMargins(0, 0, 0, 0)
        self.tools_menus_background = QWidget(self.center)
        self.tools_menus_background.setObjectName(u"tools_menus_background")
        self.tools_menus_background.setMinimumSize(QSize(0, 26))
        self.tools_menus_background.setMaximumSize(QSize(16777215, 26))
        self.tools_menus_background.setMouseTracking(True)
        self.tools_menus_background_layout = QHBoxLayout(self.tools_menus_background)
        self.tools_menus_background_layout.setSpacing(8)
        self.tools_menus_background_layout.setObjectName(u"tools_menus_background_layout")
        self.tools_menus_background_layout.setContentsMargins(0, 0, 0, 0)
        self.tools_menus = QWidget(self.tools_menus_background)
        self.tools_menus.setObjectName(u"tools_menus")
        self.tools_menus_layout = QHBoxLayout(self.tools_menus)
        self.tools_menus_layout.setSpacing(8)
        self.tools_menus_layout.setObjectName(u"tools_menus_layout")
        self.tools_menus_layout.setContentsMargins(6, 0, 6, 0)



        self.tools_menus_background_layout.addWidget(self.tools_menus, 0, Qt.AlignLeft)


        self.centent_layout.addWidget(self.tools_menus_background)

        self.canvas_content = QSplitter(self.center)
        self.canvas_content.setObjectName(u"canvas_content")
        self.centent_content__layout = QHBoxLayout(self.canvas_content)
        self.centent_content__layout.setSpacing(0)
        self.centent_content__layout.setObjectName(u"centent_content__layout")
        self.centent_content__layout.setContentsMargins(0, 0, 0, 0)
        self.tree_menus = QWidget(self.canvas_content)
        self.tree_menus.setObjectName(u"tree_menus")
        self.tree_menus.setMouseTracking(True)
        self.dir_layout = QVBoxLayout(self.tree_menus)
        self.dir_layout.setObjectName(u"dir_layout")
        self.menu_stacked = QStackedWidget(self.tree_menus)
        self.menu_stacked.setObjectName(u"menu_stacked")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dir_tree = QTreeWidget(self.page)
        __qtreewidgetitem = QTreeWidgetItem(self.dir_tree)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        self.dir_tree.setObjectName(u"dir_tree")
        self.dir_tree.setMouseTracking(True)
        self.dir_tree.setAutoFillBackground(False)
        self.dir_tree.setRootIsDecorated(True)
        self.dir_tree.setItemsExpandable(True)
        self.dir_tree.setHeaderHidden(True)
        self.dir_tree.header().setCascadingSectionResizes(False)
        self.dir_tree.header().setHighlightSections(False)
        self.dir_tree.header().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.dir_tree)

        self.menu_stacked.addWidget(self.page)
        # self.page_2 = QWidget()
        # self.page_2.setObjectName(u"page_2")
        # self.menu_stacked.addWidget(self.page_2)

        self.dir_layout.addWidget(self.menu_stacked)


        self.centent_content__layout.addWidget(self.tree_menus)

        self.canvas = QWidget(self.canvas_content)
        self.canvas.setObjectName(u"canvas")
        self.canvas.setEnabled(True)
        self.canvas.setMouseTracking(True)
        self.canvas_layout = QHBoxLayout(self.canvas)
        self.canvas_layout.setSpacing(0)
        self.canvas_layout.setObjectName(u"canvas_layout")
        self.canvas_layout.setContentsMargins(0, 0, 0, 0)

        self.centent_content__layout.addWidget(self.canvas)

        self.canvas_list = QWidget(self.canvas_content)
        self.canvas_list.setObjectName(u"canvas_list")
        self.canvas_list.setMouseTracking(True)
        self.canvas_tool_list_layout = QVBoxLayout(self.canvas_list)
        self.canvas_tool_list_layout.setObjectName(u"canvas_tool_list_layout")
        self.canvas_tool_list_top_layout = QHBoxLayout()
        self.canvas_tool_list_top_layout.setObjectName(u"canvas_tool_list_top_layout")
        self.count_label = QLabel(self.canvas_list)
        self.count_label.setObjectName(u"count_label")
        self.count_label.setMouseTracking(True)

        self.canvas_tool_list_top_layout.addWidget(self.count_label)

        self.count_value = QLabel(self.canvas_list)
        self.count_value.setObjectName(u"count_value")
        self.count_value.setMouseTracking(True)

        self.canvas_tool_list_top_layout.addWidget(self.count_value)


        self.canvas_tool_list_layout.addLayout(self.canvas_tool_list_top_layout)

        self.canvas_tool_list = QListWidget(self.canvas_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        self.canvas_tool_list.setObjectName(u"canvas_tool_list")
        self.canvas_tool_list.setMouseTracking(True)

        self.canvas_tool_list_layout.addWidget(self.canvas_tool_list)


        self.centent_content__layout.addWidget(self.canvas_list)

        self.centent_content__layout.setStretch(0, 1)
        self.centent_content__layout.setStretch(1, 4)
        self.centent_content__layout.setStretch(2, 1)

        self.centent_layout.addWidget(self.canvas_content)


        self.window_content_layout.addWidget(self.center)

        self.right_menus = QWidget(self.background)
        self.right_menus.setObjectName(u"right_menus")
        self.right_menus.setMinimumSize(QSize(32, 0))
        self.right_menus.setMaximumSize(QSize(32, 16777215))
        self.right_menus.setMouseTracking(True)
        self.right_menus_layout = QVBoxLayout(self.right_menus)
        self.right_menus_layout.setSpacing(10)
        self.right_menus_layout.setObjectName(u"right_menus_layout")
        self.right_menus_layout.setContentsMargins(0, 0, 0, 0)
        self.right_top_menus = QWidget(self.right_menus)
        self.right_top_menus.setObjectName(u"right_top_menus")
        self.right_top_menus.setMouseTracking(True)
        self.right_top_menus_layout = QVBoxLayout(self.right_top_menus)
        self.right_top_menus_layout.setSpacing(8)
        self.right_top_menus_layout.setObjectName(u"right_top_menus_layout")
        self.right_top_menus_layout.setContentsMargins(0, 0, 0, 0)
        self.notice_button = QPushButton(self.right_top_menus)
        self.notice_button.setObjectName(u"notice_button")
        self.notice_button.setMinimumSize(QSize(26, 26))
        self.notice_button.setMaximumSize(QSize(26, 26))
        icon12 = QIcon()
        icon12.addFile(u"../static/black_theme/\u6d88\u606f_message-one.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notice_button.setIcon(icon12)

        self.right_top_menus_layout.addWidget(self.notice_button, 0, Qt.AlignHCenter)

        self.external_tool_display = QPushButton(self.right_top_menus)
        self.external_tool_display.setObjectName(u"external_tool_display")
        self.external_tool_display.setMinimumSize(QSize(26, 26))
        self.external_tool_display.setMaximumSize(QSize(26, 26))
        icon13 = QIcon()
        icon13.addFile(u"../static/black_theme/\u9884\u89c8-\u5173\u95ed_preview-close-one.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.external_tool_display.setIcon(icon13)

        self.right_top_menus_layout.addWidget(self.external_tool_display, 0, Qt.AlignHCenter)


        self.right_menus_layout.addWidget(self.right_top_menus, 0, Qt.AlignTop)

        self.right_bottom_menus = QWidget(self.right_menus)
        self.right_bottom_menus.setObjectName(u"right_bottom_menus")
        self.right_bottom_menus.setMouseTracking(True)
        self.right_bottom_menus_layout = QVBoxLayout(self.right_bottom_menus)
        self.right_bottom_menus_layout.setSpacing(8)
        self.right_bottom_menus_layout.setObjectName(u"right_bottom_menus_layout")
        self.right_bottom_menus_layout.setContentsMargins(0, 0, 0, 0)
        self.update_button = QPushButton(self.right_bottom_menus)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setMinimumSize(QSize(26, 26))
        self.update_button.setMaximumSize(QSize(26, 26))
        icon14 = QIcon()
        icon14.addFile(u"../static/black_theme/\u5237\u65b0_refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.update_button.setIcon(icon14)

        self.right_bottom_menus_layout.addWidget(self.update_button, 0, Qt.AlignHCenter)


        self.right_menus_layout.addWidget(self.right_bottom_menus, 0, Qt.AlignBottom)


        self.window_content_layout.addWidget(self.right_menus)


        self.background_layout.addLayout(self.window_content_layout)

        self.bottom_menus = QWidget(self.background)
        self.bottom_menus.setObjectName(u"bottom_menus")
        self.bottom_menus.setMinimumSize(QSize(0, 26))
        self.bottom_menus.setMaximumSize(QSize(16777215, 26))
        self.bottom_menus.setMouseTracking(True)
        self.bottom_menus_layout = QHBoxLayout(self.bottom_menus)
        self.bottom_menus_layout.setSpacing(10)
        self.bottom_menus_layout.setObjectName(u"bottom_menus_layout")
        self.bottom_menus_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_left_menus = QWidget(self.bottom_menus)
        self.bottom_left_menus.setObjectName(u"bottom_left_menus")
        self.bottom_left_menus.setMouseTracking(True)
        self.bottom_left_menus_layout = QHBoxLayout(self.bottom_left_menus)
        self.bottom_left_menus_layout.setSpacing(8)
        self.bottom_left_menus_layout.setObjectName(u"bottom_left_menus_layout")
        self.bottom_left_menus_layout.setContentsMargins(6, 0, 0, 0)
        self.file_path = QLabel(self.bottom_left_menus)
        self.file_path.setObjectName(u"file_path")
        self.file_path.setMouseTracking(True)

        self.bottom_left_menus_layout.addWidget(self.file_path)


        self.bottom_menus_layout.addWidget(self.bottom_left_menus, 0, Qt.AlignLeft)

        self.bottom_right_menus = QWidget(self.bottom_menus)
        self.bottom_right_menus.setObjectName(u"bottom_right_menus")
        self.bottom_right_menus.setMouseTracking(True)
        self.bottom_right_menus_layout = QHBoxLayout(self.bottom_right_menus)
        self.bottom_right_menus_layout.setSpacing(8)
        self.bottom_right_menus_layout.setObjectName(u"bottom_right_menus_layout")
        self.bottom_right_menus_layout.setContentsMargins(0, 0, 6, 0)
        self.label_2 = QLabel(self.bottom_right_menus)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMouseTracking(True)

        self.bottom_right_menus_layout.addWidget(self.label_2)


        self.bottom_menus_layout.addWidget(self.bottom_right_menus, 0, Qt.AlignRight)


        self.background_layout.addWidget(self.bottom_menus)


        self.horizontalLayout.addWidget(self.background)


        self.retranslateUi(window)

        self.recently_lately_button.setDefault(False)


        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"Form", None))
        self.icons_button.setText("")
        self.menus_button.setText("")
        # self.recently_lately_button.setText(QCoreApplication.translate("window", u"HaiPro", None))
#if QT_CONFIG(tooltip)
        self.cooperate_with_button.setToolTip(QCoreApplication.translate("window", u"\u591a\u4eba\u534f\u540c", None))
#endif // QT_CONFIG(tooltip)
        self.cooperate_with_button.setText("")
#if QT_CONFIG(tooltip)
        self.plob_search_button.setToolTip(QCoreApplication.translate("window", u"\u968f\u5904\u641c\u7d22", None))
#endif // QT_CONFIG(tooltip)
        self.plob_search_button.setText("")
#if QT_CONFIG(tooltip)
        self.setting_button.setToolTip(QCoreApplication.translate("window", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.setting_button.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.setting_button.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.setting_button.setText("")
#if QT_CONFIG(tooltip)
        self.min_button.setToolTip(QCoreApplication.translate("window", u"\u6700\u5c0f\u5316\u7a97\u53e3", None))
#endif // QT_CONFIG(tooltip)
        self.min_button.setText("")
#if QT_CONFIG(tooltip)
        self.max_button.setToolTip(QCoreApplication.translate("window", u"\u6700\u5927\u5316\u7a97\u53e3", None))
#endif // QT_CONFIG(tooltip)
        self.close_button.setText("")
        self.project_button.setText("")
        self.problem_button.setText("")
        ___qtreewidgetitem = self.dir_tree.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("window", u"filename", None));

        __sortingEnabled = self.dir_tree.isSortingEnabled()
        self.dir_tree.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.dir_tree.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("window", u"sadasd", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("window", u"HAI", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("window", u"ASDASD", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem3.child(0)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("window", u"ASDASD", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("window", u"ASDASD", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem4.child(1)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem4.child(2)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem4.child(3)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem4.child(4)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem4.child(5)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem4.child(6)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem4.child(7)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem4.child(8)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem4.child(9)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem4.child(10)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem4.child(11)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem4.child(12)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem4.child(13)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem4.child(14)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem4.child(15)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem4.child(16)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem4.child(17)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem4.child(18)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem4.child(19)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem4.child(20)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem4.child(21)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem4.child(22)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem4.child(23)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem4.child(24)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem4.child(25)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem4.child(26)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem4.child(27)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem4.child(28)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem34 = ___qtreewidgetitem4.child(29)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem35 = ___qtreewidgetitem4.child(30)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem36 = ___qtreewidgetitem4.child(31)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem37 = ___qtreewidgetitem4.child(32)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem38 = ___qtreewidgetitem4.child(33)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem39 = ___qtreewidgetitem4.child(34)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem40 = ___qtreewidgetitem4.child(35)
        ___qtreewidgetitem40.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem41 = ___qtreewidgetitem4.child(36)
        ___qtreewidgetitem41.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem42 = ___qtreewidgetitem4.child(37)
        ___qtreewidgetitem42.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem43 = ___qtreewidgetitem4.child(38)
        ___qtreewidgetitem43.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
        self.dir_tree.setSortingEnabled(__sortingEnabled)

        self.count_label.setText(QCoreApplication.translate("window", u"\u603b\u6570\uff1a", None))
        self.count_value.setText(QCoreApplication.translate("window", u"100", None))

        __sortingEnabled1 = self.canvas_tool_list.isSortingEnabled()
        self.canvas_tool_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.canvas_tool_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("window", u"test 1", None));
        ___qlistwidgetitem1 = self.canvas_tool_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("window", u"test 2", None));
        self.canvas_tool_list.setSortingEnabled(__sortingEnabled1)

        self.notice_button.setText("")
        self.external_tool_display.setText("")
        self.update_button.setText("")
        self.file_path.setText(QCoreApplication.translate("window", u"newTools > haiPero", None))
        self.label_2.setText(QCoreApplication.translate("window", u"230043", None))
    # retranslateUi

