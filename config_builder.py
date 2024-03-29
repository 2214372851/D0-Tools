#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/13 10:47
# @Author  : yinhai
# @File    : config_builder.py
# @Project : V0.0.1-alpha
from collections import OrderedDict

from PySide6 import QtCore

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
        # {
        #     'name': 'definition',
        #     'type': 'select',
        #     '中文_options': ['清晰', '模糊'],
        #     'English_options': ['distinct', 'dim']
        # },
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
                '中文_options': ['人', '卡车', '汽车', '交通标志','停止标志-舍去', '摩托车', '单车', '红绿灯', '公共汽车'],
                'English_options': [
                    'person',
                    'truck',
                    'car',
                    'traffic_sign',
                    'stop_sign',
                    'motorcycle',
                    'bicycle',
                    'traffic_light',
                    'bus',
                ],
                'option_style': [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255),
                                 (128, 0, 128), (255, 165, 0)]
            },
            '属性1': {
                '中文_name': '属性1',
                'English_name': 'stats1',
                'type': 'select',
                '中文_options': [
                    '无',
                    '步行-人',
                    '跑步-人',
                    '站立的-人',
                    '坐着-人',
                    '绿色的信号灯',
                    '红色的信号灯',
                    '黄色的信号灯',
                    '有人骑',
                    '无人骑',
                    '出租车',
                    '警车',
                    '快递车',
                    '工业用车'
                ],
                'English_options': [
                    'empty',
                    'walking',
                    'running',
                    'standing',
                    'sitting',
                    'green',
                    'red',
                    'yellow',
                    'with_rider',
                    'without_rider',
                    'taxi',
                    'police',
                    'delivery',
                    'construction'
                ]
            },
            '属性2': {
                '中文_name': '属性2',
                'English_name': 'stats2',
                'type': 'select',
                '中文_options': [
                    '无',
                    '儿童-人',
                    '成年人-人',
                    '年长的-人',
                    '行人-信号灯',
                    '车辆-信号灯',
                    '黑的-车',
                    '白色的-车',
                    '银色的-车',
                    '红色的-车',
                    '蓝色的-车',
                    '绿色的-车',
                    '黄色的-车'
                ],
                'English_options': [
                    'empty',
                    'child',
                    'adult',
                    'senior',
                    'pedestrian',
                    'vehicle',
                    'black',
                    'white',
                    'silver',
                    'red',
                    'blue',
                    'green',
                    'yellow'
                ]
            },
            '属性3': {
                '中文_name': '属性3',
                'English_name': 'stats3',
                'type': 'select',
                '中文_options': [
                    '无',
                    '男性的-人',
                    '女性的-人',
                    '未指明的-人',
                    '移动的-车',
                    '停止的-车'
                ],
                'English_options': [
                    'empty',
                    'male',
                    'female',
                    'unspecified',
                    'moving',
                    'stopping'
                ]
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
            # '详情': {
            #     '中文_name': '模糊度',
            #     'English_name': 'info',
            #     'type': 'multiple',
            #     '中文_options': ['模糊', '清晰', '无'],
            #     'English_options': ['dim', 'distinct', 'notHave'],
            # },
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
        'role_mode': {'rect', 'poly', 'line', 'point', 'round'},
        # 'role_mode': {'rect'},
        # 绘画模式子模式（目前仅支持线模式的path选项与normal）
        'mode_type': 'path',
        # 标注模型
        'model': 'yolov8x.pt',
        # 模型清洗label
        # 'model_labels': {'truck', 'mouse', 'person', 'giraffe', 'bed',
        #                  'skateboard', 'cell phone', 'frisbee', 'bench', 'hot dog', 'bird', 'scissors',
        #                  'donut', 'broccoli', 'clock', 'teddy bear', 'tie', 'car', 'keyboard', 'kite',
        #                  'baseball glove', 'sports ball', 'toaster', 'elephant', 'parking meter', 'bowl',
        #                  'wine glass', 'laptop', 'tennis racket', 'tv', 'apple', 'bear', 'book', 'skis',
        #                  'dining table', 'sink', 'cow', 'fire hydrant', 'microwave', 'pizza', 'banana',
        #                  'fork', 'couch', 'sheep', 'orange', 'handbag', 'vase', 'horse', 'potted plant',
        #                  'oven', 'cake', 'cat', 'knife', 'stop sign', 'motorcycle', 'chair', 'cup',
        #                  'sandwich', 'spoon', 'refrigerator', 'carrot', 'dog', 'backpack', 'bottle',
        #                  'remote', 'toilet', 'surfboard', 'bicycle', 'umbrella', 'traffic light', 'hair drier',
        #                  'airplane', 'baseball bat', 'boat', 'bus', 'snowboard', 'zebra', 'toothbrush', 'train',
        #                  'suitcase'}
        'model_labels': {'person', 'truck', 'car', 'stop sign', 'motorcycle', 'bicycle', 'traffic light', 'bus'}

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

# 斐波那契数列
