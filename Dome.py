#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/28 16:56
# @Author  : yinhai
# @File    : Dome.py
# @Project : 全新UI_canvas
# '标签': {
#             'en_name': 'label',
#             'type': 'select',
#             'cn_options': ['0', '1', '2', '3', '4'],
#             'en_options': ['ptarget', 'himars', 'yellowCar', 'redCar', 'greenCar'],
#             'option_style': [(255, 0, 123), (123, 255, 255), (255, 128, 30), (23, 128, 30), (45, 45, 30)]
#         },
# '实例': {
#     'en_name': 'id',
#     'type': 'inputInt',
#     'color': [(25, 0, 0)]
# },
# '内容': {
#     'en_name': 'com',
#     'type': 'inputText'
# },
# '注释2': {
#     'en_name': 'com',
#     'type': 'inputText'
# },
# '性别': {
#     'en_name': 'sex',
#     'type': 'multiple',
#     'cn_options': ['男', '女', '无'],
#     'en_options': ['man', 'girl', 'notHave'],
# },
# '详情': {
#     'en_name': 'info',
#     'type': 'multiple',
#     'cn_options': ['模糊', '清晰', '无'],
#     'en_options': ['dim', 'distinct', 'notHave'],
# },
import sys
from PySide6 import QtWidgets, QtCore, QtGui
from pathlib import Path
from cmw import model_image_canvas
from canvas_plug.model_plug import ModelMode
from module.PlugFactory import PlugOption


class MyMode(ModelMode):
    name = 'plm'
    rule = 1
    is_fill = False

    def drawMode(self, mode_type: str, painter: QtGui.QPainter, draw_data: list[QtCore.QPointF], is_draw_point: bool,
                 point_style):
        painter.drawPolygon(draw_data)

    def drawData(self, mode_type: str, copy_temp_data: list, option_data: dict) -> tuple[list, dict]:
        return copy_temp_data, option_data
        pass


class Module(model_image_canvas.Canvas):

    # TODO: 读取配置、规范配置

    def __init__(self, option_filedata: dict):
        self.plugOption = PlugOption(**option_filedata)
        super().__init__(**self.plugOption.canvas_options)

    def getShowButton(self) -> list:
        return super().getShowButton()

    def addPluginMode(self, mode_name, add_rule, del_rule, mode_draw_func) -> None:
        pass

    def mouseRelease(self, event: QtGui.QMouseEvent):
        super().mouseRelease(event)
        pass

    def keyPress(self, event: QtGui.QKeyEvent):
        super().keyPress(event)

        if self.temp_data:
            if event.key() == QtCore.Qt.Key.Key_5:
                self.drawStop()
            return
        if event.key() == QtCore.Qt.Key.Key_1:
            self.selectMode('rect')
        elif event.key() == QtCore.Qt.Key.Key_2:
            self.selectMode('poly')
        elif event.key() == QtCore.Qt.Key.Key_3:
            self.selectMode('line')
            self.mode_type = 'path'
        elif event.key() == QtCore.Qt.Key.Key_4:
            self.selectMode('point')
        elif event.key() == QtCore.Qt.Key.Key_5:
            self.selectMode('plm')

        elif event.key() == QtCore.Qt.Key.Key_0:
            self.selectMode(None)
        elif event.key() == QtCore.Qt.Key.Key_L:
            print('添加模式')
            self.drawPlug.addDrawMode(MyMode())
        elif event.key() == QtCore.Qt.Key.Key_O:
            self.selectFile(Path(r"C:\Users\22143\Pictures\Saved Pictures\zhongguo1.jpg"))
        pass

    def keyRelease(self, event: QtGui.QKeyEvent):
        super().keyRelease(event)
        pass

    def mouseMove(self, event: QtGui.QMouseEvent):
        super().mouseMove(event)
        pass

    def mouseLeft(self, event: QtGui.QMouseEvent):
        super().mouseLeft(event)
        pass

    def mouseRight(self, event: QtGui.QMouseEvent):
        super().mouseRight(event)

    def selectFile(self, filename: Path):
        super().selectFile(filename)


if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseDesktopOpenGL)
    app = QtWidgets.QApplication(sys.argv)
    win = Module()
    win.show()
    sys.exit(app.exec())
