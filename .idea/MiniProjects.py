#OOPs in python, CLASS is a blueprint for creating objects, ab jaise ki kisi student ko school  me admission dene se pehle, school uska pura record taiyaar kartaa hain like his name, roll no ,age, blood grp ,address etc etc so here STUDENT is an object which is defined in class SCHOOL
#SYNTAX for creating class[ class class_name:], class name always starts with capital letter
from multiprocessing.spawn import set_executable


class Student:
    name = "karan"
#now we need to create OBJECTS for this class, lets see the syntax for object creation [ Object variable = class_name() ], these objects are k.a INSTANCE of a Class
s1 = Student() #YAHA pe automatically ek constructor Invoke ya execute kar diya gayaa, you will read about this below in line 19
print(s1.name)

s2 = Student()
print(s2.name)


class Car:
    color = "blue"

car1 = Car()
print(car1.color)

#lets see a function of class INIT func a.k.a CONSTRUCTOR which is invoked or executed during OBJECT CREATION. example dekhte hain,
#ALL CLASSES HAVE AN INIT Func WHICH IS ALWAYS EXECUTED WHEN THE OBJECT IS INITIATED, JESE in line 1 humne class STUDENT ke andar koi init func nhi likha, toh python automatically ek init func create karti hain aur execute bhi karaa deti hain
#aur Agar INIT func ya CONSTRUCTOR hume khud likhna ho toh kese likhenege?? lets see
class Student1:
    name = "karan"
    def __init__(self): #yaha par self means object ko refer ya indicate kar raha hain, apne aap(self) hi object calling ho jata hain when we will create object
        print(self) #see line 28's comment
        print("duniya humara: ")

s4 = Student1() #here yeh object apne aap hi call ho gayi using init self func.. now if u want to see what is self in the o/p,follow line no 25,which will explain that self is nothing but referring to the object which is created..

#agar hum alag alag students ko alag alag naam denaa chahte hain then hum constructor ko diff diff parameters bhi de sakte hain jaise ki
class Student2:
    def __init__(self,fullname,marks,age): #here self hi likhna zaroori nhi hain,tum kuch bhi likh sakte ho self ki jagah like xyz, udgd anything means u can give any name to ur object, here this constructor i k.a PARAMETERIZED CONSTRUCTOR
        self.name = fullname #yaha par self maane object s5 ko bulaaya gayaa and [name] ek variable declare kiya gayaa hain so jo bhi value line 41 me pass hogi wo 'name' me store ho jaayegi
        self.marks = marks
        self.age = age
        print("adding new students in the database: ")

s5 = Student2("karan",88,17) #object ke perenthesis mein we added a name or a value, so jo bhi value yaha par pass karenge wo line33  fullname ke andar aa jayegi
print(s5.name)  #here variable[name] is called as attributes where the datas are stored
print(s5.marks)
print(s5.age)
s6 = Student2("arjun",99,16)
print(s6.name)
print(s6.marks)
print(s6.age)

#class is basically  a collection of DATAS(ATTRIBUTES) and METHODS,attributes are like properties and METHODS Are basically functions that belong 2 objects
#for example ,lets make a method which says hi hello
class Welcome:
    def hello(self):  #Hello is the name of our method here,this is how we define a method in class, Class ke andar jo hum method likhte hain uske andar humesha humara 1st parameter must be SELF
        print("hi hello students")


x1 = Welcome()
print(x1.hello())

#Create a STUDENT CLASS that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average
#1 way to do this is coded below
class Studentmera:
    def __init__(self,fullname,phy,chem,maths):
        self.fullname = fullname
        self.physics = phy
        self.chemistry = chem
        self.mathematics = maths
        print("loading average: ")
        average = float((phy+chem+maths)/3)
        print(average)

