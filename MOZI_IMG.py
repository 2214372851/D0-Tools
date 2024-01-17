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
from pathlib import Path

import numpy as np
from PySide6 import QtWidgets, QtCore, QtGui

from canvas_plug.model_plug import ModelMode
from cmw import model_image_canvas
from module.PlugFactory import PlugOption


class MyMode(ModelMode):
    name = 'round'
    rule = 2
    is_fill = False

    def drawMode(self, mode_type: str, painter: QtGui.QPainter, draw_data: list[QtCore.QPointF], is_draw_point: bool,
                 point_style):
        # 画笔配置
        painter.drawRect(QtCore.QRectF(*draw_data))

    def drawData(self, mode_type: str, copy_temp_data: list, option_data: dict) -> tuple[list, dict]:
        return copy_temp_data, option_data

    def stopDraw(self, temp_data: list):
        if temp_data.__len__() == 2:
            return True
        return False


class Module(model_image_canvas.Canvas):
    # TODO: 读取配置、规范配置
    tool_cn_type = '标注工具'
    tool_cn_info = '墨子图像标注工具'
    tool_en_type = 'Tagging tool'
    tool_en_info = 'Mozi image annotation tool'
    expiration_date = 1706685073

    def __init__(self, option_filedata: dict):
        self.plugOption = PlugOption(**option_filedata)
        super().__init__(**self.plugOption.canvas_options)
        # self.drawPlug.addDrawMode(MyMode())

    def getShowButton(self):
        return super().getShowButton()

    def addPluginMode(self, mode_name, add_rule, del_rule, mode_draw_func) -> None:
        pass

    def mouseRelease(self, event: QtGui.QMouseEvent):
        super().mouseRelease(event)
        pass

    def keyPress(self, event: QtGui.QKeyEvent):
        super().keyPress(event)
        # if event.key() == QtCore.Qt.Key.Key_9:
        #     self.selectMode('round')
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

    def selectPath(self, filename: Path):
        super().selectPath(filename)

    @staticmethod
    def decode(path: Path):
        def crypt(buff, key):
            if key == 0:
                return buff
            buff_array = np.int32(bytearray(buff))
            size = len(buff)
            one = np.ones(size).astype(np.float32)
            size_array = one * size
            key_array = one * key
            i_array = np.arange(size)
            resut_array = (np.int32(size_array + key_array + i_array - size_array / key_array + one) % 256) ^ buff_array
            newbuff = bytearray(resut_array.tolist())
            return newbuff

        with path.open('rb') as im:
            buffs, keys = im.read(), 20230711
        HEAD_SIZE = 256
        if len(buffs) <= HEAD_SIZE:
            dst = crypt(buffs, keys)
        else:
            dst = crypt(buffs[:HEAD_SIZE], keys)
            dst = dst + buffs[HEAD_SIZE:]
        return QtGui.QPixmap.fromImage(QtGui.QImage.fromData(dst))


if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseDesktopOpenGL)
    app = QtWidgets.QApplication(sys.argv)
    win = Module()
    win.show()
    sys.exit(app.exec())
