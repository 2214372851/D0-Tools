#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/16 13:03
# @Author  : yinhai
# @File    : model_selected.py
# @Project : AUTO_UI_canvas
from PySide6 import QtCore


class Selected:
    """
    选择状态管理器
    """
    polyIndex: int | None = None
    pointIndex: int | None = None
    sideIndex: int | None = None
    isSelect: bool = False
    signal = None

    def __init__(self, main_ui):
        self.main_ui = main_ui

    def setSelect(self, poly_index: int, point_index: int | None = None, side_index: int | None = None):
        """
        设置选择状态
        :param poly_index: 轮廓id
        :param point_index: 点id
        :param side_index: 边id
        :return:
        """
        self.polyIndex = poly_index
        self.pointIndex = point_index
        self.sideIndex = side_index
        self.isSelect = True
        self.monitor()

    def clearSelect(self):
        """
        清除选择状态
        :return:
        """
        self.polyIndex = None
        self.pointIndex = None
        self.sideIndex = None
        self.isSelect = False

    @property
    def selectState(self):
        """
        获取选择状态
        :return:
        """
        if self.polyIndex is not None and self.pointIndex is not None and self.sideIndex is not None:
            return 3
        elif self.polyIndex is not None and self.pointIndex is not None:
            return 2
        elif self.polyIndex is not None:
            return 1
        else:
            return 0

    def monitor(self):
        """
        监控选择状态
        :return:
        """
        if self.signal is None: return
        self.signal()
        self.main_ui.update()

    def setSignal(self, signal):
        """
        设置信号
        :param signal:
        :return:
        """
        self.signal = signal

    def __str__(self):
        return 'D0 tools selected state\npolyIndex: {}\npointIndex: True\nsideIndex: True\nisSelect: True\n'.format(
            self.polyIndex,
            self.pointIndex,
            self.sideIndex,
            self.isSelect,
        )

    def __len__(self):
        return self.selectState
