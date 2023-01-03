from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets.components.ui_types import ButtonType, ButtonSize, BorderStyle
from widgets.components.styles.button_style import ButtonStyle

class BaseCheckBox(QCheckBox):
    """
    基础的StyleSheet
    """
    def __init__(self, *args):
        super(BaseCheckBox, self).__init__(*args)
        self.__init_style() # 设置样式


    def __init_style(self):
        checkbox_style = '''
        QCheckBox {
        border: none;
        border-radius: 13px;
        }
        QCheckBox::indicator{
    background-color: rgb(42, 45, 66);
    border: 0px solid #b1b1b1;
	width: 46px;
	height: 26px;
	border-radius: 13px;
   }

QCheckBox:enabled:checked{
	color: rgb(255, 255, 255);
}
QCheckBox:enabled:!checked{
	color: rgb(255, 255, 255);
}

QCheckBox::indicator:checked {
        background-color: rgb(27, 177, 193);
}


QCheckBox::indicator:unchecked {
background-color: rgb(42, 45, 66);
}
        '''
        self.setStyleSheet(self.styleSheet() + checkbox_style)


    def mousePressEvent(self, *args, **kwargs):
        return super(BaseCheckBox, self).mousePressEvent(*args, **kwargs)

    def mouseReleaseEvent(self, *args, **kwargs):
        return super(BaseCheckBox, self).mouseReleaseEvent(*args, **kwargs)

    def paintEvent(self, pa : QPaintEvent):
        super(BaseCheckBox, self).paintEvent(pa)
        if self.isChecked():
            painter = QPainter(self)
            painter.setPen(Qt.white)
            painter.setBrush(Qt.white)
            # painter.drawText(self.rect(), Qt.AlignLeft, "test")
            painter.drawEllipse(24, 4, 18, 18)
        else:
            painter = QPainter(self)
            painter.setPen(Qt.white)
            painter.setBrush(Qt.white)
            # painter.drawText(self.rect(), Qt.AlignLeft, "test")
            painter.drawEllipse(5, 4, 18, 18)
