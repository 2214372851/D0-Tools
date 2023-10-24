#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/19 16:19
# @Author  : yinhai
# @File    : data_proxy.py
# @Project : V0.0.1-alpha
import json
from threading import RLock
from PySide6 import QtWidgets, QtCore, QtGui
from cmw.model_data import Store
from cmw.model_selected import Selected
from utils.yun_type import YunType


class DataStateManage(metaclass=YunType):
    """
    数据状态管理器
    """
    single_lock = RLock()
    selected = None
    store = None
    data_list_widget = None
    cache_item: None | QtWidgets.QListWidgetItem = None

    @QtCore.Slot()
    def storeAlter(self):
        """
        store数据改变时，刷新数据列表
        :return:
        """
        if self.data_list_widget is None: return
        self.data_list_widget.clear()
        self.data_list_widget.itemClicked.connect(self.listItemClick)
        for index, item in enumerate(self.store.readData()):
            listItem = QtWidgets.QListWidgetItem()
            if item['mode'] == 'rect':
                listItem.setIcon(QtGui.QIcon('icons:选中焦点_selected-focus.svg'))
            elif item['mode'] == 'poly':
                listItem.setIcon(QtGui.QIcon('icons:八边形_octagon.svg'))
            elif item['mode'] == 'line':
                listItem.setIcon(QtGui.QIcon('icons:两点连接_connection-point-two.svg'))
            elif item['mode'] == 'point':
                listItem.setIcon(QtGui.QIcon('icons:点_dot.svg'))

            listItem.setData(QtCore.Qt.ItemDataRole.UserRole, index)
            info = '\n'.join([f'{k}:{v}' for k, v in item['options'].items()])
            listItem.setText(info.replace('\n', ''))
            listItem.setToolTip(info)
            self.data_list_widget.addItem(listItem)
        self.cache_item = None
        pass

    def listItemClick(self, item: QtWidgets.QListWidgetItem):
        """
        列表项点击时，刷新选中状态
        :param item:
        :return:
        """
        if self.selected is None: return
        index = item.data(QtCore.Qt.ItemDataRole.UserRole)
        self.selected.setSelect(int(index))

    @QtCore.Slot()
    def selectedAlter(self):
        """
        选择状态改变时，刷新数据列表
        :return:
        """
        if self.data_list_widget is None: return
        if self.cache_item is not None:
            self.cache_item.setBackground(QtGui.QColor(0, 0, 0, 0))
        item = self.data_list_widget.item(self.selected.polyIndex)
        item.setBackground(QtGui.QColor(240, 69, 74))
        self.cache_item = item
        pass

    def setListWidget(self, list_widget: QtWidgets.QListWidget):
        """
        设置数据列表组件
        :param list_widget:
        :return:
        """
        self.data_list_widget = list_widget
        return self

    def setSelected(self, selected: Selected):
        """
        设置选择状态器
        :param selected:
        :return:
        """
        self.selected = selected
        self.selected.setSignal(self.selectedAlter)
        return self

    def setStore(self, store: Store):
        """
        设置数据存储器
        :param store:
        :return:
        """
        self.store = store
        self.store.setSignal(self.storeAlter)
        return self