A1 = Studentmera("shahid",85,67,91)
print(A1.fullname, A1.physics, A1.chemistry, A1.mathematics)
A2 = Studentmera("lipi",88,87,81)
print(A2.fullname, A2.physics, A2.chemistry, A2.mathematics)
A3 = Studentmera("mazumdar",33,77,90)
print(A3.fullname, A3.physics, A3.chemistry, A3.mathematics)

#WE can also code the above program by using LIST, lets see
class Studenthainbhai:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def calc_avg(self):
        sum=0

        for i in self.marks:
            sum
            sum+=i
            print("hi", self.name,"your average mark is: ",float(sum/3))

m1 = Studenthainbhai("tony",[89,99,94])
print(m1.name,m1.marks)
print(m1.calc_avg()) #if u type print here u get none in the o/p.so its better not to type print here
#in the near future if u want to change the name even, u can do so by:
m1.name = "ram"
m1.marks = [100,100,100]
print(m1.name,m1.marks)
print(m1.calc_avg()) #thus this way u can manipulate the datas here

#4 important concept in OOPS..ABSTRACTION, ENCAPSULATION, INHERITANCE, POLYMORPHISM
#(A)Let's see ABSTRACTION first which means hiding the implementation details of a class yaani class ke andar kis tarah chize exactly implement ho rahi hain wo aapne hide kar liya and aap user ko bas essential chize dikha rahe ho, unneccesary chizo ko chupana jo user ke liye important nhi hain
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False #in 3 o false ka matlab hain ki abhi  v gaadi band pari hain start nhi hui

    def start(self):
        self.acc = True
        self.clutch = True #abhi in dono True ka matlab hain ki car on ho gayi start ho  gayi
        print("car started")
c1 = Car()
c1.start() #now in th o/p bas CAR STARTED hi print huwa, upar jo code ke andar itne namuney kiye. wo user ko dikhaya nhi b/c its unneccessary. the only important thing was to show the o/p to the user. this is an example of ABSTRACTION

#(B) ENCAPSULATION - yaha par hum DATA and FUNCTIONS ka ek capsule banaate hain in a single unit(object),basically abhi tak hum encapsulation hi karte aa rahe hain, classes banayaa aur unke andar methods,attributes daal diya , this is nothing but encapsulation

#Create Account clas with 2 attributes - balance & account no. Create methods for debit, credit& printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    #debit_method
    def debit(self,amount): #jab bhi paisa debit hoga toh aapke account ke total paiso se minus ho jayega debited amt ,that is [self.balance-debited amount]
        self.balance-=amount
        print("Rs",amount,"was debited",".Left balance is: ",self.get_balance())
    #let's see credit method now
    def credit(self,amount2):
        self.balance+=amount2
        print("Rs",amount2,"was credited baby!","total balance is",self.balance)
    #now a function to print the total balance
    def get_balance(self): #yeh nhi likhne se bhi hoga, iske badle we can write the code written in line 129.same o/p dega and also carries the same meaning
        return self.balance #yeh func basically balance ko hi return kartaa hain

acc1 = Account(12000,456789)
print(acc1.balance,acc1.account_no)
acc1.debit(1000)
acc1.credit(2000)
acc1.credit(40000) #mahine ka 4 tarik hain and mera salary ghus gayaa, so new balance will be showed in the o/p

#del keyword = deletes object properties or the object itself
#chalo dekhte hain
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("akash")
print(s1.name)
#del s1
#print(s1.name) #error dikhayegaaaa ki s1 name not found, so isiliye comment kar diya abhi ke liye

