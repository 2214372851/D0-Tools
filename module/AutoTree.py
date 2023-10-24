#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/18 11:18
# @Author  : yinhai
# @File    : AutoTree.py
# @Project : AUTO_UI
from threading import Thread

from PySide6 import QtGui, QtWidgets, QtCore
from pathlib import Path
from manage import HaiProMax


class Tree(QtWidgets.QTreeWidget):

    def __init__(self, main_ui: HaiProMax):
        """
        初始化树状控件
        :param main_ui:
        """
        super().__init__()
        self.main_ui = main_ui
        self.setStyleSheet(u"* {\n"
                           "    color: #fff;\n"
                           "}\n"
                           "#dir_tree {\n"
                           "    background-color: rgba(30, 30, 30, 0);\n"
                           "    border: none;\n"
                           "}\n"
                           "QTreeWidget {\n"
                           "    outline: none;\n"
                           "}\n"
                           "QTreeWidget::item:selected {\n"
                           "    color: #fff;\n"
                           "    border-radius: 4px;\n"
                           "    background-color: rgba(46, 67, 110, 1);\n"
                           "}\n"
                           "QTreeWidget::item {\n"
                           "    border: none;\n"
                           "    height: 20px;\n"
                           "    show-decoration-selected: 1;\n"
                           "}\n"
                           "QScrollBar:horizontal {\n"
                           "    height:8px;\n"
                           "    background:rgba(0,0,0,0%);\n"
                           "    margin:0px,0px,0px,0px;\n"
                           "    border-radius:4px;\n"
                           "}\n"
                           "QScrollBar:vertical {\n"
                           "    width:8px;\n"
                           "    background:rgba(0,0,0,0%);\n"
                           "    margin:0px,0px,0px,0px;\n"
                           "    border-radius:4px;\n"
                           "}\n"
                           "QScrollBar::handle:horizontal {\n"
                           "    height:8px;\n"
                           "    background:rgba(255, 255, 255, 0.17);\n"
                           "    border-radius:4px;   \n"
                           "    min-width:20;\n"
                           "}\n"
                           "QScrollBar::handle:vertical {\n"
                           "    width:8px;\n"
                           "    background:rgba(255, 255, 255, 0.17);\n"
                           "    border-radius:4px;   \n"
                           "    min-height:20;\n"
                           ""
                           "}\n"
                           "QScrollBar::handle:horizontal:hover,\n"
                           "QScrollBar::handle:vertical:hover {\n"
                           "    background:rgba(255, 255, 255, 0.3);\n"
                           "}\n"
                           "QScrollBar::sub-page:horizontal,\n"
                           "QScrollBar::add-page:horizontal,\n"
                           "QScrollBar::sub-line:horizontal, \n"
                           "QScrollBar::add-line:horizontal,\n"
                           "QScrollBar::sub-page:vertical,\n"
                           "QScrollBar::add-page:vertical,\n"
                           "QScrollBar::sub-line:vertical, \n"
                           "QScrollBar::add-line:vertical {\n"
                           "    background: rgba(255, 0, 0, 0);\n"
                           "}")
        self.initTreeItem()
        self.setMouseTracking(True)
        self.setAutoFillBackground(False)
        self.setRootIsDecorated(True)
        self.setItemsExpandable(True)
        self.setHeaderHidden(True)
        self.header().setCascadingSectionResizes(False)
        self.header().setHighlightSections(False)
        self.header().setStretchLastSection(True)
        self.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.treeMenus)

    def initTreeItem(self):
        """
        初始化树节点
        :return:
        """
        pass

    def treeMenus(self, pos: QtCore.QPoint) -> None:
        """
        文件菜单的右键菜单
        :param pos:
        :return:
        """
        pass
