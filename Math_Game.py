from tkinter import *
import random, time
import tkinter.messagebox as tk

#=================================#
# FUNCTIONS                       #
#=================================#

def Language_Settings(self):
    Selected_Language = languageOptionVar.get()

    if(Selected_Language == "French"):
        entryLabel.config(text="Nom de joueur")
        subjectFrame.config(text="sujets")
        addingCheck.config(text="Ajouter")
        subtractingCheck.config(text="Soustraire")
        multiplyingCheck.config(text="Multiplier")
        divisionCheck.config(text="Partage")
        questionNumScale.config(label= "Nombre de questions")
        languageLabel.config(text="paramètres de langue")
        questionVar.set("Appuyez sur Start")
        confirmButton.config(text="Confirmer")
        startButton.config(text="Début")
        finishButton.config(text="Terminer")
        howToPlayButton.config(text="Comment jouer")

    elif(Selected_Language == "English"):
        entryLabel.config(text="Player Name")
        subjectFrame.config(text="Subjects")
        addingCheck.config(text="Adding")
        subtractingCheck.config(text="Subtracting")
        multiplyingCheck.config(text="Multiplying")
        divisionCheck.config(text="Division")
        questionNumScale.config(label= "Number of Questions")
        languageLabel.config(text="Language Settings")
        questionVar.set("Press Start")
        confirmButton.config(text="Confirm")
        startButton.config(text="Start")
        finishButton.config(text="Finish")
        howToPlayButton.config(text="How To Play")
    
    elif(Selected_Language == "German"):
        entryLabel.config(text="Spielername")
        subjectFrame.config(text="Fächer")
        addingCheck.config(text="Hinzufügen")
        subtractingCheck.config(text="Subtrahieren")
        multiplyingCheck.config(text="Multiplizieren")
        divisionCheck.config(text="Teilen")
        questionNumScale.config(label= "Anzahl der Fragen")
        languageLabel.config(text="Spracheinstellungen")
        questionVar.set("drücke Start")
        confirmButton.config(text="Bestätigen")
        startButton.config(text="Start")
        finishButton.config(text="Fertig")
        howToPlayButton.config(text="Spielanleitung")
    
    elif(Selected_Language == "Italian"):
        entryLabel.config(text="Nome del giocatore")
        subjectFrame.config(text="Soggetti")
        addingCheck.config(text=" Aggiunta")
        subtractingCheck.config(text=" sottraendo")
        multiplyingCheck.config(text="Moltiplicando")
        divisionCheck.config(text="Dividendo")
        questionNumScale.config(label= "Numero di domande")
        languageLabel.config(text="Impostazioni della lingua")
        questionVar.set("Premi start")
        confirmButton.config(text="Confermare")
        startButton.config(text="Inizio")
        finishButton.config(text="Finire")
        howToPlayButton.config(text="Come giocare")

    elif(Selected_Language == "Spanish"):
        entryLabel.config(text="Nombre del jugador")
        subjectFrame.config(text="Asignaturas")
        addingCheck.config(text="Agregando")
        subtractingCheck.config(text="Restando")
        multiplyingCheck.config(text="Multiplicando")
        divisionCheck.config(text="Divisor")
        questionNumScale.config(label= "Numero de preguntas")
        languageLabel.config(text="Configuración de lenguaje")
        questionVar.set("Presiona inicio")
        confirmButton.config(text="Confirmar")
        startButton.config(text="Comienzo")
        finishButton.config(text="Terminar")
        howToPlayButton.config(text="Cómo jugar")
    
    elif(Selected_Language == "Russian"):
        entryLabel.config(text="Имя игрока")
        subjectFrame.config(text="Предметы")
        addingCheck.config(text="Добавление")
        subtractingCheck.config(text="Вычитание")
        multiplyingCheck.config(text="Умножив")
        divisionCheck.config(text="Разделив")
        questionNumScale.config(label="Количество вопросов")
        languageLabel.config(text="Языковые настройки")
        questionVar.set("нажмите старт")
        confirmButton.config(text="Подтверждение")
        startButton.config(text="Начало")
        finishButton.config(text="финиш")
        howToPlayButton.config(text="Как играть")
    