#LETS look into INHERITANCE now,what is it?? - vvi and easy - like we inherit features from our parents, similarly jab hum ek generation of class se dusri generation of class me chizein pass karenge toh isey hum inheritance kehte hain, when one CLASS derives the methods and properties of another class, its called inheritance,lets see with an example
class Caragain: #Caragain is the parent class
    @staticmethod   #now, here staticmethod is a decorator and iska kya kaam hain? so basically kisi bhi class ke andar when we define or write down a function then we HAVE to give SELF parameter but SELF tabhi dena chaiye jab hum OBJECTS CREATE karte hain ,ab is 153 wale line me we aren't creating objects, we are just printing CAR STARTED,like we could also just print hello, so isiliye self nhi likha and without decorator agar maine self NHI LIKHA then error dikhayega, so i wrote decorator ..
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
class Toyotacar(Caragain): #here toyotacar is the child class.
    def __init__(self,name):
        self.name = name

c1 =Toyotacar("fortuner")
print(c1.name)
print(c1.start())
print(c1.stop())

#now lets see some types of INHERITANCE..
# 1. SINGLE INHERITANCE - Here,there's only one Parent class/base class and one CHild class derived from the base class, the above toyota wala program is an example of SINGLE INHERITANCE
# 2. MULTI LEVEL INHERITANCE- Here, Base class -> derived class1 -> another derived class from the previous derived class which has the properties of both [base class and derived class1]
class Gaadi:
    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class Maruticar(Gaadi): #this is now a parent class for the class below(Ciaz)
    def __init__(self,brand):
        self.brandname = brand

class Ciaz(Maruticar): #this derived child class has the features of both the above classes
    def __init__(self, enginetype):
        self.engine = enginetype

c2 = Ciaz("petrol")
print(c2.engine)
c2 = Maruticar("ciaz")
print(c2.brandname)
print(c2.color)
print(c2.stop())

#3. MULTIPLE INHERITANCE
class A:
    var1 = "welcome to A"
class B:
    var2 = "welcome to B"
class C(A,B): #the derived class has inherited the properties from two PARENT CLASSES or BASE CLASSES [class A, class B]
    var3 = "welcome to C"
    def __init__(self,greetings):
        self.gestures = greetings

v1 = C("salaam,namastey") #we made an object v1 for Class C

print(v1.gestures, v1.var1,"and", v1.var2,"and also",v1.var3) #u saw? here we can access both the parent classes' data, where A and B are parents classes

#lets see now SUPER Method() which is used to acces methods of the parent class,lets see this with an example:.
class M:
    def __init__(self,enginetype):
        self.engine = enginetype

    @staticmethod
    def greetings():
        print("congratulations on ur new purchase!")
    @staticmethod
    def hopes():
        print("wish that u come soon for another purchase!")

class N(M):
    def __init__(self, brand,enginetype): #now, inside the perenthesis if i write enginetype, then this would be classN's attribute but i want to access the enginetype of Class M, so for this we can use SUPER method,in case if we dont write super method in line 228 , then this enginetype would be considered as an attribute of class N, but humein toh upar waale class M ka enginetype chaiye
        self.name = brand
        super().__init__("petrol") #thus using super method, we accessed the Parent class M's init function


o1 = N("FORD","DIESEL")
print(o1.name,o1.engine)
o1 = M("petrol engine")
print(o1.engine)
print(o1.greetings())
print(o1.hopes())

#CLASS METHODS - Now here we made a class with name attribute(CLASS ATTRIBUTE) as lippi in line 242 and 243, then we wanted to change this name to something else, so we defined a function to change the name,HERE we are trying ki object ki function se Class ke andar jo name ka value hain usey change karu
#but the name in line 245 is a parameter for func CHANGENAME where Self(d1) created a new attribute (name) which is different from the name in line 243, but humein toh CLASS attribute Lippi ko change karna hain


class Name:
    name = "Lippi"

    def changeName(self,name):
        self.nameNew = name

d1 = Name()
d1.changeName("shahid")
print(d1.nameNew) #yaha par name change ho gayaa in the o/p because object (d1) ko banaakar function me  input ko deke we got instantaneous output name(line 245 wala name ki baat kar raha hoon)
print(Name.name) #u can see it here that ki class ke andar name change NAHii huwa, same to same reh gyaa..but humein object ki function CHANGENAME ko use karke line 243 wale name jo Class ke andar hain, us name ke value ko change karnaa hain..ab kaise karein??

