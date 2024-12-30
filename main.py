import io
import sys
import random

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtWidgets import (QApplication, QMainWindow, QDialog, QLabel, QSpinBox, QPushButton, QVBoxLayout, QHBoxLayout,
                             QInputDialog)

my_widget_design = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>300</width>
    <height>400</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Генерация флага</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>45</x>
      <y>0</y>
      <width>210</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Ввести количество цветов флага</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class RandomFlag(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(my_widget_design)
        uic.loadUi(f, self)

        self.cnt = 0
        self.base = [45, 50, 100, 30]
        self.button.clicked.connect(self.act)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for i in range(self.cnt):
            qp.setBrush(QColor(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))
            qp.drawRect(self.base[0], self.base[1] + self.base[3] * i, self.base[2],
                            self.base[3])
        qp.end()

    def act(self):
        self.cnt, flag = QInputDialog.getInt(
            self, "Выберите значение", "Введите значение:",
            3, 1, 10, 1)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomFlag()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())


