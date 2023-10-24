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
                               QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget, QSplitter, QToolButton)


class Ui_window(QWidget):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(715, 462)
        self.setMouseTracking(True)
        self.window_layout = QVBoxLayout(window)
        self.window_layout.setSpacing(0)
        self.window_layout.setObjectName(u"window_layout")
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
        icon.addFile(u"../newTools/static/imgs/yunhai.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icons_button.setIcon(icon)
        self.icons_button.setIconSize(QSize(36, 36))

        self.top_right_menus_layout.addWidget(self.icons_button)

        self.menus_button = QToolButton(self.top_right_menu)
        self.menus_button.setObjectName(u"menus_button")
        self.menus_button.setMinimumSize(QSize(36, 36))
        self.menus_button.setMaximumSize(QSize(36, 36))
        icon1 = QIcon()
        icon1.addFile(u"static/black_theme/\u6c49\u5821\u56fe\u6807_hamburger-button.svg", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.menus_button.setIcon(icon1)
        self.menus_button.setIconSize(QSize(16, 16))

        self.top_right_menus_layout.addWidget(self.menus_button)

        self.recently_lately_button = QPushButton(self.top_right_menu)
        self.recently_lately_button.setObjectName(u"recently_lately_button")
        self.recently_lately_button.setMinimumSize(QSize(36, 36))
        self.recently_lately_button.setMaximumSize(QSize(960, 36))
        self.recently_lately_button.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u"static/black_theme/\u4e0b_down.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon3.addFile(u"static/black_theme/\u8fde\u63a5\u70b9_connection-point.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cooperate_with_button.setIcon(icon3)

        self.top_left_menus_layout.addWidget(self.cooperate_with_button)

        self.plob_search_button = QPushButton(self.top_left_menu)
        self.plob_search_button.setObjectName(u"plob_search_button")
        self.plob_search_button.setMinimumSize(QSize(36, 36))
        self.plob_search_button.setMaximumSize(QSize(36, 36))
        icon4 = QIcon()
        icon4.addFile(u"static/black_theme/\u67e5\u627e_find.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.plob_search_button.setIcon(icon4)

        self.top_left_menus_layout.addWidget(self.plob_search_button)

        self.setting_button = QPushButton(self.top_left_menu)
        self.setting_button.setObjectName(u"setting_button")
        self.setting_button.setMinimumSize(QSize(36, 36))
        self.setting_button.setMaximumSize(QSize(36, 36))
        icon5 = QIcon()
        icon5.addFile(u"static/black_theme/\u8bbe\u7f6e\u914d\u7f6e_setting-config.svg", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.setting_button.setIcon(icon5)
        self.setting_button.setIconSize(QSize(20, 16))

        self.top_left_menus_layout.addWidget(self.setting_button)

        self.min_button = QPushButton(self.top_left_menu)
        self.min_button.setObjectName(u"min_button")
        self.min_button.setMinimumSize(QSize(35, 36))
        self.min_button.setMaximumSize(QSize(4525, 12425))
        icon6 = QIcon()
        icon6.addFile(u"static/black_theme/\u51cf_minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.min_button.setIcon(icon6)

        self.top_left_menus_layout.addWidget(self.min_button, 0, Qt.AlignVCenter)

        self.max_button = QPushButton(self.top_left_menu)
        self.max_button.setObjectName(u"max_button")
        self.max_button.setMinimumSize(QSize(36, 36))
        self.max_button.setMaximumSize(QSize(36, 36))
        icon7 = QIcon()
        icon7.addFile(u"static/black_theme/\u65b9\u5f62_square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.max_button.setIcon(icon7)
        self.max_button.setCheckable(False)

        self.top_left_menus_layout.addWidget(self.max_button)

        self.close_button = QPushButton(self.top_left_menu)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(36, 36))
        self.close_button.setMaximumSize(QSize(36, 36))
        self.close_button.setFocusPolicy(Qt.NoFocus)
        icon8 = QIcon()
        icon8.addFile(u"static/black_theme/\u5173\u95ed_close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon8)
        self.close_button.setIconSize(QSize(16, 16))

        self.top_left_menus_layout.addWidget(self.close_button, 0, Qt.AlignRight | Qt.AlignVCenter)

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
        icon9.addFile(u"static/black_theme/\u6587\u4ef6\u5939-\u5173_folder-close.svg", QSize(), QIcon.Normal,
                      QIcon.Off)
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
        icon10.addFile(u"static/black_theme/\u5e2e\u52a9\u4e2d\u5fc3_helpcenter.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        self.pushButton = QPushButton(self.tools_menus)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMouseTracking(True)
        icon11 = QIcon()
        icon11.addFile(u"static/black_theme/\u7535\u6ce2_waves.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon11)

        self.tools_menus_layout.addWidget(self.pushButton)

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
        self.dir_tree = QTreeWidget(self.tree_menus)
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

        self.dir_layout.addWidget(self.dir_tree)

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
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
        QListWidgetItem(self.canvas_tool_list)
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
        icon12.addFile(u"static/black_theme/\u6d88\u606f_message-one.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notice_button.setIcon(icon12)

        self.right_top_menus_layout.addWidget(self.notice_button, 0, Qt.AlignHCenter)

        self.external_tool_display = QPushButton(self.right_top_menus)
        self.external_tool_display.setObjectName(u"external_tool_display")
        self.external_tool_display.setMinimumSize(QSize(26, 26))
        self.external_tool_display.setMaximumSize(QSize(26, 26))
        icon13 = QIcon()
        icon13.addFile(u"static/black_theme/\u9884\u89c8-\u6253\u5f00_preview-open.svg", QSize(), QIcon.Normal,
                       QIcon.Off)
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
        icon14.addFile(u"static/black_theme/\u5386\u53f2\u8bb0\u5f55_history.svg", QSize(), QIcon.Normal, QIcon.Off)
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

        self.window_layout.addWidget(self.background)

        # self.retranslateUi(window)

        self.recently_lately_button.setDefault(False)

        QMetaObject.connectSlotsByName(window)

    # setupUi

    # def retranslateUi(self, window):
    #     window.setWindowTitle(QCoreApplication.translate("window", u"Form", None))
    #     self.icons_button.setText("")
    #     self.menus_button.setText("")
    #     self.recently_lately_button.setText(QCoreApplication.translate("window", u"HaiPro", None))
    #     # if QT_CONFIG(tooltip)
    #     self.cooperate_with_button.setToolTip(QCoreApplication.translate("window", u"\u591a\u4eba\u534f\u540c", None))
    #     # endif // QT_CONFIG(tooltip)
    #     self.cooperate_with_button.setText("")
    #     # if QT_CONFIG(tooltip)
    #     self.plob_search_button.setToolTip(QCoreApplication.translate("window", u"\u968f\u5904\u641c\u7d22", None))
    #     # endif // QT_CONFIG(tooltip)
    #     self.plob_search_button.setText("")
    #     # if QT_CONFIG(tooltip)
    #     self.setting_button.setToolTip(QCoreApplication.translate("window", u"\u8bbe\u7f6e", None))
    #     # endif // QT_CONFIG(tooltip)
    #     # if QT_CONFIG(statustip)
    #     self.setting_button.setStatusTip("")
    #     # endif // QT_CONFIG(statustip)
    #     # if QT_CONFIG(whatsthis)
    #     self.setting_button.setWhatsThis("")
    #     # endif // QT_CONFIG(whatsthis)
    #     self.setting_button.setText("")
    #     # if QT_CONFIG(tooltip)
    #     self.min_button.setToolTip(QCoreApplication.translate("window", u"\u6700\u5c0f\u5316\u7a97\u53e3", None))
    #     # endif // QT_CONFIG(tooltip)
    #     self.min_button.setText("")
    #     # if QT_CONFIG(tooltip)
    #     self.max_button.setToolTip(QCoreApplication.translate("window", u"\u6700\u5927\u5316\u7a97\u53e3", None))
    #     # endif // QT_CONFIG(tooltip)
    #     self.close_button.setText("")
    #     self.project_button.setText("")
    #     self.problem_button.setText("")
    #     self.pushButton.setText("")
    #     ___qtreewidgetitem = self.dir_tree.headerItem()
    #     ___qtreewidgetitem.setText(0, QCoreApplication.translate("window", u"filename", None));
    #
    #     __sortingEnabled = self.dir_tree.isSortingEnabled()
    #     self.dir_tree.setSortingEnabled(False)
    #     ___qtreewidgetitem1 = self.dir_tree.topLevelItem(0)
    #     ___qtreewidgetitem1.setText(0, QCoreApplication.translate("window", u"sadasd", None));
    #     ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
    #     ___qtreewidgetitem2.setText(0, QCoreApplication.translate("window", u"HAI", None));
    #     ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
    #     ___qtreewidgetitem3.setText(0, QCoreApplication.translate("window", u"ASDASD", None));
    #     ___qtreewidgetitem4 = ___qtreewidgetitem3.child(0)
    #     ___qtreewidgetitem4.setText(0, QCoreApplication.translate("window", u"ASDASD", None));
    #     ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
    #     ___qtreewidgetitem5.setText(0, QCoreApplication.translate("window", u"ASDASD", None));
    #     ___qtreewidgetitem6 = ___qtreewidgetitem4.child(1)
    #     ___qtreewidgetitem6.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem7 = ___qtreewidgetitem4.child(2)
    #     ___qtreewidgetitem7.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem8 = ___qtreewidgetitem4.child(3)
    #     ___qtreewidgetitem8.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem9 = ___qtreewidgetitem4.child(4)
    #     ___qtreewidgetitem9.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem10 = ___qtreewidgetitem4.child(5)
    #     ___qtreewidgetitem10.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem11 = ___qtreewidgetitem4.child(6)
    #     ___qtreewidgetitem11.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem12 = ___qtreewidgetitem4.child(7)
    #     ___qtreewidgetitem12.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem13 = ___qtreewidgetitem4.child(8)
    #     ___qtreewidgetitem13.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem14 = ___qtreewidgetitem4.child(9)
    #     ___qtreewidgetitem14.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem15 = ___qtreewidgetitem4.child(10)
    #     ___qtreewidgetitem15.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem16 = ___qtreewidgetitem4.child(11)
    #     ___qtreewidgetitem16.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem17 = ___qtreewidgetitem4.child(12)
    #     ___qtreewidgetitem17.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem18 = ___qtreewidgetitem4.child(13)
    #     ___qtreewidgetitem18.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem19 = ___qtreewidgetitem4.child(14)
    #     ___qtreewidgetitem19.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem20 = ___qtreewidgetitem4.child(15)
    #     ___qtreewidgetitem20.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem21 = ___qtreewidgetitem4.child(16)
    #     ___qtreewidgetitem21.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem22 = ___qtreewidgetitem4.child(17)
    #     ___qtreewidgetitem22.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem23 = ___qtreewidgetitem4.child(18)
    #     ___qtreewidgetitem23.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem24 = ___qtreewidgetitem4.child(19)
    #     ___qtreewidgetitem24.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem25 = ___qtreewidgetitem4.child(20)
    #     ___qtreewidgetitem25.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem26 = ___qtreewidgetitem4.child(21)
    #     ___qtreewidgetitem26.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem27 = ___qtreewidgetitem4.child(22)
    #     ___qtreewidgetitem27.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem28 = ___qtreewidgetitem4.child(23)
    #     ___qtreewidgetitem28.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem29 = ___qtreewidgetitem4.child(24)
    #     ___qtreewidgetitem29.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem30 = ___qtreewidgetitem4.child(25)
    #     ___qtreewidgetitem30.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem31 = ___qtreewidgetitem4.child(26)
    #     ___qtreewidgetitem31.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem32 = ___qtreewidgetitem4.child(27)
    #     ___qtreewidgetitem32.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem33 = ___qtreewidgetitem4.child(28)
    #     ___qtreewidgetitem33.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem34 = ___qtreewidgetitem4.child(29)
    #     ___qtreewidgetitem34.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem35 = ___qtreewidgetitem4.child(30)
    #     ___qtreewidgetitem35.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem36 = ___qtreewidgetitem4.child(31)
    #     ___qtreewidgetitem36.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem37 = ___qtreewidgetitem4.child(32)
    #     ___qtreewidgetitem37.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem38 = ___qtreewidgetitem4.child(33)
    #     ___qtreewidgetitem38.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem39 = ___qtreewidgetitem4.child(34)
    #     ___qtreewidgetitem39.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem40 = ___qtreewidgetitem4.child(35)
    #     ___qtreewidgetitem40.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem41 = ___qtreewidgetitem4.child(36)
    #     ___qtreewidgetitem41.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem42 = ___qtreewidgetitem4.child(37)
    #     ___qtreewidgetitem42.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qtreewidgetitem43 = ___qtreewidgetitem4.child(38)
    #     ___qtreewidgetitem43.setText(0, QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     self.dir_tree.setSortingEnabled(__sortingEnabled)
    #
    #     self.count_label.setText(QCoreApplication.translate("window", u"\u603b\u6570\uff1a", None))
    #     self.count_value.setText(QCoreApplication.translate("window", u"100", None))
    #
    #     __sortingEnabled1 = self.canvas_tool_list.isSortingEnabled()
    #     self.canvas_tool_list.setSortingEnabled(False)
    #     ___qlistwidgetitem = self.canvas_tool_list.item(0)
    #     ___qlistwidgetitem.setText(QCoreApplication.translate("window", u"qweqwe", None));
    #     ___qlistwidgetitem1 = self.canvas_tool_list.item(1)
    #     ___qlistwidgetitem1.setText(QCoreApplication.translate("window", u"qwdasd", None));
    #     ___qlistwidgetitem2 = self.canvas_tool_list.item(2)
    #     ___qlistwidgetitem2.setText(QCoreApplication.translate("window", u"qwasd", None));
    #     ___qlistwidgetitem3 = self.canvas_tool_list.item(3)
    #     ___qlistwidgetitem3.setText(QCoreApplication.translate("window", u"qfsfs", None));
    #     ___qlistwidgetitem4 = self.canvas_tool_list.item(4)
    #     ___qlistwidgetitem4.setText(QCoreApplication.translate("window", u"sg", None));
    #     ___qlistwidgetitem5 = self.canvas_tool_list.item(5)
    #     ___qlistwidgetitem5.setText(QCoreApplication.translate("window", u"drfge", None));
    #     ___qlistwidgetitem6 = self.canvas_tool_list.item(6)
    #     ___qlistwidgetitem6.setText(QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qlistwidgetitem7 = self.canvas_tool_list.item(7)
    #     ___qlistwidgetitem7.setText(QCoreApplication.translate("window", u"asdfsd", None));
    #     ___qlistwidgetitem8 = self.canvas_tool_list.item(8)
    #     ___qlistwidgetitem8.setText(QCoreApplication.translate("window", u"f", None));
    #     ___qlistwidgetitem9 = self.canvas_tool_list.item(9)
    #     ___qlistwidgetitem9.setText(QCoreApplication.translate("window", u"ew", None));
    #     ___qlistwidgetitem10 = self.canvas_tool_list.item(10)
    #     ___qlistwidgetitem10.setText(QCoreApplication.translate("window", u"sd", None));
    #     ___qlistwidgetitem11 = self.canvas_tool_list.item(11)
    #     ___qlistwidgetitem11.setText(QCoreApplication.translate("window", u"f", None));
    #     ___qlistwidgetitem12 = self.canvas_tool_list.item(12)
    #     ___qlistwidgetitem12.setText(QCoreApplication.translate("window", u"sdfe", None));
    #     ___qlistwidgetitem13 = self.canvas_tool_list.item(13)
    #     ___qlistwidgetitem13.setText(QCoreApplication.translate("window", u"f", None));
    #     ___qlistwidgetitem14 = self.canvas_tool_list.item(14)
    #     ___qlistwidgetitem14.setText(QCoreApplication.translate("window", u"s", None));
    #     ___qlistwidgetitem15 = self.canvas_tool_list.item(15)
    #     ___qlistwidgetitem15.setText(QCoreApplication.translate("window", u"df", None));
    #     ___qlistwidgetitem16 = self.canvas_tool_list.item(16)
    #     ___qlistwidgetitem16.setText(QCoreApplication.translate("window", u"e", None));
    #     ___qlistwidgetitem17 = self.canvas_tool_list.item(17)
    #     ___qlistwidgetitem17.setText(QCoreApplication.translate("window", u"wf", None));
    #     ___qlistwidgetitem18 = self.canvas_tool_list.item(18)
    #     ___qlistwidgetitem18.setText(QCoreApplication.translate("window", u"d", None));
    #     ___qlistwidgetitem19 = self.canvas_tool_list.item(19)
    #     ___qlistwidgetitem19.setText(QCoreApplication.translate("window", u"s", None));
    #     ___qlistwidgetitem20 = self.canvas_tool_list.item(20)
    #     ___qlistwidgetitem20.setText(QCoreApplication.translate("window", u"ef", None));
    #     ___qlistwidgetitem21 = self.canvas_tool_list.item(21)
    #     ___qlistwidgetitem21.setText(QCoreApplication.translate("window", u"s", None));
    #     ___qlistwidgetitem22 = self.canvas_tool_list.item(22)
    #     ___qlistwidgetitem22.setText(QCoreApplication.translate("window", u"f", None));
    #     ___qlistwidgetitem23 = self.canvas_tool_list.item(23)
    #     ___qlistwidgetitem23.setText(QCoreApplication.translate("window", u"f", None));
    #     ___qlistwidgetitem24 = self.canvas_tool_list.item(24)
    #     ___qlistwidgetitem24.setText(QCoreApplication.translate("window", u"ef", None));
    #     ___qlistwidgetitem25 = self.canvas_tool_list.item(25)
    #     ___qlistwidgetitem25.setText(QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qlistwidgetitem26 = self.canvas_tool_list.item(26)
    #     ___qlistwidgetitem26.setText(QCoreApplication.translate("window", u"s", None));
    #     ___qlistwidgetitem27 = self.canvas_tool_list.item(27)
    #     ___qlistwidgetitem27.setText(QCoreApplication.translate("window", u"df", None));
    #     ___qlistwidgetitem28 = self.canvas_tool_list.item(28)
    #     ___qlistwidgetitem28.setText(QCoreApplication.translate("window", u"qd", None));
    #     ___qlistwidgetitem29 = self.canvas_tool_list.item(29)
    #     ___qlistwidgetitem29.setText(QCoreApplication.translate("window", u"as", None));
    #     ___qlistwidgetitem30 = self.canvas_tool_list.item(30)
    #     ___qlistwidgetitem30.setText(QCoreApplication.translate("window", u"da", None));
    #     ___qlistwidgetitem31 = self.canvas_tool_list.item(31)
    #     ___qlistwidgetitem31.setText(QCoreApplication.translate("window", u"sd", None));
    #     ___qlistwidgetitem32 = self.canvas_tool_list.item(32)
    #     ___qlistwidgetitem32.setText(QCoreApplication.translate("window", u"w", None));
    #     ___qlistwidgetitem33 = self.canvas_tool_list.item(33)
    #     ___qlistwidgetitem33.setText(QCoreApplication.translate("window", u"ea", None));
    #     ___qlistwidgetitem34 = self.canvas_tool_list.item(34)
    #     ___qlistwidgetitem34.setText(QCoreApplication.translate("window", u"f", None));
    #     ___qlistwidgetitem35 = self.canvas_tool_list.item(35)
    #     ___qlistwidgetitem35.setText(QCoreApplication.translate("window", u"ads", None));
    #     ___qlistwidgetitem36 = self.canvas_tool_list.item(36)
    #     ___qlistwidgetitem36.setText(QCoreApplication.translate("window", u"fa", None));
    #     ___qlistwidgetitem37 = self.canvas_tool_list.item(37)
    #     ___qlistwidgetitem37.setText(QCoreApplication.translate("window", u"d", None));
    #     ___qlistwidgetitem38 = self.canvas_tool_list.item(38)
    #     ___qlistwidgetitem38.setText(QCoreApplication.translate("window", u"aw", None));
    #     ___qlistwidgetitem39 = self.canvas_tool_list.item(39)
    #     ___qlistwidgetitem39.setText(QCoreApplication.translate("window", u"d", None));
    #     ___qlistwidgetitem40 = self.canvas_tool_list.item(40)
    #     ___qlistwidgetitem40.setText(QCoreApplication.translate("window", u"asdad", None));
    #     ___qlistwidgetitem41 = self.canvas_tool_list.item(41)
    #     ___qlistwidgetitem41.setText(QCoreApplication.translate("window", u"d", None));
    #     ___qlistwidgetitem42 = self.canvas_tool_list.item(42)
    #     ___qlistwidgetitem42.setText(QCoreApplication.translate("window", u"c", None));
    #     ___qlistwidgetitem43 = self.canvas_tool_list.item(43)
    #     ___qlistwidgetitem43.setText(QCoreApplication.translate("window", u"z", None));
    #     ___qlistwidgetitem44 = self.canvas_tool_list.item(44)
    #     ___qlistwidgetitem44.setText(QCoreApplication.translate("window", u"xcvb", None));
    #     ___qlistwidgetitem45 = self.canvas_tool_list.item(45)
    #     ___qlistwidgetitem45.setText(QCoreApplication.translate("window", u"g", None));
    #     ___qlistwidgetitem46 = self.canvas_tool_list.item(46)
    #     ___qlistwidgetitem46.setText(QCoreApplication.translate("window", u"n", None));
    #     ___qlistwidgetitem47 = self.canvas_tool_list.item(47)
    #     ___qlistwidgetitem47.setText(QCoreApplication.translate("window", u"fgn", None));
    #     ___qlistwidgetitem48 = self.canvas_tool_list.item(48)
    #     ___qlistwidgetitem48.setText(QCoreApplication.translate("window", u"fy", None));
    #     ___qlistwidgetitem49 = self.canvas_tool_list.item(49)
    #     ___qlistwidgetitem49.setText(QCoreApplication.translate("window", u"dg", None));
    #     ___qlistwidgetitem50 = self.canvas_tool_list.item(50)
    #     ___qlistwidgetitem50.setText(QCoreApplication.translate("window", u"\u65b0\u5efa\u9879\u76ee", None));
    #     ___qlistwidgetitem51 = self.canvas_tool_list.item(51)
    #     ___qlistwidgetitem51.setText(QCoreApplication.translate("window", u"th", None));
    #     ___qlistwidgetitem52 = self.canvas_tool_list.item(52)
    #     ___qlistwidgetitem52.setText(QCoreApplication.translate("window", u"dh", None));
    #     ___qlistwidgetitem53 = self.canvas_tool_list.item(53)
    #     ___qlistwidgetitem53.setText(QCoreApplication.translate("window", u"gfd", None));
    #     ___qlistwidgetitem54 = self.canvas_tool_list.item(54)
    #     ___qlistwidgetitem54.setText(QCoreApplication.translate("window", u"b", None));
    #     ___qlistwidgetitem55 = self.canvas_tool_list.item(55)
    #     ___qlistwidgetitem55.setText(QCoreApplication.translate("window", u"fgh", None));
    #     ___qlistwidgetitem56 = self.canvas_tool_list.item(56)
    #     ___qlistwidgetitem56.setText(QCoreApplication.translate("window", u"fg", None));
    #     ___qlistwidgetitem57 = self.canvas_tool_list.item(57)
    #     ___qlistwidgetitem57.setText(QCoreApplication.translate("window", u"h", None));
    #     ___qlistwidgetitem58 = self.canvas_tool_list.item(58)
    #     ___qlistwidgetitem58.setText(QCoreApplication.translate("window", u"gfb", None));
    #     ___qlistwidgetitem59 = self.canvas_tool_list.item(59)
    #     ___qlistwidgetitem59.setText(QCoreApplication.translate("window", u"f", None));
    #     ___qlistwidgetitem60 = self.canvas_tool_list.item(60)
    #     ___qlistwidgetitem60.setText(QCoreApplication.translate("window", u"g", None));
    #     self.canvas_tool_list.setSortingEnabled(__sortingEnabled1)
    #
    #     self.notice_button.setText("")
    #     self.external_tool_display.setText("")
    #     self.update_button.setText("")
    #     self.file_path.setText(QCoreApplication.translate("window", u"newTools > haiPero", None))
    #     self.label_2.setText(QCoreApplication.translate("window", u"230043", None))
    # retranslateUi
