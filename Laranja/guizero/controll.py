from guizero import App, PushButton, TextBox

def show():
    text_box.show()

def hide():
    text_box.hide()

def enable():
    text_box.enable()

def disable():
    text_box.disable()

app = App()

text_box = TextBox(app)

show_button = PushButton(app, text="show", command=show)
hide_button = PushButton(app, text="hide", command=hide)
enable_button = PushButton(app, text="enable", command=enable)
disable_button = PushButton(app, text="disable",command=disable)

app.display()
