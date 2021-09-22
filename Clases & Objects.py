class test:
    name=""
    age=0
    def print_name(self):
        print(self.name)

jordan=test()
jordan.name="jordan"
jordan.age=23


julia=test()
julia.name="julia"
julia.age=24

james=test()
james.name="james"
james.age=25

print(jordan.name)
james.print_name()

print("-----------------------------------------")

class test2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_name(self):
        print(self.name)
    def print_age(self):
        print(self.age)

juan = test2("juan",26)
juan.print_name()