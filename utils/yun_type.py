#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/21 13:15
# @Author  : yinhai
# @File    : yun_type.py
# @Project : V0.0.1-alpha
class YunType(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = cls.__new__(cls)
        cls.__init__(cls.instance, *args, **kwargs)
        return cls.instance
