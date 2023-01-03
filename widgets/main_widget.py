from widgets.components.base_frameless_widget import BaseFramelessWidget
from widgets.components.base_button import BaseButton
from widgets.components.ui_types import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from utils.log import g_log
import os
import sys
from utils.tool import MovieTool
from moviepy.editor import *


# 主界面

class MainWidget(BaseFramelessWidget):
    """
    主窗体程序
    """
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent=parent)
        self.mp4_file_name = ""
        self.__init_ui()
        self.__init_style()
        self.__init_signals()
        self.__init_others()

    def __init_ui(self):
        """
        初始化UI：主要是控件的增加以及总体的布局
        :return:
        """
        g_log.info("初始化UI")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(QSize(988,670))

        # 总体布局VBox
        self.all_layout = QVBoxLayout()
        self.setLayout(self.all_layout)

        min_button = BaseButton()
        min_button.init_button("","resource/image/min.png")
        self.min_layout = QHBoxLayout()
        self.min_layout.addWidget(min_button,0 , Qt.AlignHCenter)
        min_button.clicked.connect(self.slots_set_min)
        self.all_layout.addLayout(self.min_layout)

        title_label = QLabel()
        title_label.setText("MP4 To Gif")

        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(title_label,0,Qt.AlignHCenter)

        self.all_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.all_layout.addLayout(self.title_layout)


        # 设置背景图
        self.preview_label = QLabel()
        self.preview_label.setFixedSize(QSize(632,402))
        self.preview_pixmap = QPixmap()
        self.preview_pixmap.load("resource/image/preview.png")
        self.preview_pixmap = self.preview_pixmap.scaled(632,402, Qt.KeepAspectRatioByExpanding)
        self.preview_label.setPixmap(self.preview_pixmap)
        self.preview_layout = QHBoxLayout()
        self.preview_layout.addWidget(self.preview_label,0, Qt.AlignHCenter)

        self.all_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.all_layout.addLayout(self.preview_layout)


        self.choose_file_button = BaseButton()
        self.choose_file_button.init_button("Choose Your Mp4 File","",ButtonType.BUTTON_SUCCESS)
        self.choose_file_button.setStyleSheet(self.choose_file_button.styleSheet() + "QPushButton { font: 12px; }")
        self.choose_file_button.setFixedHeight(46)
        self.choose_file_button.setFixedWidth(180)
        self.choose_file_button.setEnabled(True)

        self.choose_file_layout = QHBoxLayout()
        self.choose_file_layout.addWidget(self.choose_file_button,0,Qt.AlignHCenter)

        self.all_layout.addItem(QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.all_layout.addLayout(self.choose_file_layout)

        # button

        self.begin_to_convert_button = BaseButton()
        self.begin_to_convert_button.init_button("Begin To Convert Gif","",ButtonType.BUTTON_DANGER)
        self.begin_to_convert_button.setStyleSheet(self.begin_to_convert_button.styleSheet() + "QPushButton { font: 12px; }")
        self.begin_to_convert_button.setFixedHeight(46)
        self.begin_to_convert_button.setFixedWidth(180)
        self.begin_to_convert_button.setEnabled(False)

        self.begin_to_layout = QHBoxLayout()
        self.begin_to_layout.addWidget(self.begin_to_convert_button,0,Qt.AlignHCenter)

        self.all_layout.addItem(QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.all_layout.addLayout(self.begin_to_layout)
        self.all_layout.addStretch()

    def __init_style(self):
        """
        初始化样式QSS
        :return:
        """
        self.setStyleSheet(self.styleSheet() + "QWidget{ background-color: rgb(238, 232, 244);}")
        pass

    def __init_signals(self):
        """
        初始化信号
        :return:
        """
        self.choose_file_button.clicked.connect(self.slots_choose_mp4_file)
        self.begin_to_convert_button.clicked.connect(self.slots_begin_convert)
        pass

    def __init_others(self):
        """
        剩余部分初始化 包括数据初始化
        :return:
        """
        pass

    def paintEvent(self, event: QPaintEvent) -> None:
        # self.paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(Qt.SolidPattern)
        color = QColor()
        color.setRgb(238, 232, 244)
        brush.setColor(color)
        painter.setBrush(brush)
        painter.setPen(Qt.transparent)
        rect = self.rect()
        rect.setWidth(rect.width() - 1)
        rect.setHeight(rect.height() - 1)
        painter.drawRoundedRect(rect, 15, 15)

    def slots_choose_mp4_file(self):
        file_name, file_type = QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(), "Mp4 Files(*.mp4)")
        g_log.info(f"file_name:{file_name},file_type: {file_type}")
        print(f"file_name:{ file_name}")
        if file_name is None or file_name == "":
            print("None")
        else:
            self.mp4_file_name = file_name
            clip = VideoFileClip(self.mp4_file_name)
            if os.path.exists("title.png"):
                os.remove("title.png")
            clip.save_frame("title.png", 0)
            self.preview_pixmap.load("title.png")
            self.preview_pixmap = self.preview_pixmap.scaled(632,402, Qt.KeepAspectRatioByExpanding)
            self.preview_label.setPixmap(self.preview_pixmap)
            self.begin_to_convert_button.setEnabled(True)

    def slots_begin_convert(self):
        if self.mp4_file_name is None or self.mp4_file_name == "":
            return
        convert_gif_file = self.mp4_file_name.replace(".mp4",".gif")
        g_log.info(f"file:{self.mp4_file_name}, convert to file:{convert_gif_file}")
        if os.path.exists(convert_gif_file):
            os.remove(convert_gif_file)
        MovieTool.save_mp4_to_gif(self.mp4_file_name,convert_gif_file)
        os.startfile(convert_gif_file)

    def slots_set_min(self):
        self.showMinimized()





