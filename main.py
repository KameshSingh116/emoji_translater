#Radhe Radhe
import demoji

choice='y'
while(choice=='y'):
         text=input("Enter you text with emojis:")
         output=demoji.findall(text)
         print(output)


         choice=input("Do you want to continue?:(y/n):")
         if(choice=='y'):
               continue
         else:
               break
         
         