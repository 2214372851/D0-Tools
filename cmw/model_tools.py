#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/23 16:48
# @Author  : yinhai
# @File    : model_tools.py
# @Project : 全新UI_canvas
from typing import List, Dict

from PySide6 import QtWidgets, QtCore, QtGui


class SelectDialog:
    """
    选择对话框
    """
    state = False

    def __init__(self, canvas):
        self.canvas = canvas
        self.language = canvas.language
        self.options = self.initOption(canvas.options, self.language)

    def setData(self, data: dict):
        """
        设置数据
        :param data:
        :return:
        """
        for key, value in data.items():
            if key not in self.options: continue
            self.options[key]['value'] = value
        return self

    def showSelect(self):
        """
        显示选择对话框
        :return:
        """
        self.state = False
        option_window = QtWidgets.QDialog()
        option_window.setMinimumSize(QtCore.QSize(0, 0))
        option_window.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        option_window.setStyleSheet(u"* {\n"
                                    "    color: rgb(223, 225, 229);\n"
                                    "}\n"
                                    "QDialog {\n"
                                    "    background: rgb(43, 45, 48);\n"
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
                                    "QPushButton, QComboBox, QSpinBox {\n"
                                    "    background: rgb(57, 59, 64);\n"
                                    "}\n"
                                    "QComboBox:on {\n"
                                    "    background-color: rgb(43, 45, 48);\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "    outline: 1px solid #000000;/*\u9009\u4e2d\u9879\u5916\u8fb9\u6846*/\n"
                                    "    background-color: rgb(43, 45, 48); /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
                                    "    selection-color: #3377FF;/*\u4e0b\u62c9\u6846\u9009\u4e2d\u9879\u5b57\u4f53\u989c\u8272*/\n"
                                    "    selection-background-color:rgb(43, 45, 48);/* \u4e0b\u62c9\u6846\u9009\u4e2d\u9879\u7684\u80cc\u666f\u8272 */\n"
                                    "}\n"
                                    "QSpinBox {\n"
                                    ""
                                    "    border: none;\n"
                                    "}")
        option_window_layout = QtWidgets.QHBoxLayout(option_window)
        option_window_layout.setContentsMargins(0, 0, 0, -1)
        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.setContentsMargins(6, 12, 6, 6)
        self.showOptions(verticalLayout, option_window)
        dialogButton = QtWidgets.QHBoxLayout()
        dialogButton.setContentsMargins(-1, -1, 0, -1)
        horizontalSpacer = QtWidgets.QSpacerItem(40, 20)
        dialogButton.addItem(horizontalSpacer)
        save_button = QtWidgets.QPushButton(option_window)
        save_button.setText('OK')
        save_button.clicked.connect(lambda: self.close(option_window))
        dialogButton.addWidget(save_button)
        cancel_button = QtWidgets.QPushButton(option_window)
        cancel_button.setText('Cancel')
        cancel_button.clicked.connect(option_window.close)
        dialogButton.addWidget(cancel_button)
        verticalLayout.addLayout(dialogButton)
        option_window_layout.addLayout(verticalLayout)
        option_window.move(self.showPosition(option_window))
        option_window.exec()
        if self.state:
            return self.getData()
        else:
            return self.getData(False)

    @staticmethod
    def showPosition(option_window):
        option_window.show()
        pos = QtCore.QPoint()
        if QtGui.QCursor.pos().x() + option_window.width() < QtGui.QGuiApplication.primaryScreen().geometry().width():
            pos.setX(QtGui.QCursor.pos().x())
        else:
            pos.setX(QtGui.QGuiApplication.primaryScreen().geometry().width() - option_window.width())

        if (QtGui.QCursor.pos().y() + option_window.height() + 100) < QtGui.QGuiApplication.primaryScreen().geometry().height():
            pos.setY(QtGui.QCursor.pos().y())
        else:
            pos.setY(QtGui.QGuiApplication.primaryScreen().geometry().height() - option_window.height() - 100)
        return pos

    def showOptions(self, vertical_layout: QtWidgets.QVBoxLayout, dialog: QtWidgets.QDialog):
        """
        显示对话框配置
        :param vertical_layout:
        :param dialog:
        :return:
        """
        for option_name, option in self.options.items():
            title = QtWidgets.QLabel(dialog)
            title.setText(f'<div style="color: rgb(175, 84, 194); font-size: 15px">{option_name}</div>')
            vertical_layout.addWidget(title)
            option_type = option['type']
            if 'value' in option:
                value: str | list[str] | None | int = option['value']
            else:
                value = None
            if option_type == 'select':
                comboBox = QtWidgets.QComboBox(dialog)
                comboBox.addItems(option[f'{self.language}_options'])
                if value:
                    comboBox.setCurrentIndex(option[f'{self.language}_options'].index(value))
                vertical_layout.addWidget(comboBox)
                self.options[option_name]['value'] = comboBox.currentText
            elif option_type == 'inputInt':
                spinBox = QtWidgets.QSpinBox(dialog)
                if value:
                    spinBox.setValue(value)
                vertical_layout.addWidget(spinBox)
                self.options[option_name]['value'] = spinBox.value
            elif option_type == 'multiple':
                radioLayout = QtWidgets.QHBoxLayout()
                button_group = QtWidgets.QButtonGroup(dialog)

                for index, item in enumerate(option[f'{self.language}_options']):
                    rb = QtWidgets.QRadioButton()
                    button_group.addButton(rb)
                    if value == item:
                        rb.setChecked(True)
                    elif value is None and index == 0:
                        rb.setChecked(True)
                    rb.setText(item)
                    radioLayout.addWidget(rb)
                self.options[option_name]['value'] = button_group
                vertical_layout.addLayout(radioLayout)

            elif option_type == 'inputText':
                lineEdit = QtWidgets.QLineEdit(dialog)
                if value:
                    lineEdit.setText(value)
                vertical_layout.addWidget(lineEdit)
                self.options[option_name]['value'] = lineEdit.text

    def close(self, dialog: QtWidgets.QDialog):
        """
        关闭对话框
        :param dialog:
        :return:
        """
        self.state = True
        dialog.close()

    def getData(self, is_back=True):
        """
        获取数据
        :param is_back: 是否返回数据
        :return:
        """
        option_data = {}
        for key, value in self.options.items():
            if key == 'instance_style': continue
            option_type = value['type']
            if option_type == 'multiple':
                value_data = value['value'].checkedButton().text()
            else:
                value_data = value['value']()
            option_data[key] = value_data
            self.options[key]['value'] = value_data
        if is_back:
            return option_data
        else:
            return

    @staticmethod
    def initOption(option: dict, language: str) -> dict:
        """
        初始化选项
        :param option:
        :param language:
        :return:
        """
        if language == 'cn':
            return option
        else:
            new_options = {}
            for key, value in option.items():
                option_type = value['type']
                if 'input' in option_type:
                    new_options[value[f'{language}_name']] = {'type': value['type']}
                else:
                    new_options[value[f'{language}_name']] = {
                        'type': value['type'],
                        'options': value[f'{language}_options']
                    }
            return new_options
