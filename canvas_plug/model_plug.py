#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/17 15:44
# @Author  : yinhai
# @File    : model_plug.py
# @Project : AUTO_UI_canvas
from typing import List
from PySide6 import QtGui, QtCore
from abc import ABCMeta, abstractmethod


class ModelMode(metaclass=ABCMeta):
    """
    画布插件基类指定工厂模式
    """
    name = None
    rule = 1
    is_fill = False

    def __init__(self):
        if self.name is None:
            raise ValueError('请为插件配置name,rule,is_fill')

    @abstractmethod
    def drawMode(self, mode_type: str, painter: QtGui.QPainter, draw_data: List[QtCore.QPointF], is_draw_point: bool,
                 point_style):
        """
        此模式下的绘制方法
        :param mode_type: 模式类型
        :param painter: 画笔
        :param draw_data: 绘制的数据
        :param is_draw_point: 是否绘制点 已做预设
        :param point_style: 点样式 已做预设
        :return:
        """
        pass

    @abstractmethod
    def drawData(self, mode_type: str, copy_temp_data: list, option_data: dict) -> tuple[list, dict]:
        """
        此模式下数据保存方式
        :param mode_type:
        :param copy_temp_data:
        :param option_data:
        :return:
        """
        return copy_temp_data, option_data
