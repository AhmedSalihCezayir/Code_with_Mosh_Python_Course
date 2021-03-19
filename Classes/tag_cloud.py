class TagCloud:

    # While naming instance/class attributes, if we starts the name by _ or __, that attribute becomes kinda private.
    # However, it is not Java-like private (i.e it is not that strict. We can still access these variables outside of
    # the class)
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    # This magic method helps us to use [] operator to get item by using key
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), -1)

    # This magic method helps us to use [] operator to set an item by using a key
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    # This magic method helps us to use len() function
    def __len__(self):
        return len(self.__tags)

    # This magic method makes our object iterable
    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()

cloud.add("Python")
cloud.add("python")
cloud.add("Python")

print(cloud.__tags)
print(cloud["python"])
print(cloud["java"])

cloud["c++"] = 20
print(len(cloud))

for i in cloud:
    print(i)
