from functools import partial

from PySide6 import QtWidgets, QtCore, QtGui
import logging
from threading import RLock
from utils.yun_type import YunType


class WidgetDialog:
    """
    AUTO_UI输入弹窗
    """
    VALUE = None

    def getInt(self, title, pos=None):
        intVal = QtGui.QIntValidator()
        intVal.setRange(0, 999)
        value = self.__show(title=title, pos=pos, val=intVal)
        logging.info(f"Input:{value}")

        return value

    def getText(self, title, pos=None):
        value = self.__show(title=title, pos=pos)
        logging.info(f"Input:{value}")

        return value

    def getInquire(self, title: str, text: str, pos=None):
        value = self.__show(title=title, pos=pos, is_input=False, text=text)
        logging.info(f"Inquire:{value}")

        return value

    def __show(self, title, pos, val=None, is_input=True, text=None) -> str | int | None:
        print('\a')
        self.VALUE = None
        dialog = QtWidgets.QDialog()
        dialog.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        dialog.resize(360, 120)
        dialog.setStyleSheet(u"* {\n"
                             "    color: rgb(223, 225, 229);\n"
                             "}\n"
                             "QDialog {\n"
                             "    background: rgb(43, 45, 48);\n"
                             "    border-radius: 20px;\n"
                             "}\n"
                             "QLineEdit {\n"
                             "    background: rgb(43, 45, 48);\n"
                             "    border-top: none;\n"
                             "    border-left: none;\n"
                             "    border-right: none;\n"
                             "    border-bottom: 1px solid red;\n"
                             "}\n"
                             "QLineEdit:focus {\n"
                             "    border-bottom: 1px solid rgb(0, 26, 255);\n"
                             "}\n"
                             "#widget {\n"
                             "    background: rgb(43, 45, 48);\n"
                             "}\n"
                             "QPushButton {\n"
                             "    background: rgb(57, 59, 64);\n"
                             "    color: rgb(223, 225, 229);\n"
                             "}")
        if pos:
            dialog.move(
                pos[0] - (dialog.width() / 2),
                pos[1] - (dialog.height() / 2)
            )
        horizontalLayout_2 = QtWidgets.QHBoxLayout(dialog)
        horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.setObjectName(u"verticalLayout")
        widget = QtWidgets.QWidget(dialog)
        widget.setObjectName(u"widget")
        verticalLayout_2 = QtWidgets.QVBoxLayout(widget)
        verticalLayout_2.setObjectName(u"verticalLayout_2")
        verticalLayout_2.setContentsMargins(-1, 0, -1, 0)

        lineEdit = QtWidgets.QLineEdit(widget)
        lineEdit.setObjectName(u"lineEdit")
        lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        if val:
            lineEdit.setValidator(val)

        def isOk():
            self.VALUE = lineEdit.text()
            if not is_input: self.VALUE = True
            dialog.close()
            pass

        def isCancel():
            self.VALUE = False
            dialog.close()

        lineEdit.returnPressed.connect(isOk)
        title_label = QtWidgets.QLabel(title)
        verticalLayout_2.addWidget(title_label)
        if is_input:
            verticalLayout_2.addWidget(lineEdit)
        else:
            lineEdit.hide()
            text_label = QtWidgets.QLabel(text)
            font = QtGui.QFont()
            font.setPointSize(12)
            text_label.setFont(font)
            verticalLayout_2.addWidget(text_label)
        verticalLayout.addWidget(widget)
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setObjectName(u"horizontalLayout")
        horizontalLayout.setContentsMargins(-1, -1, 6, -1)
        horizontalSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                 QtWidgets.QSizePolicy.Policy.Minimum)
        horizontalLayout.addItem(horizontalSpacer)
        pushButton = QtWidgets.QPushButton(dialog)
        pushButton2 = QtWidgets.QPushButton(dialog)
        pushButton.setText('OK')
        pushButton2.setText('Cancel')
        pushButton.setObjectName(u"pushButton")
        pushButton2.setObjectName(u"pushButton2")
        pushButton.clicked.connect(isOk)
        pushButton2.clicked.connect(isCancel)
        horizontalLayout.addWidget(pushButton)
        horizontalLayout.addWidget(pushButton2)
        verticalLayout.addLayout(horizontalLayout)
        horizontalLayout_2.addLayout(verticalLayout)
        dialog.exec()
        return self.VALUE


