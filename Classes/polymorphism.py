from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# When we call this method for different objects, it will run each object's individual draw() method.
# This is called polymorphism.
# To achieve polymorphism, we dont need a base class like UIControl because Python supports duck typing.
# Duck typing means that an operation does not formally specify the requirements that its operands have to
# meet, but just tries it out with what is given. In Java, the program will dont run unless we somehow indicate
# that these classes have draw() method(To achieve this we can use abstract classes or interfaces). However in Python
# we dont need to show that these classes have draw() method. If it runs at the runtime, there is no problem.
def draw(controls):
    for control in controls:
        control.draw()


textBox = TextBox()
ddl = DropDownList()

draw([ddl, textBox])
