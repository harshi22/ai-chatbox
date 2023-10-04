from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

chatbot = ChatBot("Tom Cruise")

convo = {
    'hello',
    'hi there!',
    'My name is Tom Cruise'
}

trainer = ListTrainer(chatbot)
trainer.train(convo)


#print("Talk to bot")


main = Tk()

main.geometry("500x650")

main.title("My chat Bot")

#img = PhotoImage(file="C:/Users/haaga/Desktop/Python/chatbot/imgg.png")
#photoL = Label(main, image=img)

#photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = chatbot.get_response(query)
    msgs.insert(END, "you  :  " + query)
    msgs.insert(END, "bot :  " + str(answer_from_bot))
    textF.delete(0, END)
    #print("clicked")



frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF=Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function

def enter_function(event):
    btn.invoke()

#going to bind main window with enter key
main.bind('<Return>', enter_function)

main.mainloop()