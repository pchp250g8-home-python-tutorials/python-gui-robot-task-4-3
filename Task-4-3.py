# --coding:utf-8--

from robot import *

while is_free_right() or is_free_left() or is_free_up():
    while is_free_right():
        move_right()
    paint()
    while is_free_down():
        move_down()
    paint()
    while is_free_left():
        move_left()
    paint()
    while is_free_up():
        move_up()
