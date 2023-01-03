from moviepy.editor import *
from utils.log import g_log
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from widgets.main_widget import MainWidget
import os
import sys

def test_gif_function():
    clip = VideoFileClip("test.mp4")
    clip = clip.subclip(0, 10)
    clip.write_gif("test.gif")


# 资源文件目录访问
def source_path(relative_path):
    # 是否Bundle Resource
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 修改当前工作目录，使得资源文件可以被正确访问
cd = source_path('')
os.chdir(cd)


if __name__ == '__main__':
    g_log.info("程序启动")
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QtWidgets.QApplication([""])
    widget = MainWidget()
    widget.show()
    ret = app.exec_()
    sys.exit(ret)