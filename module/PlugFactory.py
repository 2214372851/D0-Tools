#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/19 09:08
# @Author  : yinhai
# @File    : PlugFactory.py
# @Project : V0.0.1-alpha
from pathlib import Path
from abc import ABCMeta, abstractmethod


class PlugOption:
    def __init__(self, cn_name: str, en_name: str, cn_info: str, en_info: str, version: str, en_plug_type: str,
                 cn_plug_type: str, import_path: str, expiration_date: int, auto_dir: bool,
                 sidebar: bool, image_options: list, canvas_options: dict):
        """
        插件配置
        :param cn_name: 中文名称
        :param en_name: 英文名称
        :param cn_info: 中文提示
        :param en_info: 英文提示
        :param version: 版本号
        :param cn_plug_type:   中文插件类型
        :param en_plug_type:   英文插件类型
        :param show_file_type:  支持文件类型
        :param import_path: 导入名称
        :param expiration_date: 过期时间
        :param canvas_options: 插件内部配置项
        """
        self.cn_name = cn_name
        self.en_name = en_name
        self.cn_info = cn_info
        self.en_info = en_info
        self.version = version
        self.cn_plug_type = cn_plug_type
        self.en_plug_type = en_plug_type
        self.show_file_type = canvas_options['show_file_type']
        self.import_path = import_path
        self.expiration_date = expiration_date
        self.auto_dir = auto_dir
        self.sidebar = sidebar
        self.image_options = image_options
        self.canvas_options = canvas_options

    def toOption(self):
        """
        转换为插件option
        :return:
        """
        return {
            "中文_name": self.cn_plug_type,
            "English_name": self.en_plug_type,
            "module": {
                self.import_path: {
                    "中文_name": self.cn_name,
                    "English_name": self.en_name,
                    "中文_info": self.cn_info,
                    "English_info": self.en_info,
                    "version": self.version
                }
            }
        }
