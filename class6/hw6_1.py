class Lesson:

    #建構式
    def __init__(self, teacher, time):
        self.teacher = teacher
        self.time = time

    # 美國人
    @classmethod
    def math(cls):
        return cls("Emma", "Monday")

    # 台灣人
    @classmethod
    def english(cls):
        return cls("Peter", "Thursday")
    
    # 實體方法(Instance Method)
    def introduce(self):
        print("This lesson is taught by " + self.teacher + " on " + self.time + ".")

Louie = Lesson.math()
Lucas = Lesson.english()
Louie.introduce()
Lucas.introduce()