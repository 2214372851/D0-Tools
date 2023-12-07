#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/15 09:59
# @Author  : yinhai
# @File    : translate.py
# @Project : 全新UI
from utils.yun_type import YunType


class Translate(metaclass=YunType):
    __language = '中文'
    __translate_dict = {
        '文件操作': {'English': 'File Operation'},
        '当前未打开文件夹': {'English': 'The Folder Is Not Currently Open'},
        '错误': {'English': 'Error'},
        '配置操作': {'English': 'Configuration Operation'},
        '未找到配置文件': {'English': 'Configuration File Not Found'},
        '未找到样式文件': {'English': 'Style File Not Found'},
        '输入匹配名称': {'English': 'Enter a Match Name'},
        '名称:': {'English': 'Name:'},
        '文件': {'English': 'File'},
        '打开目录': {'English': 'Open Project'},
        '设置': {'English': 'Settings'},
        '关闭项目': {'English': 'Close Project'},
        '保存': {'English': 'Save'},
        '工具': {'English': 'Tool'},
        '工具列表': {'English': 'Tool List'},
        '添加工具': {'English': 'Add Tool'},
        '删除工具': {'English': 'Delete Tool'},
        '刷新工具': {'English': 'Refresh Tool'},
        '帮助': {'English': 'Help'},
        '帮助文档': {'English': 'Help Document'},
        '工具官网': {'English': 'Tool Official Website'},
        '删除': {'English': 'Delete'},
        '文件夹读取成功': {'English': 'Folder read successfully'},
        '插件异常': {'English': 'Plug-in Exception'},
        '插件操作': {'English': 'Plug-in Operation'},
        '读取插件完成': {'English': 'Read plug-in Complete'},
        '读取安装完成': {'English': 'Read installation complete'},
        '读取安装失败': {'English': 'Read installation failure'},
        '插件读取失败': {'English': 'Plug-in Read Failure'},
        '选择文件夹': {'English': 'Select Folder'},
        '选择文件': {'English': 'Select File'},
        '关闭': {'English': 'Close'},
        '最大化': {'English': 'Maximize'},
        '最小化': {'English': 'Minimize'},
        '搜索': {'English': 'Search'},
        '协同': {'English': 'Coordination'},
        '主菜单': {'English': 'Main Menu'},
        '项目': {'English': 'Project'},
        '信息': {'English': 'Info Message'},
        '工具栏': {'English': 'Tool Bar'},
        '刷新': {'English': 'Refresh'},
        '重启': {'English': 'Restart'},
        '修改': {'English': 'edit'},
        '重启成功': {'English': 'Restart Successfully'},
        '语言切换成功': {'English': 'Language Switch Successful'},
        '最近项目': {'English': 'Recent Project'},
        '输入名称': {'English': 'Enter Name'},
        '打开项目': {'English': 'Open Project'},
        '是否打开此项目': {'English': 'Whether to open this item'},
        '项目已关闭': {'English': 'Project Closed'},
        '是否打开上次的项目': {'English': 'Whether to open the last project'},
        '文件夹不存在': {'English': 'Folder does not exist'},
        '打开': {'English': 'Open'},
        '取消': {'English': 'cancel'},
        '数量': {'English': 'Number'},
        '授权失效,请重新授权': {'English': 'Authorization expired, please re-authorize'},
        '打开成功': {'English': 'Open Successfully'},
        '删除成功': {'English': 'Successfully Deleted'},
        '上一个打开任务尚未完成': {'English': 'The previous open task has not been completed'},
        '没有权限': {'English': 'Have no authority'},
        '模式': {'English': 'Mode'},
        '当前模式不支持': {'English': 'The current mode is not supported'},
        '标尺未开启': {'English': 'Ruler is not opened'},
        '不能打开相同文件': {'English': 'Cannot open the same file'},
        '当前插件不支持此文件': {'English': 'The current plug-in does not support this file'},
        '保存成功': {'English': 'Save successfully'},
        '确定': {'English': 'OK'},
        '上移图层': {'English': 'Move up layer'},
        '下移图层': {'English': 'Scroll down layer'},
        '当前图形不支持涂抹': {'English': 'The current graphic does not support smearing'},
        '当前模式未支持或未选中轮廓': {'English': 'Contours are not supported or not selected in the current mode'},
        '尝试打开的数据语言与当前工具语言不匹配': {
            'English': 'The data language you are trying to open does not match the current tool language'},
        '打开于资源管理器': {'English': 'Open in explorer'},
        '复制文件路径': {'English': 'Copy file path'},
    }

    @property
    def getLanguage(self):
        """
        获取当前语言
        :return:
        """
        return self.__language

    def setLanguage(self, language: str):
        """
        设置语言
        :param language:
        :return:
        """
        self.__language = language

    def get_tr(self, text: str) -> str:
        """
        获取翻译
        :param text:
        :return:
        """
        if self.__language == '中文':
            return text
        return self.__translate_dict[text][self.__language]

    def add_tr(self, language_options: dict):
        """
        添加翻译
        :param language_options: {'文件操作': {'English': 'File Operation'}}
        :return:
        """
        self.__translate_dict.update(language_options)
