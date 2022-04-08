import tkinter

def on_off():
    if OnOffButton["text"] == "ON":
        window.configure(bg="red")
        OnOffButton["text"] = "OFF"
    else:
        window.configure(bg="blue")
        OnOffButton["text"] = "ON"

def quit():
    window.destroy()

window = tkinter.Tk()
window.geometry("300x200")
window.title("ON OFF BUTTON")

OnOffButton = tkinter.Button(window,text="OFF",
                             width= 10,
                             command=on_off)

QuitButton = tkinter.Button(window,text="Quit",
                            width=15,
                            command=quit)

QuitButton.pack(side="bottom")
OnOffButton.pack()
window.mainloop()