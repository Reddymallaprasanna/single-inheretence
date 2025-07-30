class person:
    def info(self):
        print("I am a Student")
class student(person):
    def study(self):
        print("The Student is studying")
s=student()
s.info()
s.study()