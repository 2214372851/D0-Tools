class ToolsTemp:
    """
    工具缓存类
    """
    # 版本
    THEMES = None
    VERSION = None
    # 移动窗口标定点位
    MOVE_WINDOW_POSITION = None
    # 是否改变鼠标样式
    IS_WINDOW_SIZE = 0
    # 是否依据鼠标样式改变窗口大小
    IS_CLICK_WINDOW_SIZE = None
    # 打开的文件夹
    OPEN_DIR_PATH = None
    # 打开文件夹下的文件
    OPEN_DIR_FILES = []
    # 当前语言
    LANGUAGE = None
    # 上次打开路径
    lastOpenPath = None

    MENU_BUTTON_STYLE = '''
    QPushButton{color: rgb(255, 255, 255);background-color: rgba(30, 30, 30, 0);}
    QPushButton:hover{background-color: rgb(56, 58, 61);border-radius:5px;}
    '''
    MENU_BUTTON_CLICK_STYLE = '''
    background-color: rgb(53, 116, 239);border-radius:5px;
    '''
