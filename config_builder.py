#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/13 10:47
# @Author  : yinhai
# @File    : config_builder.py
# @Project : V0.0.1-alpha
from collections import OrderedDict
from PySide6 import QtCore
from typing import Literal, List, Dict, TypedDict

sets = QtCore.QSettings("D0.ini", QtCore.QSettings.IniFormat)

data = {
    'cn_name': 'cn_name',
    'en_name': 'en_name',
    'cn_info': 'cn_info',
    'en_info': 'en_info',
    'version': 'version',
    'cn_plug_type': 'plug_type_cn',
    'en_plug_type': 'plug_type_en',
    'import_path': 'Dome',
    'expiration_date': 5697679643,
    'auto_dir': True,
    'sidebar': True,
    'image_options': [
        {
            'name': 'definition',
            'type': 'select',
            '中文_options': ['清晰', '模糊'],
            'English_options': ['distinct', 'dim']
        },
        {
            'name': 'invalid',
            'type': 'button',
            '中文_options': ['有效', '无效'],
            'English_options': ['valid', 'invalid']
        },
    ],
    'canvas_options': {
        # 插件参数
        # 配置
        'options': OrderedDict({
            '标签': {
                '中文_name': '标签',
                'English_name': 'label',
                'type': 'select',
                '中文_options': ['手机', '脸'],
                'English_options': ['phone', 'fack'],
                'option_style': [(255, 0, 123), (123, 255, 255)]
            },
            # '实例': {
            #     'English_name': 'id',
            #     'type': 'inputInt',
            #     'color': [(25, 0, 0)]
            # },
            # '内容': {
            #     'English_name': 'com',
            #     'type': 'inputText'
            # },
            # '注释2': {
            #     'English_name': 'com',
            #     'type': 'inputText'
            # },
            # '性别': {
            #     'English_name': 'sex',
            #     'type': 'multiple',
            #     '中文_options': ['男', '女', '无'],
            #     'English_options': ['man', 'girl', 'notHave'],
            # },
            '详情': {
                '中文_name': '模糊度',
                'English_name': 'info',
                'type': 'multiple',
                '中文_options': ['模糊', '清晰', '无'],
                'English_options': ['dim', 'distinct', 'notHave'],
            },
        }),
        # 是否加密
        'encipher': False,
        # 绘画模式模块
        'version': 'version',
        # 矩形模式最小长宽
        'draw_rect_min_size': (10, 10),
        # 轮廓模式最小面积
        'draw_poly_min_size': 4,
        # 点模式点结束个数
        'draw_point_num': 10,
        # 点模式点属性样式
        'draw_point_attribute': {
            1: (0, 255, 0),
            2: (255, 0, 0),
            3: (0, 0, 255)
        },
        # 点模式连线
        'draw_point_line': [
            [[0, 1, 2, 3, 4], (255, 128, 255)],
            [[3, 5, 6, 7, 8, 9], (13, 128, 255)],
        ],
        # 展示文件类型
        'show_file_type': ['.png', '.jpg'],
        # 运行允许的模式
        'role_mode': {'rect', 'poly', 'line', 'point'},
        # 绘画模式子模式（目前仅支持线模式的path选项与normal）
        'mode_type': 'path',
        # 标注模型
        'model': 'yolov8x-seg.pt',
        # 模型清洗label
        'model_labels': {'person', 'bicycle', 'car', 'motorcycle', 'bus', 'train', 'truck',
                         'traffic light', 'stop sign'}


    },
}
'''
“人”、“自行车”、“汽车”、“摩托车”、“飞机”、“公共汽车”、“火车”、“卡车”、“船”、“红绿灯”、“消防栓”、“停车标志” , 
'停车计时器', '长凳', '鸟', '猫', '狗', '马', '羊', '牛', '大象', '熊', '斑马', '长颈鹿', “背包”、“雨伞”、
“手提包”、“领带”、“手提箱”、“飞盘”、“滑雪板”、“滑雪板”、“运动球”、“风筝”、“棒球棒”、“棒球手套” , '滑板', '冲浪板', 
'网球拍', '瓶子', '酒杯', '杯子', '叉子', '刀', '勺子', '碗', '香蕉', '苹果' 、“三明治”、“橙子”、“西兰花”、“胡萝卜”、
“热狗”、“披萨”、“甜甜圈”、“蛋糕”、“椅子”、“沙发”、“盆栽植物”、“床” 、“餐桌”、“厕所”、“电视”、“笔记本电脑”、“鼠标”、“遥控器”、
“键盘”、“手机”、“微波炉”、“烤箱”、“烤面包机”、“水槽” 、“冰箱”、“书”、“时钟”、“花瓶”、“剪刀”、“泰迪熊”、“吹风机”、“牙刷”
'''
sets.setValue('PROJECT', data)

sets.setValue('Module', 'MOZI_IMG')
sets.setValue('LASTFILENAME', '')
#
sets.sync()