#lets see, we can use a method name [@classmethod]...thus syntax is in line 257 258 259.lets see in the code
class Name:
    name = "anonymous"

    @classmethod
    def changeName(cls,name): #line 257 and 258 are SYNTAX for class method, instead of self now the parameter will be CLS
        cls.name = name #ab ye change seedha directly mere class Name me hone wala hain

g1 = Name()
print(Name.name) #this line will give us the original o/p from the line 255,unchanged
print(g1.changeName("lipishahid"))
print(g1.name)
print(Name.name) #as soon as the object calls the function CHANGENAME to change the name,then value of name is also changed from the main Class above, so now see the o/p for this line, u will see the o/p for this line is same as passed in the argument for func NAMECHANGE when our object g1 called the func NAMECHANGE

#Lets see PROPERTY Decorator - we use it in the class to use the method/functions as a property, like for example we made a class program which will calc the percentage of marks for 3 subjects and kal ko her/his paper was rechecked and in one of the subs his marks were decreased then when we change the marks of that particular sub in the program and calc the percentage, then the program will give the same PREVIOUS PERCENTAGE, not the updated % where one of his subs' marks was decreased
#then usi func ko hum property banaa dete hain, then with changing values , percentage bhi change hota rahegaa
class StudentBhosdk:

    def __init__(self,phy,chem,maths):
        self.physics = phy
        self.chemistry = chem
        self.mathematics = maths
        self.percentage = str((self.physics+self.chemistry+self.mathematics)/3) + "%"

stu1 = StudentBhosdk(80,80,80)
print(stu1.mathematics)
print(stu1.percentage)
#kal ko ab maan lo physics ka marks maine change karke 85 rakh diya
stu1.physics = 85 #so abhi if i calc the percentage answer must be 85+80+80/3, but o/p will be the old values/3 maane 80+80+80/3, so here we will need property decorator
print(stu1.percentage) #wahi 80% hi print hoga

#so now lets use property n see how it works in calculating percentage method
class StudentBhosdk:

    def __init__(self,phy,chem,maths):
        self.physics = phy
        self.chemistry = chem
        self.mathematics = maths

    @property  #thus this will help the func calc_percent to carry operation with the updated present values
    def calc_percent(self):
        return str((self.physics+self.chemistry+self.mathematics)/3) + "%"

stu2 = StudentBhosdk(90,90,90)
print(stu2.calc_percent)
#lets change the maths mark now
stu2.mathematics = 80 #now lets calc the percentage
print(stu2.calc_percent) #this wil give the updated percentage taking the changed maths mark as input and the other two subjects' marks also as i/p


#2. practising The same program again with @property decorator
class Bachhe:
    def __init__(self,eng,sst,hindi):
        self.english = eng
        self.socialstudies = sst
        self.hindiB = hindi

    @property
    def calc_avg(self):
        return str((self.english+self.socialstudies+self.hindiB)/3) + "%"

bach1 = Bachhe(80,80,80)
print(bach1.calc_avg)
bach1.socialstudies = 90
print(bach1.calc_avg)
bach1.english = 90
bach1.hindiB = 90
print(bach1.calc_avg)

#Lets look into POLYMORPHISM now where POLY means MANY and MORPH means FORMS..Best example of it is OPERATOR OVERLOADING...LIKE lets take the example of "+" operator

print(1+2) #here 1 and 2 are objects of class int, so Class int has already defined the + operator in python which does the work of adding 2 integers or float etc etc nos
print("shahid" + "lippi") #here shahid and lipi are objects of class String and class str has already defined + operator in python which will concetanate 2 strings or more
print([1,2,3] + [4,5,6]) #where 2 lists are objects of Class list and class list has already defined +operator in python which does the work of merging 2 or more lists
#so basically here the same operator(+) has different meaning according 2 the context, since just this one (+) operator has multiple functions according to the classes(int,str,list) etc etc, so this is k.a OPERATOR OVERLOADING

