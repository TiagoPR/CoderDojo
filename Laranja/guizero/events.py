from guizero import App, PushButton, Text

def say_hello():
    message.value = "Hello"

app = App()
message = Text(app)
button = PushButton(app, text="Press me", command=say_hello)

app.display()