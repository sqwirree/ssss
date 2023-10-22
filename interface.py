from main_meme import *
from main_data import *

from random import choice, shuffle

ans_buttons = [ans1_button, ans2_button, ans3_button, ans4_button]
shuffle(ans_buttons)

frm = Form("Сколько надо?", "1", "2", "3", "10032903")
frm_card = FormView(frm, question_label, ans_buttons[0], ans_buttons[1], ans_buttons[2], ans_buttons[3])

main_window = QWidget()
main_window.resize(600, 400)

main_window.setLayout(main_layout)
main_window.show()
app.exec()