#Lets look into DUNDER functions now where we can ourselves define an operator like our + operator, underscore underscore are used in dunder funcs..
#lets make a program for adding 2 complex nos.. like[ 4i + 3j] + [1i + 3j] = [5i + 6j] where 5i is the real part and 6j is the img part, but our + operator cant add these complex nos..so here we will use dunder funcs..let's see
class ComplexNos:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showComplexNo(self): #i just want to see my complex no in the o/p
        print(self.real,"i","+",self.img,"j")

r1 = ComplexNos(4,8)
r2 = ComplexNos(5,2)
print(r1.showComplexNo())
print(r2.showComplexNo())

#now i want to add the above 2 complex nos , so for this lets understand the phenomenon of DUNDER func by writing the program below:
class Complex:
    def __init__(self, realMan, imgMan):
        self.realMan = realMan
        self.imgMan = imgMan


    def showNowMyComplexNo(self):
        print(self.realMan,"i","+",self.imgMan,"j")

    def __add__(self,num2): #here we used or DUNDER func ADD with 2 leading underscores which will add the real part and img part separately, in the same way we can subtract 2 complex nos using [_sub__]
        newRealMan = self.realMan + num2.realMan
        newImgMan = self.imgMan + num2.imgMan
        return Complex(newRealMan,newImgMan)

z1 = Complex(2,4)
print(z1.showNowMyComplexNo())
z2 = Complex(4,7)
print(z2.showNowMyComplexNo())
z3 = z1 + z2  #here instead of writing functions and calling funcs through objects we could just directly use + operator to add real part and img part separately just b/c of the dunder function used in line 353
print(z3.showNowMyComplexNo())

#LETS DO SOME PRACTISE QUESTION..
#Q1). DEFINE A CIRCLE Class to create a circle with radius r using the constructor. Define an Area()method of the class which calculates the area of the circle
#define a perimeter() method of the class which allows u 2 calc the perimeter of the circle

class Circle:
    def __init__(self,radius):
        self.radius = radius
        print("circle is created with radius", self.radius, "m")

    def calc_area(self):
        print("Area of the circle is: ",3.14 * self.radius * self.radius,"m^2")

    def perimeter(self):
        print("Perimeter of a circle is:",2 * 3.14 * self.radius,"m")

i1 = Circle(4)
print(i1.radius)
print(i1.calc_area())
print(i1.perimeter())

#Q2). Define an EMPLOYEE CLASS with attributes role, department & salary. This class also has a showDetails() method.Create Engineer Class that inherits properties from EMPLOYEE & has additional attributes: name & age
class Employee:
    def __init__(self,role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        return self.role,self.dept,self.salary

e1 = Employee("engg","backend",40000)
print(e1.showDetails())
e2 = Employee("dr","anatomy",78000)
print(e2.showDetails())


#doing the second part of the above program
class EmployeeMan:
    def __init__(self,role1, dept1, salary1):
        self.role1 = role1
        self.dept1 = dept1
        self.salary1 = salary1

    def showDetails(self):
        return self.role1,self.dept1,self.salary1

class Engineer(EmployeeMan):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("ENGINEER","IT",78000)


u1 = Engineer("akash", 28)
print(u1.name,u1.age)
print(u1.showDetails())


#Q3). Create a class called ORDER which stores items and its price. Use DUNDER (greater __gt__)func to convey that: order 1 > order 2 if the price of order1 > price of order2
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

v1 = Order("mango",100)
v2 = Order("potato", 80)

print(v1>v2) #this will return TRUE in the o/p..haan aur agar __gt__ func use nhi kiya hota humne and gt func ko use kiye bina 436 wala line likh dete toh pakkaaa error ata but 436 wala line easily likh paaye b/c of gt func