def howToPlay():
    tk.showinfo("How to Play", f"You get 5 points for every right answer and lost 5 points for every wrong answer\n\n You can choose your subject and language and number of question\n in order check your answer press confirm")

def showResultInfo():
    Max_Score = scoreVar.get()
    Player_Name = nameVar.get()
    Total_Score = pointsVar.get()
    Question_Number = questionNumVar.get()

    if(Total_Score > Max_Score):
        scoreVar.set(Total_Score)

    pointsVar.set(0)
    questionVar.set("Press Start")

    tk.showinfo("Results", f"Player Name = {Player_Name} \nTotal_Score = {Total_Score} \nQuestion Number = {Question_Number}")
         

def Answer_Check():
    global Answered_Questions, Question_Number, Correct_Answer, Point

    Answered_Questions = 0
    User_Answer = answerVar.get()

    if(User_Answer == Correct_Answer):
        Point = Point + 5
        Answered_Questions += 1
        resultVar.set("!!! Correct !!!")
        resultLabel.config(bg="green")
        pointsVar.set(Point)
        Game_Launcher()

    else:
        Point -= 5
        Answered_Questions += 1
        resultLabel.config(bg="red")
        resultVar.set("!!! Wrong !!!")
        pointsVar.set(Point)
        Game_Launcher()

    if(Question_Number == Answered_Questions):
        showResultInfo()
       
    
def Game_Launcher():
    global Answered_Questions, Question_Number, Correct_Answer, Point

    Question_Types = []
    Answers = []

    Adding = addingVar.get()
    Subtracting = subtractingVar.get()
    Multiplying = multiplyingVar.get()
    Division = divisionVar.get()

    if(Adding != 0): Question_Types.append(Adding)
    if(Subtracting != 0): Question_Types.append(Subtracting)
    if(Multiplying != 0): Question_Types.append(Multiplying)
    if(Division != 0):Question_Types.append(Division)

    Question_Number = questionNumVar.get()

    Ques_Number1 = random.randint(1,20)
    Ques_Number2 = random.randint(1,20)

    Ans_Number1 = random.randint(1, 20)
    Ans_Number2 = random.randint(1, 20)
    

    Ans_Number3 = random.randint(1, 20)
    while Ans_Number3 in Answers:
        Ans_Number3 = random.randint(1, 20)
    Answers.append(Ans_Number3)
            

    Answers.append(Ans_Number1)
    Answers.append(Ans_Number2)

    Selected_Subject = random.choice(Question_Types)

    root.update()
    time.sleep(1)
    resultVar.set(" ")
    resultLabel.config(bg="#0BE5FF")

    if(Selected_Subject == Adding): 
        Question = f"{Ques_Number1} + {Ques_Number2} = ?" 
        questionVar.set(Question)
        Correct_Answer = Ques_Number1 + Ques_Number2
        Answers.append(Correct_Answer)

        random.shuffle(Answers)
        answer1Radio.config(text=f"{Answers[0]}", value = Answers[0])
        answer2Radio.config(text=f"{Answers[1]}", value = Answers[1])
        answer3Radio.config(text=f"{Answers[2]}", value = Answers[2])
        answer4Radio.config(text=f"{Answers[3]}", value = Answers[3])
    
    elif(Selected_Subject == Subtracting):
        Question = f"{Ques_Number1} - {Ques_Number2} = ?"
        questionVar.set(Question)
        Correct_Answer = Ques_Number1 - Ques_Number2
        Answers.append(Correct_Answer)

        random.shuffle(Answers)
        answer1Radio.config(text=f"{Answers[0]}", value = Answers[0])
        answer2Radio.config(text=f"{Answers[1]}", value = Answers[1])
        answer3Radio.config(text=f"{Answers[2]}", value = Answers[2])
        answer4Radio.config(text=f"{Answers[3]}", value = Answers[3])

    elif(Selected_Subject == Multiplying):
        Question = f"{Ques_Number1} x {Ques_Number2} = ?"
        questionVar.set(Question)
        Correct_Answer = Ques_Number1 * Ques_Number2
        Answers.append(Correct_Answer)

        random.shuffle(Answers)
        answer1Radio.config(text=f"{Answers[0]}", value = Answers[0])
        answer2Radio.config(text=f"{Answers[1]}", value = Answers[1])
        answer3Radio.config(text=f"{Answers[2]}", value = Answers[2])
        answer4Radio.config(text=f"{Answers[3]}", value = Answers[3])

    elif(Selected_Subject == Division):
        Question = f"{Ques_Number1} / {Ques_Number2}"
        questionVar.set(Question)
        Correct_Answer = Ques_Number1 / Ques_Number2
        Answers.append(Correct_Answer)
            
        random.shuffle(Answers)
        answer1Radio.config(text=f"{Answers[0]}", value = Answers[0])
        answer2Radio.config(text=f"{Answers[1]}", value = Answers[1])
        answer3Radio.config(text=f"{Answers[2]}", value = Answers[2])
        answer4Radio.config(text=f"{Answers[3]}", value = Answers[3])
     
        
    
