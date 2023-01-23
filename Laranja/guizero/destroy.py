from guizero import App, PushButton, Text

def destroy_message():
    message.destroy()

app = App()
message = Text(app, text="Destroy me!")
destroy_button = PushButton(app, text="Destroy", command=destroy_message)

app.display()