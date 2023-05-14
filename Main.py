import speech_recognition
import pyttsx3
from datetime import date, datetime

#Initialize
speech = pyttsx3.init()
hearing = speech_recognition.Recognizer()
robot =""
today = date.today()

day=today.strftime("%B %d, %Y")
now= datetime.now()
#Hear
with speech_recognition.Microphone() as mic:
    print("Ko nhon: I'm listening")
    audio = hearing.listen(mic)

print("Robot: ...")

try:
    you = hearing.recognize_google(audio)
except:
    you =""

print("You: " + you)

#Comprehend

if you == "":
    robot = "I can't fucking hear you"
elif "hello" in you:
    robot = "Hello mother fucker, Tuan Hiep"
elif"my name" in you:
    robot = "The stupid fluffy asshole"
elif "today" in you:
    robot = day
elif "time" in you:
    robot = now.strftime("%H hours %M minutes %S seconds")
elif "your father" in you:
    robot = "Your father is son of a bitch"
elif "know about data structure" in you:
    robot="A data structure is a way of storing and organizing data in the computer's memory so that it can be accessed and updated efficiently.There are different types of data structures, such as arrays, linked lists, stacks, queues, trees, graphs, etc. Each data structure has its own advantages and disadvantages, and is suitable for different problems and applications. Data structures can also be classified as static or dynamic, depending on whether their size is fixed or flexible at runtime. Some common operations that can be performed on data structures are searching, sorting, inserting, deleting, traversing, etc"
else:
    robot = "What the fuck are you talking about"

print("Robot: " + robot)

#Speak

speech.say(robot)
speech.runAndWait()