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

#Just like this we can give any emoji as the imput and it will simpy provide us with the name of the emoji.