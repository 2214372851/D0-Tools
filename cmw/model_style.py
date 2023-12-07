#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/21 16:18
# @Author  : yinhai
# @File    : model_style.py
# @Project : 全新UI_canvas
from PySide6 import QtGui, QtCore

from utils.translate import Translate


class Style:
    def __init__(self, options: dict):
        self.lineWidth = 2
        # 被选中图像时线条颜色
        self.select_line_color = QtGui.QColor(255, 0, 0)
        self.select_point_color = QtGui.QColor(255, 255, 0)
        self.select_poly_color = QtGui.QColor(0, 0, 0)

        self.line_color = QtGui.QColor(0, 255, 94)
        self.point_color = QtGui.QColor(235, 203, 0)
        self.poly_color = QtGui.QColor(204, 51, 255)
        self.styleColor = [
            QtGui.QColor(255, 235, 238),
            QtGui.QColor(255, 205, 210),
            QtGui.QColor(239, 154, 154),
            QtGui.QColor(229, 115, 115),
            QtGui.QColor(239, 83, 80),
            QtGui.QColor(244, 67, 54),
            QtGui.QColor(229, 57, 53),
            QtGui.QColor(211, 47, 47),
            QtGui.QColor(198, 40, 40),
            QtGui.QColor(183, 28, 28),
            QtGui.QColor(255, 138, 128),
            QtGui.QColor(255, 82, 82),
            QtGui.QColor(255, 23, 68),
            QtGui.QColor(213, 0, 0),
            QtGui.QColor(252, 228, 236),
            QtGui.QColor(248, 187, 208),
            QtGui.QColor(244, 143, 177),
            QtGui.QColor(240, 98, 146),
            QtGui.QColor(236, 64, 122),
            QtGui.QColor(233, 30, 99),
            QtGui.QColor(216, 27, 96),
            QtGui.QColor(194, 24, 91),
            QtGui.QColor(173, 20, 87),
            QtGui.QColor(136, 14, 79),
            QtGui.QColor(255, 128, 171),
            QtGui.QColor(255, 64, 129),
            QtGui.QColor(245, 0, 87),
            QtGui.QColor(197, 17, 98),
            QtGui.QColor(243, 229, 245),
            QtGui.QColor(225, 190, 231),
            QtGui.QColor(206, 147, 216),
            QtGui.QColor(186, 104, 200),
            QtGui.QColor(171, 71, 188),
            QtGui.QColor(156, 39, 176),
            QtGui.QColor(142, 36, 170),
            QtGui.QColor(123, 31, 162),
            QtGui.QColor(106, 27, 154),
            QtGui.QColor(74, 20, 140),
            QtGui.QColor(234, 128, 252),
            QtGui.QColor(224, 64, 251),
            QtGui.QColor(213, 0, 249),
            QtGui.QColor(170, 0, 255),
            QtGui.QColor(237, 231, 246),
            QtGui.QColor(209, 196, 233),
            QtGui.QColor(179, 157, 219),
            QtGui.QColor(149, 117, 205),
            QtGui.QColor(126, 87, 194),
            QtGui.QColor(103, 58, 183),
            QtGui.QColor(94, 53, 177),
            QtGui.QColor(81, 45, 168),
            QtGui.QColor(69, 39, 160),
            QtGui.QColor(49, 27, 146),
            QtGui.QColor(179, 136, 255),
            QtGui.QColor(124, 77, 255),
            QtGui.QColor(101, 31, 255),
            QtGui.QColor(98, 0, 234),
            QtGui.QColor(232, 234, 246),
            QtGui.QColor(197, 202, 233),
            QtGui.QColor(159, 168, 218),
            QtGui.QColor(121, 134, 203),
            QtGui.QColor(92, 107, 192),
            QtGui.QColor(63, 81, 181),
            QtGui.QColor(57, 73, 171),
            QtGui.QColor(48, 63, 159),
            QtGui.QColor(40, 53, 147),
            QtGui.QColor(26, 35, 126),
            QtGui.QColor(140, 158, 255),
            QtGui.QColor(83, 109, 254),
            QtGui.QColor(61, 90, 254),
            QtGui.QColor(48, 79, 254),
            QtGui.QColor(227, 242, 253),
            QtGui.QColor(187, 222, 251),
            QtGui.QColor(144, 202, 249),
            QtGui.QColor(100, 181, 246),
            QtGui.QColor(66, 165, 245),
            QtGui.QColor(33, 150, 243),
            QtGui.QColor(30, 136, 229),
            QtGui.QColor(25, 118, 210),
            QtGui.QColor(21, 101, 192),
            QtGui.QColor(13, 71, 161),
            QtGui.QColor(130, 177, 255),
            QtGui.QColor(68, 138, 255),
            QtGui.QColor(41, 121, 255),
            QtGui.QColor(41, 98, 255),
            QtGui.QColor(225, 245, 254),
            QtGui.QColor(179, 229, 252),
            QtGui.QColor(129, 212, 250),
            QtGui.QColor(79, 195, 247),
            QtGui.QColor(41, 182, 246),
            QtGui.QColor(3, 169, 244),
            QtGui.QColor(3, 155, 229),
            QtGui.QColor(2, 136, 209),
            QtGui.QColor(2, 119, 189),
            QtGui.QColor(1, 87, 155),
            QtGui.QColor(128, 216, 255),
            QtGui.QColor(64, 196, 255),
            QtGui.QColor(0, 176, 255),
            QtGui.QColor(0, 145, 234),
            QtGui.QColor(224, 247, 250),
            QtGui.QColor(178, 235, 242),
            QtGui.QColor(128, 222, 234),
            QtGui.QColor(77, 208, 225),
            QtGui.QColor(38, 198, 218),
            QtGui.QColor(0, 188, 212),
            QtGui.QColor(0, 172, 193),
            QtGui.QColor(0, 151, 167),
            QtGui.QColor(0, 131, 143),
            QtGui.QColor(0, 96, 100),
            QtGui.QColor(132, 255, 255),
            QtGui.QColor(24, 255, 255),
            QtGui.QColor(0, 229, 255),
            QtGui.QColor(0, 184, 212),
            QtGui.QColor(224, 242, 241),
            QtGui.QColor(178, 223, 219),
            QtGui.QColor(128, 203, 196),
            QtGui.QColor(77, 182, 172),
            QtGui.QColor(38, 166, 154),
            QtGui.QColor(0, 150, 136),
            QtGui.QColor(0, 137, 123),
            QtGui.QColor(0, 121, 107),
            QtGui.QColor(0, 105, 92),
            QtGui.QColor(0, 77, 64),
            QtGui.QColor(167, 255, 235),
            QtGui.QColor(100, 255, 218),
            QtGui.QColor(29, 233, 182),
            QtGui.QColor(0, 191, 165),
            QtGui.QColor(232, 245, 233),
            QtGui.QColor(200, 230, 201),
            QtGui.QColor(165, 214, 167),
            QtGui.QColor(129, 199, 132),
            QtGui.QColor(102, 187, 106),
            QtGui.QColor(76, 175, 80),
            QtGui.QColor(67, 160, 71),
            QtGui.QColor(56, 142, 60),
            QtGui.QColor(46, 125, 50),
            QtGui.QColor(27, 94, 32),
            QtGui.QColor(185, 246, 202),
            QtGui.QColor(105, 240, 174),
            QtGui.QColor(0, 230, 118),
            QtGui.QColor(0, 200, 83),
            QtGui.QColor(241, 248, 233),
            QtGui.QColor(220, 237, 200),
            QtGui.QColor(197, 225, 165),
            QtGui.QColor(174, 213, 129),
            QtGui.QColor(156, 204, 101),
            QtGui.QColor(139, 195, 74),
            QtGui.QColor(124, 179, 66),
            QtGui.QColor(104, 159, 56),
            QtGui.QColor(85, 139, 47),
            QtGui.QColor(51, 105, 30),
            QtGui.QColor(204, 255, 144),
            QtGui.QColor(178, 255, 89),
            QtGui.QColor(118, 255, 3),
            QtGui.QColor(100, 221, 23),
            QtGui.QColor(249, 251, 231),
            QtGui.QColor(240, 244, 195),
            QtGui.QColor(230, 238, 156),
            QtGui.QColor(220, 231, 117),
            QtGui.QColor(212, 225, 87),
            QtGui.QColor(205, 220, 57),
            QtGui.QColor(192, 202, 51),
            QtGui.QColor(175, 180, 43),
            QtGui.QColor(158, 157, 36),
            QtGui.QColor(130, 119, 23),
            QtGui.QColor(244, 255, 129),
            QtGui.QColor(238, 255, 65),
            QtGui.QColor(198, 255, 0),
            QtGui.QColor(174, 234, 0),
            QtGui.QColor(255, 253, 231),
            QtGui.QColor(255, 249, 196),
            QtGui.QColor(255, 245, 157),
            QtGui.QColor(255, 241, 118),
            QtGui.QColor(255, 238, 88),
            QtGui.QColor(255, 235, 59),
            QtGui.QColor(253, 216, 53),
            QtGui.QColor(251, 192, 45),
            QtGui.QColor(249, 168, 37),
            QtGui.QColor(245, 127, 23),
            QtGui.QColor(255, 255, 141),
            QtGui.QColor(255, 255, 0),
            QtGui.QColor(255, 234, 0),
            QtGui.QColor(255, 214, 0),
            QtGui.QColor(255, 248, 225),
            QtGui.QColor(255, 236, 179),
            QtGui.QColor(255, 224, 130),
            QtGui.QColor(255, 213, 79),
            QtGui.QColor(255, 202, 40),
            QtGui.QColor(255, 193, 7),
            QtGui.QColor(255, 179, 0),
            QtGui.QColor(255, 160, 0),
            QtGui.QColor(255, 143, 0),
            QtGui.QColor(255, 111, 0),
            QtGui.QColor(255, 229, 127),
            QtGui.QColor(255, 215, 64),
            QtGui.QColor(255, 196, 0),
            QtGui.QColor(255, 171, 0),
            QtGui.QColor(255, 243, 224),
            QtGui.QColor(255, 224, 178),
            QtGui.QColor(255, 204, 128),
            QtGui.QColor(255, 183, 77),
            QtGui.QColor(255, 167, 38),
            QtGui.QColor(255, 152, 0),
            QtGui.QColor(251, 140, 0),
            QtGui.QColor(245, 124, 0),
            QtGui.QColor(239, 108, 0),
            QtGui.QColor(230, 81, 0),
            QtGui.QColor(255, 209, 128),
            QtGui.QColor(255, 171, 64),
            QtGui.QColor(255, 145, 0),
            QtGui.QColor(255, 109, 0),
            QtGui.QColor(251, 233, 231),
            QtGui.QColor(255, 204, 188),
            QtGui.QColor(255, 171, 145),
            QtGui.QColor(255, 138, 101),
            QtGui.QColor(255, 112, 67),
            QtGui.QColor(255, 87, 34),
            QtGui.QColor(244, 81, 30),
            QtGui.QColor(230, 74, 25),
            QtGui.QColor(216, 67, 21),
            QtGui.QColor(191, 54, 12),
            QtGui.QColor(255, 158, 128),
            QtGui.QColor(255, 110, 64),
            QtGui.QColor(255, 61, 0),
            QtGui.QColor(221, 44, 0),
            QtGui.QColor(239, 235, 233),
            QtGui.QColor(215, 204, 200),
            QtGui.QColor(188, 170, 164),
            QtGui.QColor(161, 136, 127),
            QtGui.QColor(141, 110, 99),
            QtGui.QColor(121, 85, 72),
            QtGui.QColor(109, 76, 65),
            QtGui.QColor(93, 64, 55),
            QtGui.QColor(78, 52, 46),
            QtGui.QColor(62, 39, 35),
            QtGui.QColor(250, 250, 250),
            QtGui.QColor(245, 245, 245),
            QtGui.QColor(238, 238, 238),
            QtGui.QColor(224, 224, 224),
            QtGui.QColor(189, 189, 189),
            QtGui.QColor(158, 158, 158),
            QtGui.QColor(117, 117, 117),
            QtGui.QColor(97, 97, 97),
            QtGui.QColor(66, 66, 66),
            QtGui.QColor(33, 33, 33),
            QtGui.QColor(236, 239, 241),
            QtGui.QColor(207, 216, 220),
            QtGui.QColor(176, 190, 197),
            QtGui.QColor(144, 164, 174),
            QtGui.QColor(120, 144, 156),
            QtGui.QColor(96, 125, 139),
            QtGui.QColor(84, 110, 122),
            QtGui.QColor(69, 90, 100),
            QtGui.QColor(55, 71, 79),
            QtGui.QColor(38, 50, 56),
            QtGui.QColor(255, 255, 255),
            QtGui.QColor(0, 0, 0),
        ]

        self.labelColor = {}
        language = Translate().getLanguage
        self.initStyle(options, language)

    def initStyle(self, options: dict, language: str, cls: int = 1):
        """
        初始化标签颜色
        :param options: 配置
        :param language: 语言
        :param cls: 类型
        :return:
        """
        # 标签区分颜色
        if cls == 1:
            labels = options['标签'][f'{language}_options']
            option_style = None
            if 'option_style' in options['标签']:
                option_style = options['标签']['option_style']
            self.setLabelColor(labels, option_style)
        if '实例' in options:
            for style in options['实例']['color']:
                self.styleColor.insert(0, QtGui.QColor(*style))

    def setLabelColor(self, labels: list, option_style: list):
        """
        设置标签颜色
        :param labels: 标签
        :param option_style: 样式
        :return:
        """
        if not option_style:
            for index, label in enumerate(labels):
                self.labelColor[label] = self.styleColor[index * 3:(index + 1) * 3]
        elif len(option_style) == len(labels):
            for index, label in enumerate(labels):
                self.labelColor[label] = self.toQColor([option_style[index], ] * 3)
        elif len(option_style) == len(labels) * 3:
            for index, label in enumerate(labels):
                self.labelColor[label] = self.toQColor(option_style[index * 3:(index + 1) * 3])
        else:
            raise ValueError('The color configuration in the configuration does not meet specifications')

    @staticmethod
    def toQColor(colors: list):
        """
        转换颜色为Qt颜色
        :param colors:
        :return:
        """
        return [QtGui.QColor(*color) for color in colors]

    def getGeneralStyle(self, is_select, index=None, label=None):
        """
        获取样式
        :param index: 索引
        :param label: 标签
        :param is_select: 是否选中状态 bool
        :return: 画笔， 轮廓填充， 点填充
        """
        if is_select:
            pen_color = self.select_line_color
            brush_poly_color = self.select_poly_color
            brush_point_color = self.select_point_color
        else:
            # 此处还需修改颜色获取逻辑
            if label:
                if label not in self.labelColor: raise ValueError('此标签不属于当前项目')
                pen_color, brush_poly_color, brush_point_color = self.labelColor[label]
            elif index is not None:
                pen_color, brush_poly_color, brush_point_color = [self.styleColor[index], ] * 3
            else:
                pen_color = self.line_color
                brush_poly_color = self.poly_color
                brush_point_color = self.point_color
        return self.getStyleEvent(pen_color, brush_poly_color, brush_point_color)

    def getStyleEvent(self, pen_color, brush_poly_color, brush_point_color):
        """
        获取样式事件
        :param pen_color:
        :param brush_poly_color:
        :param brush_point_color:
        :return:
        """
        pen = QtGui.QPen(
            pen_color,
            self.lineWidth,
            QtCore.Qt.PenStyle.SolidLine
        )
        brush_poly = QtGui.QBrush(
            brush_poly_color,
            QtCore.Qt.BrushStyle.SolidPattern
        )
        brush_point = QtGui.QBrush(
            brush_point_color,
            QtCore.Qt.BrushStyle.SolidPattern
        )
        return pen, brush_poly, brush_point
