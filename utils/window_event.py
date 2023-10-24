from PySide6 import QtGui


def isWindowMove(event: QtGui.QMouseEvent):
    """
    是否移动窗口
    :param event: 鼠标事件
    :return: 允许移动的位置|None
    """
    position = event.position()
    if 6 < position.y() < 42:
        return position
    return None


def isWindowSize(width, height, event: QtGui.QMouseEvent, is_max):
    """
    判断鼠标位置用于改变窗口大小
    :param is_max: 是否最大化
    :param width: 视口宽度
    :param height: 视口高度
    :param event: 鼠标事件
    :return: 0:不符合|1：左上角|2：右上角|3：左下角|4：右下角|5：上|6：下|7：左|8：右
    """
    if is_max: return
    position = event.position()
    # print(position)
    threshold_value = 3
    if 0 < position.x() < threshold_value and 0 < position.y() < threshold_value:
        return 1
    elif 0 < width - position.x() < threshold_value and 0 < position.y() < threshold_value:
        return 2
    elif 0 < position.x() < threshold_value and 0 < height - position.y() < threshold_value:
        return 3
    elif 0 < width - position.x() < threshold_value and 0 < height - position.y() < threshold_value:
        return 4
    elif 0 < position.y() < threshold_value:
        return 5
    elif 0 < height - position.y() < threshold_value:
        return 6
    elif 0 < position.x() < threshold_value:
        return 7
    elif 0 < width - position.x() < threshold_value:
        return 8
    else:
        return 0
