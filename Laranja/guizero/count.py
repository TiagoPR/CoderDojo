from guizero import App, TextBox, Text

def count():
    character_count.value = len(entered_text.value)

app = App()
entered_text = TextBox(app, command=count)
character_count = Text(app)

app.display()