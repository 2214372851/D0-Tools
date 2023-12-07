#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/16 17:51
# @Author  : yinhai
# @File    : model_data.py
# @Project : 全新UI_canvas
import collections
import copy
import pickle
from pathlib import Path
from threading import Thread

from PySide6 import QtCore, QtGui, QtWidgets

from utils import tools
from utils.translate import Translate


class Store:
    """
    数据存储器
    """

    def __init__(self, filename: Path, filedata: QtGui.QPixmap, entirety, version: str, language: str,
                 cache_count: int = 6, suffix: str = '.d0'):
        """
        输出存储器
        :param filename:
        :param filedata:
        :param entirety:
        :param version:
        :param language:
        :param cache_count:
        :param suffix:
        """
        self.filename = None
        self.width = None
        self.height = None
        self.versions = None
        self.language = None
        self.entirety = entirety
        self.__DATA: list = []
        self.__data_suffix = ''
        self.image_entirety: dict = {}
        self.signal = None
        self.widget_toast = tools.WidgetMessage()
        self.timing = QtCore.QTimer()
        self.language = language
        self.__rollback_stark = collections.deque(maxlen=cache_count)
        self.__advance_stark = collections.deque(maxlen=cache_count)
        self.__data_suffix = suffix
        self.filedata = filedata
        self.readImage(filename, version)
        self.__updateEntirety()

    def addData(self, data: dict):
        """
        添加数据
        :param data: dict
        :return:
        """
        stark_data = copy.copy(self.__DATA)
        self.__rollback_stark.append(stark_data)
        self.__DATA.append(data)
        self.monitor()

    def delData(self, index: int, child_index: int | None = None):
        """
        删除数据
        :param index: 轮廓ID
        :param child_index: 点ID
        :return:
        """
        stark_data = copy.deepcopy(self.__DATA)
        self.__rollback_stark.append(stark_data)
        if child_index is None:
            del self.__DATA[index]
        else:
            del self.__DATA[index]['data'][child_index]
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

    def editAll(self, data):
        self.__DATA = data
        self.monitor()

    def editData(self, index: int, data: list | tuple, attribute: str = 'data',
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
        self.monitor()

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
        print('addRoll')
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
        self.filename = filename.__str__()
        self.width = self.filedata.width()
        self.height = self.filedata.height()
        self.versions = version
        self.monitor()
        self.readFileData(filename)

    def readFileData(self, filename: Path):
        """
        读取图片对应标注信息
        :param filename:
        :return:
        """
        data_filename = filename.parent / (filename.stem + self.__data_suffix)
        if not data_filename.exists():
            self.monitor()
            return
        with data_filename.open('rb') as fd:
            data = pickle.loads(fd.read())
            if data['language'] != self.language:
                self.widget_toast.showError(Translate().get_tr(f'尝试打开的数据语言与当前工具语言不匹配'))

            self.__DATA = data['data']
            self.image_entirety = data['image_entirety']
            self.__updateEntirety()
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

    def __updateEntirety(self):
        """
        刷新图片整体属性
        :return:
        """
        if not self.entirety: return
        if not self.image_entirety:
            self.image_entirety = {k: v['option'][0] for k, v in self.entirety.items()}

        for name, value in self.image_entirety.items():
            widget = self.entirety[name]['widget']
            option = self.entirety[name]['option']
            if isinstance(widget, QtWidgets.QComboBox):
                widget.setCurrentIndex(option.index(value))
            else:
                widget: QtWidgets.QPushButton
                widget.setChecked(bool(option.index(value)))

    def movingLayer(self, mode: str, index: int):
        """
        移动标注层
        :param mode: +上移|-下移
        :param index: 索引
        :return:
        """
        data = self.__DATA.pop(index)
        if index > 0 and mode == '-':
            self.__DATA.insert(index - 1, data)
        elif index < len(self.__DATA) and mode == '+':
            self.__DATA.insert(index + 1, data)
        else:
            self.__DATA.insert(index, data)
        self.monitor()

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
        save_data = {
            'filename': self.filename,
            'width': self.width,
            'height': self.height,
            'versions': self.versions,
            'image_entirety': self.image_entirety,
            'data': self.__DATA,
            'language': self.language
        }
        filename = Path(self.filename)

        def save():
            with open(filename.parent / (filename.stem + self.__data_suffix), 'wb') as f:
                f.write(pickle.dumps(save_data))

        Thread(target=save, daemon=True).start()
        self.widget_toast.showSucceed(Translate().get_tr('保存成功'))
        pass

    def setSignal(self, signal):
        """
        设置信号
        :param signal:
        :return:
        """
        self.signal = signal
        self.monitor()

    def __str__(self):
        return self.filename

    def __len__(self):
        return len(self.__DATA)

    def __del__(self):
        self.saveData()
