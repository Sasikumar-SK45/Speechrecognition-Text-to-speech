import speech_recognition as sr
import pyttsx3
# from pluginmanager.compat import read_file

# intitialize the recognizer
r = sr.Recognizer()

# Convert text to speech
def SpeakText(command):
     #initialize the engine
     engine = pyttsx3.init()
     engine.say(command)
     engine.runAndWait()

def InventoryPrice():

     # import mysql
     import pymysql as p
     # connecting to the database
     inventorymanagementdb = p.connect(host='localhost',user='root',password='2333',db='inventorymanagement')
     print("Succesfully Connected")

     # created a page
     mypage = inventorymanagementdb.cursor()

     # selected query
     q1 ='select price from products;'

     # execute the query
     mypage.execute(q1)

     # fetch the details from queries
     res = mypage.fetchall()

     # close db
     inventorymanagementdb.close()
     return res[0][0]

while(True):

     try:
          print("Please speak = ")
          # use the microphone as source for input.
          with sr.Microphone() as source2:

               r.adjust_for_ambient_noise(source2,duration=0.2)
               # listens for the user's input
               audio2 = r.listen(source2)

               # Using Google to Recognize the Voice
               MyText = r.recognize_google(audio2)
               MyText = MyText.lower()
               print("Did u said",MyText)
               SpeakText(MyText)

               if('stop' in MyText.lower()):
                    SpeakText("Thanks for using voice services Have a good Day")
                    break

               if('price' in MyText.lower()):
                    res = InventoryPrice()
                    var ="The price of the inventory is " + str(res) + "$"
                    SpeakText(var)
                    print(var)


               if('sports' in MyText.lower()):
                    fvar = open('Sports news.txt', 'r')
                    var = fvar.read()
                    SpeakText(var)
                    fvar.close()


               if('Movies' in MyText.lower()):
                    fvar = open('Movie.txt', 'r')
                    print("Connected Succesfully")
                    var = fvar.read()
                    SpeakText(var)
                    fvar.close()


               if('Politics' in MyText.lower()):
                    fvar = open('Politicial.txt', 'r')
                    var = fvar.read()
                    SpeakText(var)
                    fvar.close()


               if('Headlines' in MyText.lower()):
                    fvar = open('TodayHeadlines.txt', 'r')
                    var = fvar.read()
                    SpeakText(var)
                    fvar.close()



     except sr.RequestError as e:
          print("Could not request results; {0}".format(e))

     except sr.UnknownValueError:
          print("unknown error occurred")

