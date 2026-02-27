# 1. A class property is a property that belongs to the class rather than an instance of the class. 
# It can be accessed and modified without creating an instance of the class.


# 2. A Class method is a method that is bound to the class itself.




#3.
class Student:
    def __init__(self, name, age, grade_level, student_id):
        
        self.name = name  
        self.age = age    
        self.grade_level = grade_level 
        self.student_id = student_id 
        self.gpa = 0.0
    def getinfo(self):
        
     
    
        return f"{self.name} (ID: {self.student_id}) is {self.age} years old and in grade {self.grade_level} with a GPA of {self.gpa:.2f}."
    def setgpa(self, new_gpa):
        
       
        if 0.0 <= new_gpa <= 4.0:
            self.gpa = new_gpa
            return f"GPA updated to {self.gpa:.2f} for {self.name}."
        else:
            return "Invalid GPA"

student1 = Student("Alice", 16, 11, "S12345")
print(student1.get_info()) 
print(student1.set_gpa(3.8))
print(student1.get_info()) 

# 4.
class GameCharacter:
   
    def __init__(self, name, character_class, health, attack_power):
       
        self.name = name  
        self.character_class = character_class  
        self.health = health  
        self.attack_power = attack_power 
        self.is_alive = True
    def attack(self, target):
       
        if self.is_alive:
            print(f"[{self.name}] attacks [{target.name}] with {self.attack_power} damage!")
            target.take_damage(self.attack_power)
        else:
            print(f"[{self.name}] is defeated and cannot attack.")
    def takedamage(self, damage_amount):
        
        self.health -= damage_amount
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            print(f"[{self.name}] has been defeated!")
        else:
            print(f"[{self.name}] takes {damage_amount} damage Remaining health: {self.health}.")
    def displaystatus(self):
    
        status = "Alive" if self.is_alive else "Defeated"
        print(f"--- {self.name} Status ---")
        print(f"Class: {self.character_class}")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Status: {status}\n")

player1 = GameCharacter("Jay", "Warrior", 100, 15)
player2 = GameCharacter("Xen", "Mage", 75, 20)

player1.displaystatus()
player2.displaystatus()

player1.attack(player2)
player2.attack(player1)

player1.displaystatus()
player2.displaystatus()
