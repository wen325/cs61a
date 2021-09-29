class Instructor:
    degree = "PhD (Magic)" # this is a class attribute
    def __init__(self, name):
        self.name = name # this is an instance attribute
    def lecture(self, topic):
        print("Today we're learning about " + topic)
dumbledore = Instructor("Dumbledore")

class Student:
    instructor = dumbledore
    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        ta.add_student(self)
    def attend_lecture(self, topic):
        Student.instructor.lecture(topic)
        if Student.instructor == dumbledore:
            print(Student.instructor.name + " is awesome!")
        else:
            print("I miss Dumbledore.")
        self.understanding += 1
        
    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class TeachingAssistant:
    def __init__(self, name):
        self.name = name
        self.students = {}
    def add_student(self, student):
        self.students[student.name] = student
    def assist(self, student):
        student.understanding += 1
        
# 1.2 Not finished        
class Email:
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        
class Mailman:
    def __init__(self):
        self.clients = {}
        
    def send(self, email):                        # not understand
        email.recipient_name.inbox += email  
                 
    def register_client(self, client):  #client is an object
        self.clients[client] = client.name
        
               
class Client:
    def __init__(self, mailman, name):
        self.inbox = []
        self.mailman = mailman
        self.name = name
        
    def compose(self, msg, recipient_name):      
        new = Email(msg,self.name,recipient_name)
        self.mailman.send(new)
        
    def receive(self, email):
        if self.name == email.recipient_name:
            self.inbox += email
            print("received!")
        else:
            print("This is not your email")
            
NTU_system = Mailman()
huawei = Client(NTU_system,"huawei")
iphone = Client(NTU_system,"iphone")
NTU_system.register_client(huawei)
NTU_system.register_client(iphone)

lunch = Email("GO for lunch?",huawei,iphone)
accept = Email("OK, let's go!", iphone,huawei)
deny = Email("Sorry, I'm busying",iphone,huawei)


# 2.1

class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)
        
class Dog(Pet):
    def __init__(self, name, owner):
        Pet.__init__(self, name, owner)
    def talk(self):
        print(self.name + ' says woof!')
        
class Cat(Pet):
    def __init__(self, name, owner, lives =9):
        Pet.__init__(self,name,owner)
        self.lives = lives
      
    def talk(self):
        """ A cat says meow! when asked to talk."""
        print(self.name + " says meow!")
        
    def lose_life(self):
        """A cat can only lose a life if they have at
        least one life. When lives reaches zero, 'is_alive'
        becomes False.
        """
        self.lives -=1
        if self.lives == 0:
            self.is_alive = False

# 2.2

class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    # def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        # no, inheritance
        # but the NoisyCat should creat as fox = NoisyCat("hellokitty", "Japan")
        
    def talk(self):
        """Repeat what a Cat says twice."""
        print(self.name + " says meow!")
        print(self.name + " says meow!")
        
fox = NoisyCat("hellokitty", "Japan")

# 2.3
class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4

class Yolo:
    motto = 0
    def __init__(self,num):
        self.motto = num
    def g(self,x):
        return x+self.motto