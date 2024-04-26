#Imports
import os

#Class Screen
class Screen:
    def __init__(self):
        deafultline=""
        self.lines=[];
    def clear():
        os.system('cls');
#Class Level
class Level:
    def __init__(self):
        self.Position=0;
        self.Values=[0, 0, 0, 0];
    def setColor(self,x):
        self.Values[self.Position]+=x;
        if self.Values[self.Position] >8:
            self.Values[self.Position]=0;
        if self.Values[self.Position] <0:
            self.Values[self.Position]=8;
    
    def ChangePosition(self,x):
        self.Position+=x;
        if self.Position<4:
            self.Position=0;
        if self.Position<0:
            self.Position=4