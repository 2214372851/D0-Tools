#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/18 10:46
# @Author  : yinhai
# @File    : path_temp.py
# @Project : AUTO_UI
from pathlib import Path


class CachePath:
    def __init__(self):
        self.cache_file = Path('temp/cache_path.txt')
        self.cache_list = list()
        self.__readCache()

    def __readCache(self):
        """
        读取缓存
        :return:
        """
        Path('temp').mkdir(parents=True, exist_ok=True)
        if not self.cache_file.exists(): return
        with self.cache_file.open('r', encoding='utf-8') as f:
            self.cache_list = [path.replace('\n', '') for path in f.readlines()]

    def addCache(self, path: str):
        """
        添加缓存路径
        :param path:
        :return:
        """
        path = path
        if path in self.cache_list:
            del self.cache_list[self.cache_list.index(path)]

        self.cache_list.append(path)
        if len(self.cache_list) > 10:
            self.cache_list.pop(0)
        self.saveCache()

    def saveCache(self):
        """
        保存缓存
        :return:
        """
        with self.cache_file.open('w', encoding='utf-8') as f:
            f.writelines('\n'.join(self.cache_list))

    def getCache(self):
        """
        获取缓存路径
        :return:
        """
        if self.cache_list:
            return self.cache_list[-1]
        else:
            return Path.home().joinpath('Desktop').__str__()


