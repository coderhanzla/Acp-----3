class Robot:
    name = "Jarvis"
    Owner = "Tony Stark"
   

    def introduction(self):
        print(" I am Jarvis and I am a Robot")

    def details(self):
        print("Hi! I am " , self.name)
        print("I am the Robot of" , self.Owner)

a= Robot()
a.introduction()        
a.details()