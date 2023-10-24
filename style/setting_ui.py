from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                               QLayout, QPushButton, QSizePolicy, QSpacerItem,
                               QTabWidget, QVBoxLayout, QWidget)


class Ui_Setting(QWidget):
    def setupUi(self, Setting, set_language, language):
        if language == 'en':
            language = 'English'
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(550, 200)
        Setting.setMinimumSize(QSize(100, 100))
        Setting.setMaximumSize(QSize(550, 200))
        Setting.setStyleSheet(u"* {\n"
                              "    color: #b5b6b8;\n"
                              "}\n"
                              "#Setting {\n"
                              "    background: #2b2d30;\n"
                              "}\n"
                              "#tab_window {\n"
                              "    background: #2b2d30;\n"
                              "}#Setting {\n"
                              "    background: #2b2d30;\n"
                              "}\n"
                              "#tab_window {\n"
                              "    background: #2b2d30;\n"
                              "}\n"
                              "QTabWidget::pane {\n"
                              "    border: 1px solid #2b2d30;\n"
                              "}\n"
                              "QTabBar::tab{\n"
                              "    background-color: #2b2d30;\n"
                              "	font-family:Consolas;\n"
                              "	font-size:8pt;\n"
                              "	border-top-left-radius: 5px;\n"
                              "	border-top-right-radius: 5px;\n"
                              "	min-width: 8px;\n"
                              "	padding: 5px;\n"
                              "}\n"
                              "QTabBar::tab:selected{\n"
                              "    background-color: #1e1f22;\n"
                              "}\n"
                              "QTabBar::tab:hover {\n"
                              "    background-color: #1e1f22;\n"
                              "}\n"
                              "QTabWidget::pane {\n"
                              "    border: 1px solid #2b2d30;\n"
                              "}\n"
                              "QTabBar::tab{\n"
                              "    background-color: #2b2d30;\n"
                              "	font-family:Consolas;\n"
                              "	font-size:8pt;\n"
                              "	color:#ced4da;\n"
                              "	border-top-left-radius: 5px;\n"
                              "	border-top-right-radius: 5px;\n"
                              "	min-width: 8px;\n"
                              "	padding: 5px;\n"
                              "}\n"
                              "QTabBar::tab:hover {\n"
                              "    background-color: #1e1f22;\n"
                              "}\n"
                              "#user {\n"
                              ""
                              "    background-color: #1e1f22;\n"
                              "    border-radius: 10px;\n"
                              "}\n"
                              "QPushButton {\n"
                              "    background: #1e1f22;\n"
                              "}\n"
                              "QPushButton:hover {\n"
                              "    background: #1e1f22;\n"
                              "}\n"
                              "QComboBox{\n"
                              "    background: #2b2d30;\n"
                              "    font-size:14px;\n"
                              "    padding: 1px 15px 1px 3px;\n"
                              "    border:1px solid #1e1f22;\n"
                              "    border-radius:5px 5px 0px 0px;\n"
                              "  } \n"
                              "QComboBox::drop-down {\n"
                              "    subcontrol-origin: padding;\n"
                              "    subcontrol-position: top right;\n"
                              "    width: 15px;\n"
                              "    border:none;\n"
                              "}\n"
                              "QComboBox QAbstractItemView{\n"
                              "	background:#2b2d30;\n"
                              "    border:1px solid #1e1f22;\n"
                              "    border-radius:0px 0px 5px 5px;\n"
                              "	font-size:14px;\n"
                              "    outline: 0px;\n"
                              "  }")
        self.verticalLayout_2 = QVBoxLayout(Setting)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tab_window = QTabWidget(Setting)
        self.tab_window.setObjectName(u"tab_window")
        self.user_page = QWidget()
        self.user_page.setObjectName(u"user_page")
        self.verticalLayout_3 = QVBoxLayout(self.user_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.user = QWidget(self.user_page)
        self.user.setObjectName(u"user")
        self.verticalLayout = QVBoxLayout(self.user)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(100, 0, 20, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.username = QLabel(self.user)
        self.username.setObjectName(u"username")
        self.username.setMouseTracking(False)
        self.username.setTabletTracking(False)
        self.username.setAcceptDrops(False)

        self.horizontalLayout_2.addWidget(self.username)

        self.username_value = QLabel(self.user)
        self.username_value.setObjectName(u"username_value")

        self.horizontalLayout_2.addWidget(self.username_value)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.validity = QLabel(self.user)
        self.validity.setObjectName(u"validity")

        self.horizontalLayout_3.addWidget(self.validity)

        self.validity_value = QLabel(self.user)
        self.validity_value.setObjectName(u"validity_value")

        self.horizontalLayout_3.addWidget(self.validity_value)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.addWidget(self.user)

        self.userVerticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.userVerticalSpacer_2)

        self.pushButton = QPushButton(self.user_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))

        self.verticalLayout_3.addWidget(self.pushButton)

        self.userVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.userVerticalSpacer)

        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.tab_window.addTab(self.user_page, "")
        self.general_page = QWidget()
        self.general_page.setObjectName(u"general_page")
        self.verticalLayout_4 = QVBoxLayout(self.general_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.language = QLabel(self.general_page)
        self.language.setObjectName(u"language")

        self.horizontalLayout.addWidget(self.language)

        self.language_value = QComboBox(self.general_page)
        self.language_value.addItem("1")
        self.language_value.addItem("1")
        self.language_value.setObjectName(u"language_value")
        if language:
            self.language_value.setCurrentIndex(['中文', 'English'].index(language))
        self.language_value.currentIndexChanged.connect(lambda : set_language(self.language_value.currentText()))

        self.horizontalLayout.addWidget(self.language_value)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.update = QLabel(self.general_page)
        self.update.setObjectName(u"update")

        self.horizontalLayout_4.addWidget(self.update)

        self.update_value = QPushButton(self.general_page)
        self.update_value.setObjectName(u"update_value")

        self.horizontalLayout_4.addWidget(self.update_value)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 2)
        self.tab_window.addTab(self.general_page, "1")

        self.verticalLayout_2.addWidget(self.tab_window)

        self.retranslateUi(Setting)

        self.tab_window.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Setting)

    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"Form", None))
        self.username.setText(QCoreApplication.translate("Setting", u"\u8d26\u53f7\uff1a", None))
        self.username_value.setText(QCoreApplication.translate("Setting", u"admin", None))
        self.validity.setText(QCoreApplication.translate("Setting", u"\u6709\u6548\u671f\uff1a", None))
        self.validity_value.setText(QCoreApplication.translate("Setting", u"2023-6-16", None))
        self.pushButton.setText(QCoreApplication.translate("Setting", u"\u6ce8\u9500", None))
        self.tab_window.setTabText(self.tab_window.indexOf(self.user_page),
                                   QCoreApplication.translate("Setting", u"\u8d26\u53f7\u8bbe\u7f6e", None))
        self.language.setText(QCoreApplication.translate("Setting", u"\u8bed\u8a00\uff1a", None))
        self.language_value.setItemText(0, QCoreApplication.translate("Setting", u"\u4e2d\u6587", None))
        self.language_value.setItemText(1, QCoreApplication.translate("Setting", u"English", None))

        self.update.setText(QCoreApplication.translate("Setting", u"\u66f4\u65b0\uff1a", None))
        self.update_value.setText(QCoreApplication.translate("Setting", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.tab_window.setTabText(self.tab_window.indexOf(self.general_page),
                                   QCoreApplication.translate("Setting", u"\u901a\u7528\u8bbe\u7f6e", None))