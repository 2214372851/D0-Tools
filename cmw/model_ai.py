#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/3 14:11
# @Author  : yinhai
# @File    : model_ai.py
# @Project : V0.0.1-alpha
from pathlib import Path

import numpy
from PySide6.QtCore import QPointF
from ultralytics import YOLO
from ultralytics.models.sam import Predictor as SAMPredictor

from utils.yun_type import YunType


class UltralyticsYOLO(metaclass=YunType):
    model = None
    yolo = None

    def setModel(self, model_path: str):
        self.model = model_path
        self.yolo = YOLO(model_path)

    def getRect(self, filename: Path, labels: set[str]) -> list[numpy.array]:
        if not self.model: return []
        result = self.yolo(source=filename)
        model_label = result[0].names
        cls_label = result[0].boxes.cls.cpu().numpy()
        boxes = result[0].boxes.xyxy.cpu().numpy()
        return [boxes[i] for i in range(len(boxes)) if model_label[cls_label[i]] in labels]

    def getMask(self, filename: Path, labels: set[str]) -> list[numpy.array]:
        result = self.yolo(source=filename)
        model_label = result[0].names
        masks = result[0].masks.xy
        cls_label = result[0].boxes.cls.cpu().numpy()

        return [masks[i] for i in range(len(masks)) if model_label[cls_label[i]] in labels]


class UltralyticsSAM(metaclass=YunType):
    model = None
    overrides = dict(conf=0.25, task='segment', mode='predict', model="mobile_sam.pt")
    predictor = SAMPredictor(overrides=overrides)
    prompt_point = []
    filename = None

    def setImage(self, filename):
        self.filename = filename
        self.predictor.set_image(filename)

    def addPoint(self, point: QPointF, mode):
        self.prompt_point.append([point.x(), point.y(), mode])

    def getPoly(self):
        results = self.predictor(points=[i[:2] for i in self.prompt_point], labels=[i[-1] for i in self.prompt_point])
        result = results[0]
        return [QPointF(*p)for p in result.masks.xy[0].tolist()]
