#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/16 17:51
# @Author  : yinhai
# @File    : model_data.py
# @Project : 全新UI_canvas
import copy
from utils import tools
from PIL import Image
from pathlib import Path
import pickle
import collections
from PySide6 import QtCore
from threading import Thread


class Store:
    """
    数据存储器
    """
    filename = None
    width = None
    height = None
    versions = None
    language = None
    __DATA: list = []
    __data_suffix = ''
    cache_data = None
    image_entirety: dict = {}
    signal = None
    # widget_toast = tools.WidgetMessage()

    def __init__(self, filename: Path, version: str, language: str, cache_count: int = 6, suffix: str = '.yunhai'):
        """
        输出存储器
        :param filename:
        :param version:
        :param language:
        :param cache_count:
        :param suffix:
        """
        self.language = language
        self.__rollback_stark = collections.deque(maxlen=cache_count)
        self.__advance_stark = collections.deque(maxlen=cache_count)
        self.__data_suffix = suffix
        self.readImage(filename, version)

    def addData(self, data: dict):
        """
        添加数据
        :param data: dict
        :return:
        """
        stark_data = copy.copy(self.__DATA)
        self.__rollback_stark.append(stark_data)
        self.__DATA.append(data)
        self.saveData()
        self.monitor()

    def delData(self, index: int, child_index: int | None = None):
        """
        删除数据
        :param index: 轮廓ID
        :param child_index: 点ID
        :return:
        """
        stark_data = copy.copy(self.__DATA)
        self.__rollback_stark.append(stark_data)
        if child_index is None:
            del self.__DATA[index]
        else:
            del self.__DATA[index]['data'][child_index]
        self.saveData()
        self.monitor()

    def readData(self, index: int | None = None):
        """
        读取数据
        :param index: 轮廓ID
        :return:
        """
        if index is None:
            return self.__DATA
        else:
            return self.__DATA[index]

    def editData(self, index: int, data: list, attribute: str = 'data',
                 child_index: int | None = None, is_roll: bool = True):
        """
        修改数据
        :param index: 轮廓ID
        :param data: 新数据
        :param attribute: 修改的属性
        :param child_index: 点ID
        :param is_roll: 是否设置上一步缓存
        :return:
        """
        if is_roll:
            self.__rollback_stark.append(copy.deepcopy(self.__DATA))
        if child_index is None:
            self.__DATA[index][attribute] = data
        else:
            self.__DATA[index][attribute][child_index] = data

    def rollback(self):
        """
        上一步
        :return:
        """
        if not self.__rollback_stark: return
        self.__advance_stark.append(copy.copy(self.__DATA))
        self.__DATA = self.__rollback_stark.pop()
        self.monitor()

    def advance(self):
        """
        下一步
        :return:
        """
        if not self.__advance_stark: return
        self.__rollback_stark.append(copy.copy(self.__DATA))
        self.__DATA = self.__advance_stark.pop()
        self.monitor()

    def addRollback(self):
        """
        添加上一步缓存
        :return:
        """
        stark_data = copy.deepcopy(self.__DATA)
        self.__rollback_stark.append(stark_data)

    def readImage(self, filename: Path, version):
        """
        读取图片信息
        :param filename:
        :param version:
        :return:
        """
        if not filename.exists(): raise FileExistsError('文件不存在' + filename.__str__())
        with Image.open(filename) as img:
            self.filename = filename.__str__()
            self.width = img.width
            self.height = img.height
            self.versions = version

    def readFileData(self, filename: Path):
        """
        读取图片对应标注信息
        :param filename:
        :return:
        """
        data_filename = Path(str(filename) + self.__data_suffix)
        if data_filename.exists():
            with data_filename.open('rb') as fd:
                data = pickle.load(fd)
                if (data_language := data['language']) != self.language:
                    raise ValueError(f'尝试打开的数据语言为{data_language}与当前工具语言{self.language}不匹配')
                self.__DATA = data['data']
                self.image_entirety = data['image_entirety']
                self.monitor()

    def setImageEntirety(self, data: dict):
        """
        设置图片整体信息
        :param data:
        :return:
        """
        if data == self.image_entirety: return
        self.image_entirety = data
        self.saveData()

    def monitor(self):
        """
        监控数据变化
        :return:
        """
        if self.signal is None: return
        self.signal()

    @QtCore.Slot()
    def saveData(self) -> None:
        """
        保存数据
        :return:
        """
        if not self.filename: return

        def save():
            save_data = {
                'filename': self.filename,
                'width': self.width,
                'height': self.height,
                'versions': self.versions,
                'image_entirety': self.image_entirety,
                'data': self.__DATA,
                'language': self.language
            }
            if save_data == self.cache_data: return
            self.cache_data = copy.deepcopy(save_data)
            with open('{}{}'.format(self.filename, self.__data_suffix), 'wb') as f:
                f.write(pickle.dumps(save_data))

        Thread(target=save, daemon=True).start()
        pass

    def setSignal(self, signal):
        """
        设置信号
        :param signal:
        :return:
        """
        self.signal = signal

    def __str__(self):
        return self.filename