class WidgetMessage(metaclass=YunType):
    """
    AUTO_UI消息弹窗
    """
    single_lock = RLock()
    STACK = []
    STACK_COUNT = 0
    ICON = ''

    def showError(self, message: str, show_time=5000, call_back=None):
        """
        显示错误信息
        :param message: 消息内容
        :param show_time: 消息消失时间ms
        :param call_back: 点击回调函数
        :return:
        """
        logging.error(message)
        self.ICON = 'icons:错误_error.svg'
        self.__show(message, show_time, call_back)

    def showInfo(self, message: str, show_time=5000, call_back=None):
        """
        显示描述信息
        :param message: 消息内容
        :param show_time: 消息消失时间ms
        :param call_back: 点击回调函数
        :return:
        """
        logging.warning(message)
        self.ICON = 'icons:信息_info.svg'
        self.__show(message, show_time, call_back)

    def showSucceed(self, message: str, show_time=5000, call_back=None):
        """
        显示成功信息
        :param message: 消息内容
        :param show_time: 消息消失时间ms
        :param call_back: 点击回调函数
        :return:
        """
        logging.info(message)
        self.ICON = 'icons:正确的_correct.svg'
        self.__show(message, show_time, call_back)

    def __show(self, message: str, show_time, call_back) -> None:
        print('\a')
        TIMER = QtCore.QTimer()
        window_message = QtWidgets.QWidget()
        window_message.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        window_message.mouseReleaseEvent = lambda event: call_back()
        window_message.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        window_message.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        window_message.move(30, self.STACK[-1].y() + self.STACK[-1].height() - 20 if self.STACK else 55)
        window_message.setStyleSheet(u"#widget {\n"
                                     "    border-radius: 10px;\n"
                                     "    background: rgb(30, 31, 34);\n"
                                     "    border: 1px solid rgb(57, 59, 64);\n"
                                     "}\n"
                                     "QLabel{\n"
                                     "    color: #fff;\n"
                                     "}")
        horizontalLayout = QtWidgets.QHBoxLayout(window_message)
        horizontalLayout.setObjectName(u"horizontalLayout")
        widget = QtWidgets.QWidget(window_message)
        widget.setObjectName(u"widget")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(widget)
        horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        img = QtWidgets.QLabel(widget)
        img.setObjectName(u"img")
        img.setMinimumSize(QtCore.QSize(25, 25))
        img.setMaximumSize(QtCore.QSize(25, 25))
        img.setPixmap(QtGui.QPixmap(self.ICON))
        img.setScaledContents(True)
        horizontalLayout_2.addWidget(img)
        msg = QtWidgets.QLabel(widget)
        msg.setObjectName(u"msg")
        horizontalLayout_2.addWidget(msg)
        horizontalLayout.addWidget(widget)
        msg.setText(message)
        window_message.show()
        window_message.setWindowOpacity(1)
        TIMER.timeout.connect(partial(self.__close, window_message, TIMER))
        TIMER.start(show_time)
        self.STACK.append(window_message)

    def __close(self, widget: QtWidgets.QWidget, timer: QtCore.QTimer):
        timer.stop()
        widget.windowOpacity()
        animation = QtCore.QPropertyAnimation(widget, b'windowOpacity', widget)
        animation.setStartValue(1)
        animation.setEndValue(0)
        animation.setDuration(600)
        animation.start()
        widget.close()
        del self.STACK[self.STACK.index(widget)]
        for stack_widget in self.STACK:
            stack_widget: QtWidgets.QWidget
            stack_widget.move(stack_widget.x(), stack_widget.y() - widget.height() + 20)

