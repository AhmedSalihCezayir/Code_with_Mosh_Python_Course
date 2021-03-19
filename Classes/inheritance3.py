# We can extend built-in types
class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())


# This method just extends built-in list class' append method
class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")
print(list)
