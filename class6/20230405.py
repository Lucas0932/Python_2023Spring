# 自我介紹
"""
class Person:
    # 建構式
    def __init__(self, name, age, favoriteFood):
        self.name = name
        self.age = age
        self.favoriteFood = favoriteFood

    # 實體方法(Instance Method)
    def introduce(self):
        print("我是" + self.name + "我今年" + str(self.age) + "歲，我最喜歡吃" + self.favoriteFood)
    # 實體方法(Instance Method)
    def shout(self, content):
        print("我大喊:「 "+ content+ "」")

# 建立物件
Lucas = Person("Lucas", 13, "牛排")
# 呼叫行為 1
Lucas.introduce()
# 呼叫行為 2
Lucas.shout("我喜歡打電動!")
"""
# 生病
"""
class Person:
    state = "healthy"
    # 實體方法(Instance Method)
    def getCold(self):  
        self.__class__.state = "sick"

Lucas = Person()
print("I am: "+ Person.state + "!")
Lucas.getCold()
print("It is cold now, I feel cold and I think now I am: "+ Person.state + "!")
"""
# 國家
"""
class Person:

    #建構式
    def __init__(self, haircolor, eyecolor):
        self.haircolor = haircolor
        self.eyecolor = eyecolor

    # 美國人
    @classmethod
    def american(cls):
        return cls("brown", "blue")

    # 台灣人
    @classmethod
    def taiwanese(cls):
        return cls("black", "black")
    
    # 實體方法(Instance Method)
    def introduce(self):
        print("My eyes is " + self.eyecolor + " and my hair is " + self.haircolor + "!")

Louie = Person.american()
Lucas = Person.taiwanese()
Lucas.introduce()
Louie.introduce()
"""
# 速率
"""
class Person:

    # 速率靜態方法
    @staticmethod
    def working_hours(hours):
        return hours
    
# 透過物件呼叫
Lucas = Person()
Lucas_work = Lucas.working_hours(8)
print("Working hours: ", Lucas_work)

# 透過類別呼叫
Louie = Person.working_hours(10)
print("Working hours: ", Louie)
"""