#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/13 17:26
# @Author  : yinhai
# @File    : test.py
# @Project : V0.0.1-alpha
import json
from utils.tools import WidgetMessage
from PySide6 import QtWidgets, QtGui
from pathlib import Path
import sys


class Module(QtWidgets.QTextEdit):
    tool_cn_type = '文本编辑器'
    tool_cn_info = '文本编辑器'
    tool_en_type = 'textEditor'
    tool_en_info = 'textEditor'
    expiration_date = 1704042061
    sidebar = False
    isConfig = False

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.widget_toast = WidgetMessage()
        self.setStyleSheet('QTextEdit {background: #1e1f22;color: #fff}')

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        """
        拖拽事件
        :param event:
        :return:
        """
        event.accept()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        """
        拖拽释放事件
        :param event:
        :return:
        """
        drag_filename = Path(event.mimeData().text().replace('file:///', ''))
        try:
            if drag_filename.suffix == '.json':
                with drag_filename.open('r', encoding='utf-8') as f:
                    text = json.dumps(json.loads(f.read()), indent=4, ensure_ascii=False)


            elif drag_filename.suffix == '.txt':
                with drag_filename.open('r', encoding='utf-8') as f:
                    text = '\n\n'.join([json.dumps(eval(i), indent=4, ensure_ascii=False) for i in f.readlines()])
            else: return
            self.setText(text)
        except Exception as e:
            self.widget_toast.showError(f'文件格式错误：{e}')