#=================================#
# GLOBALS                         #
#=================================#

global Answered_Questions, Question_Number, Correct_Answer, Point

Answered_Questions = 0
Question_Number = 0
Correct_Answer = 0 
Language = ""
Point = 0

#=================================#
# MAIN                            #
#=================================#

root = Tk()
mainframe = Frame(root, bg="#0BE5FF") 
titleFrame = Frame(mainframe, bg="#0BE5FF") 
leftFrame = Frame(mainframe,  bg="#0BE5FF")
centerFrame = Frame(mainframe, bg="#0BE5FF")
rightFrame = Frame(mainframe, bg="#0BE5FF")

#=================================#
# WIDGETS                         #
#=================================#

userWordVar = StringVar()
userWordLabel = Label(mainframe, textvariable=userWordVar)


#Title Widget
titleLabel = Label(titleFrame, text= "Mathematic Game", font=("Beirut", 60), bg="yellow",  foreground="black")

#Left Frame Widgets
entryLabel = Label(leftFrame, text= "Player Name", font=("Arial", 20), bg="#cc0000")

nameVar = StringVar()
nameEntry = Entry(leftFrame, textvariable= nameVar, bg="#ff6666")

subjectFrame = LabelFrame(leftFrame, text="Subjects", bg="#cc0000")

addingVar = IntVar()
addingCheck = Checkbutton(subjectFrame, text= "Adding", variable= addingVar, bg="#cc0000", fg="yellow", onvalue= 5,  offvalue= 0)
subtractingVar = IntVar()
subtractingCheck = Checkbutton(subjectFrame, text= "Subtracting", variable= subtractingVar, bg="#cc0000", fg="yellow", onvalue= 6, offvalue= 0)
multiplyingVar = IntVar()
multiplyingCheck = Checkbutton(subjectFrame, text= "Multiplying", variable= multiplyingVar, bg="#cc0000", fg="yellow", onvalue= 7, offvalue= 0)
divisionVar = IntVar()
divisionCheck = Checkbutton(subjectFrame, text= "Division", variable= divisionVar, bg="#cc0000", fg="yellow", onvalue= 8, offvalue= 0)

questionNumVar = IntVar()
questionNumScale = Scale(leftFrame, from_= 1, to= 10, variable= questionNumVar, label="Number of Questions", bg="#cc0000", width=20, length= 150,  orient= HORIZONTAL  )

languageLabel = Label(leftFrame, text="Language Options", bg="#cc0000")

languages = ["English", "French", "German", "Italian", "Spanish", "Russian"]
languageOptionVar = StringVar()
languageOptionVar.set("English")
languageOptionMenu = OptionMenu(leftFrame, languageOptionVar,  *languages, command= Language_Settings)

