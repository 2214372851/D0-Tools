#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/17 14:32
# @Author  : yinhai
# @File    : model_plug.py
# @Project : AUTO_UI_canvas
from canvas_plug.model_plug import ModelMode


class DrawPlug:
    """
    绘制模块插件
    """
    DrawMode = {}

    def getMode(self, mode_name: str) -> ModelMode:
        """
        获取对应绘制模块
        :param mode_name:
        :return:
        """
        print(mode_name, self.DrawMode)
        if mode_name not in self.DrawMode: raise ModuleNotFoundError('未找到对应绘制模块')
        return self.DrawMode[mode_name]

    def addDrawMode(self, mode: ModelMode):
        """
        添加对应绘制模块
        :param mode:
        :return:
        """
        print(mode.name)
        self.DrawMode[mode.name] = mode
