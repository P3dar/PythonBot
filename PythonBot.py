import requests
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# send the message to telegram chat


def send_to_telegram(message):

    apiToken = ''  # Insert API Token
    chatID = ''  # Insert any ChatID
    apiURL = f''  # Insert APIurl

    try:
        response = requests.post(
            apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)


# window for the bot
app_window = Tk()
app_window.title("PythonBot")
w = 500  # Width
h = 400  # Height
app_window.configure(bg="white")
app_window.resizable(0, 0)

# move window to center
winWidth = app_window.winfo_screenwidth()
winHeight = app_window.winfo_screenheight()
x = (winWidth/2) - (w/2)
y = (winHeight/2) - (h/2)
app_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

# GUI elements
title = Label(text="Welcome to PythonBot!", background="white",
              foreground="grey1", font=("boulder", 18, "bold"))
title.pack(side="top")

brief_text = Label(text="Welcome fellow python lover!\n Type you message and send it to your friends via telegram!", background="white",
                   foreground="grey1", font=("boulder", 10, "bold"))
brief_text.pack()

Img = ImageTk.PhotoImage(Image.open("logo.png"))
Image = Label(image=Img).pack(side="bottom")
message_box = Entry()
message_box.pack()

# check if the message isn't empty, then activate the telegram funcion


def send_message():
    inp = str(message_box.get())
    if len(inp) != 0:
        send_to_telegram(inp)
    else:
        messagebox.showwarning(
            "Error", "The message is blank")

# clear the textbox after sending a message


def clear_text():
    message_box.delete(0, END)


# create a button and give the commands when pressed
send_button = Button(text="send", command=lambda: [
                     send_message(), clear_text()])
send_button.pack()

# launch the app
app_window.mainloop()