#Center Frame Widgets
questionVar = StringVar()
questionVar.set("Press Start")
questionLabel = Label(centerFrame, textvariable= questionVar, font=("Arial", 60), bg= "#0BE5FF")

answerVar = IntVar()
answer1Radio = Radiobutton(centerFrame, text="A", variable= answerVar, value= 0, width= 27, height=2)
answer2Radio = Radiobutton(centerFrame, text="B", variable= answerVar, value= 0, width= 27, height=2)
answer3Radio = Radiobutton(centerFrame, text="C", variable= answerVar, value= 0, width= 27, height=2)
answer4Radio = Radiobutton(centerFrame, text="D", variable= answerVar, value= 0, width= 27, height=2)

confirmButton = Button(centerFrame, text="Confirm", command= Answer_Check, width=10, height=5)

resultVar = StringVar()
resultVar.set(" ")
resultLabel = Label(centerFrame, textvariable= resultVar, font=("Arial", 50), bg="#0BE5FF", width=21)

#Right Frame Widgets

pointsVar = IntVar()
pointsVar.set(0)
pointLabel = Label(rightFrame, textvariable= pointsVar, font=("Arial", 50), bg="#cc0000")

scoreVar = IntVar()
scoreVar.set(0)
scoreLabel = Label(rightFrame, textvariable= scoreVar, font=("Arial", 50), bg="#cc0000")

startButton = Button(rightFrame, text="Start", font=("Arial", 30), highlightbackground="#cc0000", command= Game_Launcher, width=10, height=3)

finishButton = Button(rightFrame, text="Finish", font=("Arial", 30), highlightbackground="#cc0000", command= showResultInfo ,width=10, height=3)

howToPlayButton = Button(rightFrame, text= "How To Play", highlightbackground="#cc0000", command= howToPlay, font=("Arial", 30))


#=================================#
# GRID                            #
#=================================#

#Frames
mainframe.grid(row= 0, column= 0)
titleFrame.grid(row=1, column=1, columnspan=3)
leftFrame.grid(row=2,  column=1)
centerFrame.grid(row=2, column=2, ipady=19)
rightFrame.grid(row=2, column=3, ipady=44)

#Title Frame Widget
titleLabel.grid(row=0, column=0, sticky=EW)

#Left Frame Widgets
entryLabel.grid(row=0, column=2, pady=(20,0))

nameEntry.grid(row=1, column=2)

subjectFrame.grid(row=2, column=2, columnspan= 2, ipadx= 50, pady= 15)
addingCheck.grid(row=1, column=1, sticky=W)
subtractingCheck.grid(row=4, column=1, sticky=W)
multiplyingCheck.grid(row=3, column=1, sticky=W)
divisionCheck.grid(row=2, column=1, sticky=W)

questionNumScale.grid(row=3, column=2)


languageLabel.grid(row=5, column=2, pady=(10,0))
languageOptionMenu.grid(row= 6, column=1, columnspan=2, pady=(0,0)) 

#Center Frame Widgets
questionLabel.grid(row=1, column=1, columnspan= 4, padx=(10, 10), pady=(20, 10))

answer1Radio.grid(row=2, column=1, padx=(10,5), pady= 10)
answer2Radio.grid(row=2, column=2, padx=(10,5), pady= 10)
answer3Radio.grid(row=3, column=1, padx=(10,5))
answer4Radio.grid(row=3, column=2, padx=(10,5))

confirmButton.grid(row=2, column=3, rowspan=2, padx=5, pady= (10,0))

resultLabel.grid(row=4, column=1, columnspan= 3, padx=(10,5), pady=(15, 10))

#Right Frame Widgets
pointLabel.grid(row=1, column=1, padx=(10, 10), pady=(20, 10)) 
scoreLabel.grid(row=1, column=2, padx=(10, 10), pady=(20, 10))
startButton.grid(row=2, column=1, padx=10, pady=(10, 10)) 
finishButton.grid(row=2, column=2, padx=10, pady=(10, 10)) 
howToPlayButton.grid(row=4, column=1, columnspan=2,)


root.mainloop()