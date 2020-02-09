import os
import datetime
#from playsound import playsound
#from Appkit import NSSound
import winsound
#winsound.PlaySound("RoosterCrowing.wav", winsound.SND_FILENAME)
def alarmClock():
     print("JM's Alarm Clock")
     now = datetime.datetime.now()
     print (" Current date and time : "+ now.strftime("%Y-%m-%d %H:%M:%S"))
     #print (now.strftime("%Y4 -%m-%d %H:%M:%S"))
     alarmN = int(input("Will you want to set 1 or 2 alarms? Please enter 1 or 2 respectively: "))
     if(alarmN == 1):
          alarmHour = int(input("What hour do you want to set the alarm for? "))
          alarmMinute = int(input("What minute do you want to set the alarm for? "))
          amPm = str(input("am or pm: ").lower())
          print("The alarm will go off at" , alarmHour ,":" , alarmMinute, amPm)
          if(amPm == "pm"):
               alarmHour = alarmHour + 12
               while(1==1):
                    if(alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
                         print("It is time")
                    #playsound('RoosterCrowing.mp3')
                         winsound.PlaySound("RoosterCrowing.wav", winsound.SND_FILENAME)
                         break
     elif(alarmN==2):
          choice = str(input("You can now set two alarms. Would you want to continue? (Y/N):").upper())
          if(choice == "N"):
               exit
          while (choice == "Y"):
               alarmHour = int(input("What hour do you want to set the alarm for? "))
               alarmMinute = int(input("What minute do you want to set the alarm for? "))
               amPm = str(input("am or pm: ").lower())
               print("The alarm will go off at" , alarmHour ,":" , alarmMinute, amPm)
               if(amPm == "pm"):
                    alarmHour = alarmHour + 12
               #break 
          while(1==1):
               if(alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
                    print("It is time")
                    #playsound('RoosterCrowing.mp3')
                    winsound.PlaySound("RoosterCrowing.wav", winsound.SND_FILENAME)
                    #break 
                       
     else:
          print("Enter the correct number of alarms to set")

alarmClock()
               
               
