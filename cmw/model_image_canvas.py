import math
import pickle
from abc import ABCMeta, abstractmethod
from typing import List
from pathlib import Path
from PySide6 import QtWidgets, QtGui, QtCore
from PIL import ImageQt, Image
from cmw.model_data import Store
from cmw.model_plug import DrawPlug
from cmw.model_style import Style
from cmw.model_tools import SelectDialog
from geomdl import fitting
from cmw.model_selected import Selected
from utils import tools, data_proxy


# TODO： 图像打整体属性
# TODO： 标注缓存 》 Ctrl + Z 上一步
class Canvas(QtWidgets.QWidget):
    """
    图像标注基类
    功能：图像显示、缩放、移动
    """
    __metaclass__ = ABCMeta
    tool_cn_type = '标注工具'
    tool_cn_info = '通用标注工具'
    tool_en_type = 'Tagging tool'
    tool_en_info = 'Universal annotation tool'
    expiration_date = 1704042061
    sidebar = True

    def __init__(self,
                 options: dict, version: str, draw_rect_min_size: tuple,
                 draw_poly_min_size: int, draw_point_num: int, show_file_type: list,
                 encipher: bool = False, language: str = 'en'):
        """
        画布初始化
        :param options: 项目配置
        :param version: 工具版本号
        :param encipher: 是否加密
        :param language: 语言 cn|en
        """
        super().__init__()

        # 工具配置
        """
        调节矩形最小值
        调节轮廓最小面积
        是否显示标尺
        标尺颜色
        标尺样式
        是否填充图像内部
        是否绘制多边形的点
        画笔透明度调节
        缩放调节
        点的大小调节
        绘制模式的改变
        """
        self.options = options
        # 画布语言
        self.language = language
        self.label_key = '标签' if language == 'cn' else self.options['标签'][f'{language}_name']
        # 选择标签弹窗
        self.selectDialog = SelectDialog(self)
        # 绘制的矩形最小宽高
        self.draw_rect_min_size = draw_rect_min_size
        # 绘制轮廓最小面积
        self.draw_poly_min_size = draw_poly_min_size
        # 点模式最多点(到达最多数时自动停止本次标注)
        self.draw_point_num = draw_point_num
        # 是否启用绘图标尺
        self.isScaleplate = False
        # 标尺颜色
        self.scaleplate_color = QtCore.Qt.GlobalColor.red
        # 标尺样式 SolidLine|DashLine
        self.scaleplate_style = QtCore.Qt.PenStyle.DotLine
        # 启用拖拽事件
        self.setAcceptDrops(True)
        # 启用鼠标移动事件
        self.setMouseTracking(True)
        # 设置工具版本
        self.version = version
        # 是否启用加密
        self.encipher: bool = encipher
        # 模式类型
        self.mode_type: str = 'normal'
        # 工具支持的文件类型
        self.showFileType = show_file_type
        # 是否填充图形内部
        self.isFill: dict = {
            'default': False
        }
        # 是否实例分割
        self.isInstance = '实例' in self.options
        # 是否正在移动多边形
        self.isMovePloy = False
        # 是否已保存
        self.isSave = True
        # 是否正在绘制
        self.isDraw: bool = False
        # 是否绘制多边形的点
        self.isDrawPolyPoint: bool = False
        # 画笔透明的
        self.opacity = .5
        # 数据存储器
        self.draw_store: Store | None = None
        # 样式存储器
        self.draw_style: Style = Style(options=self.options, language=language)
        # 当前打开的文件路径
        self.openfile: Path | None = None
        # 当前缩放比
        self.zoom: float = 0
        # 是否重置缩放比
        self.img_reset: bool = False
        # 图片显示基准点
        self.image_standard: QtCore.QPoint = QtCore.QPoint(0, 0)
        # 是否加速操作（按下Shift）
        self.speed_up: bool = False
        # 是否按下Ctrl
        self.isCtrl: bool = False
        # 是否移动图片位置
        self.is_move: bool = False
        # 鼠标左键点击
        self.left_mouse_click: bool = False
        # 鼠标左键点击位置
        self.left_mouse_click_pos: None | QtCore.QPointF = None
        # 鼠标右键点击
        self.right_mouse_click: bool = False
        # 鼠标右键点击位置
        self.right_mouse_click_pos: None | QtCore.QPointF = None
        # 当前显示的文件的QPixmap对象
        self.show_file_data: None | QtGui.QPixmap = None
        # 绘制中的数据暂存
        self.temp_data: List[QtCore.QPointF] = []
        # 显示点的大小
        self.point_size: int = 3
        # 当前绘制模式(rect|poly|line|point|None),当值为None时不具备标注功能
        self._draw_mode = None
        # 预设模式
        self._preinstall_modes = {'rect', 'poly', 'line', 'point', None}
        # 当前选中 [轮廓index, 点, 边标识]
        self.selected = Selected(self)
        # 鼠标位置
        self.mouse_pos: QtCore.QPointF = QtCore.QPointF()
        # 自动保存定时器
        self.timing_save = QtCore.QTimer(self)
        # 绘制插件管理
        self.drawPlug = DrawPlug()
        # 窗口消息
        self.widget_toast = tools.WidgetMessage()
        # 数据连通管理
        self.dataManage = data_proxy.DataStateManage().setSelected(self.selected)

    def initMenus(self):
        """
        初始化主UI的菜单
        :return:
        """
        # TODO: 这里的需要向主UI映射菜单
        # 绘画模式
        self._draw_mode = None
        # 绘画点大小
        self.point_size: int = 3
        # 透明度
        self.opacity = 1.0
        # 是否绘制多边形的点
        self.isDrawPolyPoint: bool = False
        # 是否填充图形内部
        self.isFill: bool = False
        # 是否实例分割
        self.isInstance = True
        # 标尺样式 SolidLine|DashLine
        self.scaleplate_style = QtCore.Qt.PenStyle.DotLine
        # 标尺颜色
        self.scaleplate_color = QtCore.Qt.GlobalColor.red
        # 是否启用绘图标尺
        self.isScaleplate = True

    def selectMode(self, mode_name: str | None):
        """
        切换绘画类型
        :param mode_name: 模式 point|rect|poly|line
        :return:
        """
        self.widget_toast.showSucceed(f'{mode_name} mode')
        self._draw_mode = mode_name
        self.mode_type = 'normal'
        if mode_name not in self._preinstall_modes:
            mode = self.drawPlug.getMode(mode_name)
            if mode_name in self.isFill: return
            self.isFill[mode_name] = mode.is_fill

    def getShowButton(self) -> list:
        """
        主UI工具栏按钮渲染
        :return:
        """

        @QtCore.Slot()
        def switchoverScaleplate():
            self.isScaleplate = not self.isScaleplate

        @QtCore.Slot()
        def switchoverFill():
            self.isFill['default'] = not self.isFill['default']
            self.update()

        @QtCore.Slot()
        def switchoverDrawPolyPoint():
            self.isDrawPolyPoint = not self.isDrawPolyPoint
            self.update()

        return [
            {
                'function': switchoverScaleplate,
                'icon': 'icons:网格3_grid-three.svg',
                'menu_id': 9,
                'tip': {'显示标尺': {'English': 'Display scale'}}
            },
            {
                'function': self.switchScaleplateStyle,
                'icon': 'icons:切换轨道_switch-track.svg',
                'menu_id': 9,
                'tip': {'切换标尺样式': {'English': 'Toggle ruler style'}}
            },
            {
                'function': switchoverFill,
                'icon': 'icons:填充_fill.svg',
                'menu_id': 9,
                'tip': {'是否填充': {'English': 'Fill or not'}}
            },
            {
                'function': switchoverDrawPolyPoint,
                'icon': 'icons:圆圈_circle-four-line.svg',
                'menu_id': 9,
                'tip': {'绘制多边形的点': {'English': 'Draw the points of the polygon'}}
            },
            {
                'function': lambda: self.__setOpacity('+'),
                'icon': 'icons:加_plus.svg',
                'menu_id': 9,
                'tip': {'透明度的增加': {'English': '透明度的增加'}}
            },
            {
                'function': lambda: self.__setOpacity('-'),
                'icon': 'icons:减_minus.svg',
                'menu_id': 9,
                'tip': {'透明度的减少': {'English': '透明度的减少'}}
            },
            {
                'function': lambda: self._editLineWidth('+'),
                'icon': 'icons:添加_add-one.svg',
                'menu_id': 9,
                'tip': {'增加线宽': {'English': '增加线宽'}}
            },
            {
                'function': lambda: self._editLineWidth('-'),
                'icon': 'icons:减少_reduce-one.svg',
                'menu_id': 9,
                'tip': {'减少线宽': {'English': '减少线宽'}}
            },
            {
                'function': self.__adaptZoom,
                'icon': 'icons:坐标系统_coordinate-system.svg',
                'menu_id': 9,
                'tip': {'自适应缩放': {'English': '自适应缩放'}}
            },
            {
                'function': lambda: self.widget_toast.showError('1阿萨大{}'.format(self.widget_toast.STACK.__len__())),
                'icon': 'icons:坐标系统_coordinate-system.svg',
                'menu_id': 9,
                'tip': {'自适应缩放': {'English': '自适应缩放'}}
            },
        ]

    def clearState(self):
        """
        清除状态
        :return:
        """
        self.draw_store = None
        self.openfile: Path | None = None
        self.zoom: float = 0
        self.img_reset: bool = False
        self.image_standard: QtCore.QPoint = QtCore.QPoint(0, 0)
        self.speed_up: bool = False
        self.is_move: bool = False
        self.isSave = True
        self.left_mouse_click: bool = False
        self.left_mouse_click_pos: None | QtCore.QPointF = None
        self.right_mouse_click: bool = False
        self.right_mouse_click_pos: None | QtCore.QPointF = None
        self.show_file_data: None | QtGui.QPixmap = None
        self.temp_data: List[QtCore.QPointF] = []

    def __showFile(self, brush: QtGui.QPainter) -> None:
        """
        显示文件
        当前显示的文件为self.openfile
        :return:
        """
        if not self.openfile: return
        if not self.zoom or self.img_reset: self.__adaptZoom(True)
        s_x = int(self.show_file_data.width() / self.zoom)
        s_y = int(self.show_file_data.height() / self.zoom)
        rect = QtCore.QRect(self.image_standard.x(), self.image_standard.y(), s_x, s_y)
        brush.drawPixmap(rect, self.show_file_data)
        pass

    def __adaptZoom(self, auto=False):
        """
        根据窗口大小自适应缩放
        :param auto: 是否是自动适应
        :return:
        """
        if self.height() <= (self.width() * self.show_file_data.height()) / self.show_file_data.width():
            self.zoom = self.show_file_data.height() / self.height()
        else:
            self.zoom = self.show_file_data.width() / self.width()
        self.image_standard = QtCore.QPoint(
            int((self.width() - (self.show_file_data.width() / self.zoom)) / 2),
            int((self.height() - (self.show_file_data.height() / self.zoom)) / 2)
        )
        if not auto:
            self.update()

    def showScaleplate(self, brush: QtGui.QPainter):
        """
        显示标尺
        :param brush: 画笔
        :return:
        """
        if not self.isScaleplate: return
        if self.mouse_pos == QtCore.QPointF(0, 0) or self.is_move or not self._draw_mode: return
        normal_mouse_pos = self.showPoint(self.mouse_pos)
        pen = QtGui.QPen(self.scaleplate_color, 1, self.scaleplate_style)
        brush.setPen(pen)
        brush.drawLine(QtCore.QLineF(0, normal_mouse_pos.y(), self.width(), normal_mouse_pos.y()))
        brush.drawLine(QtCore.QLineF(normal_mouse_pos.x(), 0, normal_mouse_pos.x(), self.height()))

    def switchScaleplateStyle(self) -> None:
        """
        切换标尺样式
        :return:
        """
        if not self.isScaleplate:
            self.widget_toast.showInfo('标尺未开启')
            return
        if self.scaleplate_style == QtCore.Qt.PenStyle.DashLine:
            self.scaleplate_style = QtCore.Qt.PenStyle.SolidLine
        else:
            self.scaleplate_style = QtCore.Qt.PenStyle.DashLine

    def selectFile(self, filename: Path):
        """
        切换文件
        手动必须给self.openfile赋值,或super().selectFile(filename:Path)
        :return:
        """
        if self.openfile.__str__() == filename.__str__():
            self.widget_toast.showInfo('不能打开相同文件')
            return
        if filename.suffix not in self.showFileType:
            self.widget_toast.showError('当前插件不支持此文件')
            return
        self.timing_save.stop()
        self.clearState()
        self.openfile = filename
        self.draw_store = Store(filename=filename, version=self.version, language=self.language)
        self.dataManage.setStore(self.draw_store)
        self.draw_store.readFileData(filename)
        if self.encipher:
            self.show_file_data = self.__decode(self.openfile)
        else:
            with Image.open(self.openfile) as im:
                self.show_file_data = QtGui.QPixmap(ImageQt.ImageQt(im))
        self.timing_save.timeout.connect(self.draw_store.saveData)
        self.timing_save.start(3000)
        self.update()
        pass

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        """
        绘制事件
        :param event: 绘制事件
        :return:
        """
        brush = QtGui.QPainter()
        brush.begin(self)
        brush.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)
        self.__showFile(brush)
        brush.setOpacity(self.opacity)
        self._showData(brush)
        brush.setOpacity(1)
        self.showScaleplate(brush)
        brush.end()

    def wheelEvent(self, event) -> None:
        """
        鼠标滚轮事件
        :param event: 鼠标滚轮事件
        :return:
        """
        if not self.openfile: return
        angle = event.angleDelta() / 8
        angle_y = angle.y()
        exclude = (event.position() - self.image_standard) * self.zoom
        if angle_y > 0:
            pantograph_ratio = 0.7 if self.speed_up else 0.95
            if self.zoom * pantograph_ratio > 0.001:
                self.zoom *= pantograph_ratio
        else:
            pantograph_ratio = 1.3 if self.speed_up else 1.05
            if self.zoom * pantograph_ratio < 100:
                self.zoom *= pantograph_ratio
        self.image_standard = (event.position() - exclude / self.zoom).toPoint()

        self.update()

    def _editLineWidth(self, mode):
        """
        修改绘制线宽
        :param mode: +加粗|-减细|#恢复默认2
        :return:
        """
        if mode == "#":
            self.draw_style.lineWidth = 2
        elif mode == "+":
            if self.draw_style.lineWidth == 20: return
            self.draw_style.lineWidth += 5 if self.speed_up else 1
        else:
            if self.draw_style.lineWidth == 1: return
            self.draw_style.lineWidth -= 5 if self.speed_up else 1
        self.update()

    @QtCore.Slot()
    def __editPolyInfo(self):
        """
        修改选中轮廓属性
        :return:
        """
        if not self.selected.isSelect or not self._draw_mode: return
        old_options = self.draw_store.readData(self.selected.polyIndex)['options']
        option_data = self.selectDialog.setData(old_options).showSelect()
        if not option_data: return
        self.draw_store.editData(self.selected.polyIndex, attribute='options', data=option_data)

    def __setOpacity(self, mode):
        """
        设置透明度
        :param mode:
        :return:
        """
        if mode == "+":
            if self.opacity >= 1: return
            self.opacity += 0.1 if self.speed_up else 0.05
        else:
            if self.opacity <= 0: return
            self.opacity -= 0.1 if self.speed_up else 0.05
        self.update()

    def showPolyMenu(self):
        """
        轮廓的右键菜单
        :return:
        """
        if not self.selected.isSelect: return
        popMenu = QtWidgets.QMenu()
        itemMenu = popMenu.addAction("删除")
        itemMenu.triggered.connect(self.__delDataPosition)
        itemMenu = popMenu.addAction("修改")
        itemMenu.triggered.connect(self.__editPolyInfo)
        popMenu.exec(QtGui.QCursor.pos())
        popMenu.show()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        鼠标点击
        :param event: 鼠标点击事件
        :return:
        """
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.left_mouse_click_pos = event.position()
            self.left_mouse_click = True
            if self.is_move or not self.openfile: return
            save_pos = self.savePoint(event.position())
            if self.selected.isSelect and not self.speed_up: return
            if not self._draw_mode: return
            self.isDraw = True
            self.isSave = False
            if self._draw_mode == 'rect':
                self.temp_data = [save_pos, save_pos]
            else:
                self.temp_data.append(save_pos)
            self.mouseLeft(event)
        elif event.button() == QtCore.Qt.MouseButton.RightButton:
            self.right_mouse_click_pos = event.position()
            self.right_mouse_click = True
            if self.isDraw and self.temp_data:
                if self._draw_mode == 'rect':
                    self.temp_data.clear()
                else:
                    self.temp_data.pop()
                if not self.temp_data or self.speed_up:
                    self.temp_data.clear()
                    self.isDraw = False
                    self.isSave = True
                    print("清空temp——data")

            self.showPolyMenu()
            self.mouseRight(event)
        elif event.button() == QtCore.Qt.MouseButton.MiddleButton:
            self.drawStop()
        self.update()
        pass

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        鼠标移动
        :param event: 鼠标移动事件
        :return:
        """
        self.setFocus()
        if self.left_mouse_click and (self.is_move or not self._draw_mode):
            sx = self.left_mouse_click_pos - event.position()
            self.image_standard = QtCore.QPoint(self.image_standard.x() - sx.x(), self.image_standard.y() - sx.y())
            self.left_mouse_click_pos = event.position()
        self.mouse_pos = self.savePoint(event.position())
        if self.isDraw:
            self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
            if self._draw_mode == 'rect' and self.left_mouse_click:
                self.temp_data = [self.temp_data[0], self.mouse_pos]
        else:
            self.checkSelection(event)
            self.__moveDataPosition(event)
        self.mouseMove(event)
        self._showPolyTip(event)
        self.update()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        鼠标释放
        :param event: 鼠标释放事件
        :return:
        """
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.left_mouse_click = False
        elif event.button() == QtCore.Qt.MouseButton.RightButton:
            self.right_mouse_click = False
        self.mouseRelease(event)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        键盘按键按下
        :param event: 按键触发事件
        :return:
        """
        self.img_reset = False
        if event.key() == QtCore.Qt.Key.Key_Shift:
            # 组合上档键
            self.speed_up = True
        if event.key() == QtCore.Qt.Key.Key_Control:
            # 组合操作键
            self.isCtrl = True
        if event.key() == QtCore.Qt.Key.Key_Space:
            # 移动图片位置
            self.is_move = True
            self.setCursor(QtCore.Qt.CursorShape.OpenHandCursor)
        if event.key() == QtCore.Qt.Key.Key_Delete:
            # 删除图形
            self.__delDataPosition()
        if event.key() == QtCore.Qt.Key.Key_Q:
            # 增加透明度
            self.__setOpacity('+')
        if event.key() == QtCore.Qt.Key.Key_W:
            # 减小透明度
            self.__setOpacity('-')
        if event.key() == QtCore.Qt.Key.Key_E:
            # 修改轮廓属性
            self.__editPolyInfo()
        if event.key() == QtCore.Qt.Key.Key_A:
            # 增加线宽
            self._editLineWidth('+')
        if event.key() == QtCore.Qt.Key.Key_S:
            # 默认线宽
            self._editLineWidth('#')
        if event.key() == QtCore.Qt.Key.Key_D:
            # 减少线宽
            self._editLineWidth("-")
        if event.key() == QtCore.Qt.Key.Key_Z:
            if self.isCtrl and self.speed_up:
                # 操作前进
                self.draw_store.advance()
            elif self.isCtrl:
                # 操作回退
                self.draw_store.rollback()
            else:
                # 图片自适应大小
                self.__adaptZoom()
        self.keyPress(event)
        self.update()

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        键盘按键松开
        :param event: 按键释放事件
        :return:
        """
        if event.key() == QtCore.Qt.Key.Key_Shift:
            self.speed_up = False
        if event.key() == QtCore.Qt.Key.Key_Control:
            self.isCtrl = False
        if event.key() == QtCore.Qt.Key.Key_Space:
            self.is_move = False
        self.keyRelease(event)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        """
        拖拽事件
        :param event:
        :return:
        """
        event.accept()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        """
        拖拽释放事件
        :param event:
        :return:
        """
        drag_filename = Path(event.mimeData().text().replace('file:///', ''))
        self.selectFile(drag_filename)

    def savePoint(self, point: QtCore.QPointF) -> QtCore.QPointF:
        """
        点转换为保存格式(原图中点的位置)
        :param point: 点(QtCore.QPointF)
        :return:
        """
        return (point - self.image_standard) * self.zoom

    def showPoint(self, point: QtCore.QPointF) -> QtCore.QPointF:
        """
        点转换为绘制格式(画布中点的位置)
        :param point: 点(QtCore.QPointF)
        :return:
        """
        # noinspection PyTypeChecker
        return (point / self.zoom) + self.image_standard

    def _showPolyTip(self, event: QtGui.QMouseEvent):
        """
        显示轮廓信息
        :param event:
        :return:
        """
        if not self.selected.isSelect or self.isMovePloy:
            QtWidgets.QToolTip.hideText()
            return
        data = self.draw_store.readData(self.selected.polyIndex)
        show_label = '\n'.join([f'{k}：{v if v else "无"}' for k, v in data['options'].items()])
        QtWidgets.QToolTip.showText(event.globalPos(), show_label)

    def _showData(self, painter: QtGui.QPainter) -> None:
        """
        绘制标注数据
        :param painter: 画笔(QtGui.QPainter)
        :return:
        """
        if self.temp_data:
            draw_temp_data = self.temp_data + ([self.mouse_pos] if self._draw_mode != 'rect' else [])
            datas = [{'data': draw_temp_data, 'mode': self._draw_mode}, ]
            temp = 1
        else:
            datas = []
            temp = -1
        if self.draw_store:
            datas = self.draw_store.readData() + datas
            temp = len(datas) - temp
        for data_index, data in enumerate(datas):
            if not data['data']: continue
            if temp == data_index:
                parameter = [True, None]
            elif self.selected.isSelect and self.selected.polyIndex == data_index and not self.isCtrl:
                continue
            else:
                parameter = [False, None]
            self._drawSelected(painter, parameter, temp, data_index, data)
        if self.selected.isSelect and not self.isCtrl:
            parameter = [True, None]
            self._drawSelected(painter, parameter, temp, self.selected.polyIndex, datas[self.selected.polyIndex])
        pass

    def _drawSelected(self, painter, parameter, temp, data_index, data):
        """
        映射至绘制模式
        :param painter: 画笔
        :param parameter:
        :param temp:
        :param data_index:
        :param data:
        :return:
        """
        is_draw_point = parameter[0]
        draw_data: List[QtCore.QPointF] = [self.showPoint(point) for point in data['data']]
        mode_type = data['mode_type'] if 'mode_type' in data else 'normal'
        data_type = data['mode']
        if self.isInstance and temp != data_index:
            options = data['options']
            if '实例' in options:
                parameter[1] = options['实例']
            elif (id_name := self.options['实例'][f'{self.language}_name']) in options:
                parameter[1] = options[id_name]

        elif temp != data_index:
            data_label = data['options'][self.label_key]
            parameter.append(data_label)

        style = self.draw_style.getGeneralStyle(*parameter)
        painter.setPen(style[0])
        if data_type in self.isFill and self.isFill[data_type] or self.isFill['default']:
            painter.setBrush(style[1])
        else:
            painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)

        if data_type == 'rect':
            self._drawRect(mode_type, painter, draw_data, is_draw_point, style[2])
        elif data_type == 'poly':
            self._drawPoly(mode_type, painter, draw_data, is_draw_point, style[2])
        elif data_type == 'point':
            self._drawPoint(mode_type, painter, draw_data, style[2])
        elif data_type == 'line':
            self._drawLine(mode_type, painter, draw_data, is_draw_point, style[2])
        else:
            self._drawMode(mode_type, data_type, painter, draw_data, is_draw_point, style[2])

    def _drawMode(self, mode_type: str, data_type, painter, draw_data, is_draw_point: bool, point_style):
        """
        绘制自定义图形
        :param mode_type: 模式类型
        :param point_style: 点的颜色
        :param is_draw_point: 是否是临时数据
        :param data_type: 自定义模式名称
        :param painter: 画笔
        :param draw_data: 数据
        :return:
        """
        self.drawPlug.getMode(data_type).drawMode(mode_type, painter, draw_data, is_draw_point, point_style)
        if self.isDrawPolyPoint or is_draw_point:
            # 画笔配置
            self._drawPoint(mode_type, painter, draw_data, point_style)

    def _drawRect(self, mode_type: str, painter: QtGui.QPainter, draw_data: List[QtCore.QPointF], is_draw_point: bool,
                  point_style) -> None:
        """
        绘制矩形
        :param mode_type: 模式类型
        :param point_style: 点的颜色
        :param is_draw_point: 是否是临时数据
        :param draw_data: 数据
        :param painter: 画笔(QtGui.QPainter)
        :return:
        """
        if len(draw_data) != 2: raise ValueError('rect array shape is incorrect')
        # 画笔配置
        painter.drawRect(QtCore.QRectF(*draw_data))
        if self.isDrawPolyPoint or is_draw_point:
            # 画笔配置
            self._drawPoint(mode_type, painter, draw_data, point_style)
        pass

    def _drawPoly(self, mode_type: str, painter: QtGui.QPainter, draw_data: List[QtCore.QPointF], is_draw_point: bool,
                  point_style) -> None:
        """
        绘制轮廓
        :param mode_type: 模式类型
        :param point_style: 点的颜色
        :param is_draw_point: 是否是临时数据
        :param draw_data: 数据
        :param painter: brush: 画笔(QtGui.QPainter)
        :return:
        """
        # 画笔配置
        painter.drawPolygon(draw_data)
        if self.isDrawPolyPoint or is_draw_point:
            # 画笔配置
            self._drawPoint(mode_type, painter, draw_data, point_style)
        pass

    def _drawPoint(self, mode_type: str, painter: QtGui.QPainter, draw_data: List[QtCore.QPointF], point_style) -> None:
        """
        绘制点
        :param mode_type: 模式类型
        :param point_style: 点的颜色
        :param draw_data: 数据
        :param painter: brush: 画笔(QtGui.QPainter)
        :return:
        """
        painter.setBrush(point_style)
        for index, point in enumerate(draw_data):
            # 画笔配置
            painter.drawEllipse(point, self.point_size, self.point_size)
        pass

    def _drawLine(self, mode_type: str, painter: QtGui.QPainter, draw_data: List[QtCore.QPointF], is_draw_point: bool,
                  point_style) -> None:
        """
        绘制线段
        :param mode_type: 模式类型
        :param point_style: 点的颜色
        :param is_draw_point: 是否是临时数据
        :param draw_data: 数据
        :param painter: brush: 画笔(QtGui.QPainter)
        :return:
        """
        # 画笔配置
        points = [(i.x(), i.y()) for i in draw_data]
        if points[-1] == points[-2]:
            del points[-1]
        if (self.mode_type == 'path' or mode_type == 'path') and len(points) >= 3:
            curve = fitting.interpolate_curve(points, 2)
            curve.delta = 0.01
            draw_data2 = [QtCore.QPointF(i[0], i[1]) for i in curve.evalpts]
            painter.drawPolyline(draw_data2)
        else:
            painter.drawPolyline(draw_data)
        if self.isDrawPolyPoint or is_draw_point:
            # 画笔配置
            self._drawPoint(mode_type, painter, draw_data, point_style)
        pass

    def drawStop(self) -> None:
        """
        标注结束
        :return: None
        """
        copy_temp_data = self.temp_data.copy()
        if self._draw_mode == 'rect':
            copy_temp_data_x = [point.x() for point in copy_temp_data]
            copy_temp_data_y = [point.y() for point in copy_temp_data]
            copy_temp_data = [
                QtCore.QPointF(min(copy_temp_data_x), min(copy_temp_data_y)),
                QtCore.QPointF(max(copy_temp_data_x), max(copy_temp_data_y))
            ]
            rect = QtCore.QRectF(*copy_temp_data)
            if rect.width() < self.draw_rect_min_size[0] or rect.height() < self.draw_rect_min_size[1]:
                self.temp_data.clear()
                # TODO: 提示尺寸
                return
        if self._draw_mode == 'poly':
            if (self._calculate_area(QtGui.QPolygonF(copy_temp_data))) < self.draw_poly_min_size:
                self.temp_data.clear()
                # TODO: 提示尺寸
                return
        option_data = self.selectDialog.showSelect()
        self.temp_data.clear()
        self.isDraw = False
        self.speed_up = False
        if not option_data: return
        if self._draw_mode not in self._preinstall_modes:
            copy_temp_data, option_data = self.drawPlug.getMode(self._draw_mode).drawData(self.mode_type,
                                                                                          copy_temp_data, option_data)
        draw_data = {
            'mode': self._draw_mode,
            'mode_type': self.mode_type,
            'data': copy_temp_data,
            'options': option_data,
        }
        self.draw_store.addData(draw_data)
        self.isSave = True

    def checkSelection(self, event: QtGui.QMouseEvent) -> None:
        """
        检查选择状态
        :param event: QtGui.QMouseEvent
        :return:
        """
        if self.selected.isSelect and self.left_mouse_click: return
        if self.isDraw or self.is_move or not self.draw_store or not self._draw_mode:
            self.selected.clearSelect()
            return
        self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
        self.selected.clearSelect()
        if self.speed_up: return
        near_distance = (5 * self.zoom)
        data_area = None
        for index, value in enumerate(self.draw_store.readData()):
            mode = value['mode']
            data = value['data']
            poly_data = value['data']
            for point_index, point in enumerate(data):
                if (point.x() + near_distance > self.mouse_pos.x() > point.x() - near_distance and
                        point.y() + near_distance > self.mouse_pos.y() > point.y() - near_distance):
                    self.selected.setSelect(index, point_index)
                    self.setCursor(QtCore.Qt.CursorShape.CrossCursor)
                    return
            # 矩形可调整边
            if mode == 'rect':
                min_x_point = 1 if data[0].x() > data[1].x() else 0
                min_y_point = 1 if data[0].y() > data[1].y() else 0
                x_set = {point.x() for point in data}
                y_set = {point.y() for point in data}
                min_x = min(x_set)
                max_x = max(x_set)
                min_y = min(y_set)
                max_y = max(y_set)
                if min_x + near_distance > self.mouse_pos.x() > min_x - near_distance and \
                        max_y > self.mouse_pos.y() > min_y:
                    self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
                    self.selected.setSelect(index, min_x_point, 0)
                elif max_x + near_distance > self.mouse_pos.x() > max_x - near_distance and \
                        max_y > self.mouse_pos.y() > min_y:
                    self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
                    self.selected.setSelect(index, 1 - min_x_point, 0)
                elif min_y + near_distance > self.mouse_pos.y() > min_y - near_distance and \
                        max_x > self.mouse_pos.x() > min_x:
                    self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
                    self.selected.setSelect(index, min_y_point, 1)
                elif max_y + near_distance > self.mouse_pos.y() > max_y - near_distance and \
                        max_x > self.mouse_pos.x() > min_x:
                    self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
                    self.selected.setSelect(index, 1 - min_y_point, 1)
                else:
                    poly_data = [
                        QtCore.QPointF(min_x, min_y),
                        QtCore.QPointF(max_x, min_y),
                        QtCore.QPointF(max_x, max_y),
                        QtCore.QPointF(min_x, max_y),
                    ]
            # TODO: $插件模式的选择特性添加位置
            poly_f = QtGui.QPolygonF(poly_data)
            if poly_f.containsPoint(self.mouse_pos.toPoint(), QtCore.Qt.FillRule.OddEvenFill):
                area = self._calculate_area(poly_f)
                if data_area is not None and area > data_area: continue
                self.selected.setSelect(index)
                data_area = area
                self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

    @staticmethod
    def _calculate_area(polygon: QtGui.QPolygonF):
        """
        计算 QPolygonF 的面积。
        :param polygon: 多边形
        :return 多边形面积
        """
        area = 0.0
        n = polygon.size()
        if n < 3:
            return area

        for i in range(n):
            p1 = polygon.at(i)
            p2 = polygon.at((i + 1) % n)
            area += (p1.x() * p2.y() - p2.x() * p1.y())

        area /= 2.0
        return abs(area)

    def __moveDataPosition(self, event: QtGui.QMouseEvent) -> None:
        """
        移动图形位置
        :param event: QtGui.QMouseEvent
        :return:
        """
        if not self.selected.isSelect or self.isDraw or not self.left_mouse_click:
            self.isMovePloy = False
            return
        if not self.isMovePloy:
            self.draw_store.addRollback()
        self.isMovePloy = True
        poly = self.draw_store.readData(self.selected.polyIndex)['data']
        offset = event.position() - self.left_mouse_click_pos
        if self.selected.selectState() == 1:
            self.draw_store.editData(
                index=self.selected.polyIndex,
                data=[point + (offset * self.zoom) for point in poly],
                is_roll=False
            )
        elif self.selected.selectState() == 2:
            self.draw_store.editData(
                index=self.selected.polyIndex,
                data=poly[self.selected.pointIndex] + (offset * self.zoom),
                child_index=self.selected.pointIndex,
                is_roll=False
            )
        elif self.selected.selectState() == 3:
            if self.selected.sideIndex:
                edit_data = poly[self.selected.pointIndex] + (QtCore.QPointF(0, offset.y()) * self.zoom)
            else:
                edit_data = poly[self.selected.pointIndex] + (QtCore.QPointF(offset.x(), 0) * self.zoom)
            self.draw_store.editData(
                index=self.selected.polyIndex,
                data=edit_data,
                child_index=self.selected.pointIndex,
                is_roll=False
            )
        self.left_mouse_click_pos = event.position()

    @QtCore.Slot()
    def __delDataPosition(self) -> None:
        """
        删除轮廓
        :return:
        """
        if not self.selected.isSelect: return
        select = self.draw_store.readData(self.selected.polyIndex)
        if not self.speed_up and select['mode'] != 'rect' and self.selected.selectState() > 1:
            is_verify = False
            if select['mode'] == 'poly' and len(select['data']) > 4:
                is_verify = True
            elif select['mode'] == 'line' and len(select['data']) > 2:
                is_verify = True
            elif select['mode'] == 'point' and len(select['data']) > 0:
                is_verify = True
            elif self.drawPlug.getMode(select['mode']).rule < len(select['data']):
                is_verify = True
            if is_verify:
                self.draw_store.delData(self.selected.polyIndex, self.selected.pointIndex)
                return
        self.draw_store.delData(self.selected.polyIndex)
        self.selected.clearSelect()

    @abstractmethod
    def mouseLeft(self, event: QtGui.QMouseEvent) -> None:
        """
        鼠标左键按下回调
        :param event: QtGui.QMouseEvent
        :return: None
        """
        pass

    @abstractmethod
    def mouseRight(self, event: QtGui.QMouseEvent) -> None:
        """
        鼠标右键按下回调
        :param event: QtGui.QMouseEvent
        :return: None
        """
        pass

    @abstractmethod
    def mouseMove(self, event: QtGui.QMouseEvent) -> None:
        """
        鼠标移动回调
        :param event: QtGui.QMouseEvent
        :return: None
        """
        pass

    @abstractmethod
    def mouseRelease(self, event: QtGui.QMouseEvent) -> None:
        """
        鼠标松开回调
        :param event: QtGui.QMouseEvent
        :return: None
        """
        if self._draw_mode == 'rect' and len(self.temp_data) == 2 and not self.is_move:
            # 矩形数据完成
            self.drawStop()
            pass
        elif self._draw_mode == 'point' and len(self.temp_data) == self.draw_point_num:
            self.drawStop()
        pass

    @abstractmethod
    def keyPress(self, event: QtGui.QKeyEvent) -> None:
        """
        按键按下回调
        :param event: QtGui.QKeyEvent
        :return: None
        """
        pass

    @abstractmethod
    def keyRelease(self, event: QtGui.QKeyEvent) -> None:
        """
        按键松开回调
        :param event: QtGui.QKeyEvent
        :return: None
        """
        pass

    @staticmethod
    @abstractmethod
    def __decode(path: Path) -> Image:
        """
        解密文件数据
        :param path: 文件路径pathlib对象
        :return: PIL.Image
        """
        pass
