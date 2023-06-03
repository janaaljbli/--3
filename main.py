def on_button_pressed_a():
    jist.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global add
    add = 3 + 5
    basic.show_number(add)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

add = 0
jist: game.LedSprite = None
jist = game.create_sprite(4, 2)

def on_forever():
    pass
basic.forever(on_forever)
