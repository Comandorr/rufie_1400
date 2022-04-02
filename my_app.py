# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
from time import *

from instr import *

app = QApplication([])
window = QWidget()
window.show()

# ВИДЖЕТЫ ПЕРВОГО ЭКРАНА
label1 = QLabel('Добро пожаловать!')
label2 = QLabel(start_instr)
knopka_start = QPushButton('Начать')
ekran1 = [label1, label2, knopka_start]

# ВИДЖЕТЫ ВТОРОГО ЭКРАНА
label_age = QLabel('Введите возраст:')
edit_age = QLineEdit()
label_inst_1 = QLabel('Лягте на спину и замерьте пульс за 15 сек')
knopka_test_1 = QPushButton('Начать отсчет')

label_inst_2 = QLabel('Выполните 30 приседаний за 45 сек')
knopka_test_2 = QPushButton('Начать отсчет приседаний')

label_inst_3 = QLabel(final_instr)
knopka_timer = QPushButton('Начать отсчет')
edit_pulse_1 = QLineEdit()
edit_pulse_2 = QLineEdit()
knopka_final = QPushButton('Завершить тест')

ekran2 = [label_age, edit_age, label_inst_1, knopka_test_1,
label_inst_2, knopka_test_2, label_inst_3, knopka_timer,
edit_pulse_1, edit_pulse_2, knopka_final]

line_1 = QVBoxLayout()
line_1.addWidget(label1)
line_1.addWidget(label2)
line_1.addWidget(knopka_start)

for w in ekran2:
    line_1.addWidget(w)
    w.hide()

def start():
    for w in ekran1:
        w.hide()
    for w in ekran2:
        w.show()
knopka_start.clicked.connect(start)


window.setLayout(line_1)
app.exec_()