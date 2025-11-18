# from dotenv import load_dotenv
# import os

# load_dotenv()
# my_variable = os.getenv("MY_KEY")

# print(my_variable)


# class cat:
#     # pass
#     tail = True
#     name = "default"
#     color = "black"

#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#         # print("создание объекта")

#     def run(self):
#         print(f"{self.color} кошка бежит")


# cat1 = cat(name="мурка", color="black")
# cat2 = cat(name="пухля", color="white")

# cat1.tail = True  # отребут(переменная)
# cat1.run()  # метод
# print(cat1.name, cat1.color, cat1.tail)
# print(cat2.name, cat2.color)


# def main():
#     print("Hello from hello!")

# name = "tom"

# if __name__ == "__main__":
#     main()


# class Npc:
#     name = "anonymus"
#     body_color = "black"
#     hp = 100

#     def __init__(self, name, color, hp):
#         self.hp = hp
#         self.name = name
#         self.body_colorcolor = color

#     def __del__(self):
#         print("удаление персонажа")

#     def get_damage(self, damage):
#         self.hp -= damage
#         # print("вы получили -12 урона")

#     def regenerate(self, regenerate):
#         self.hp += regenerate
#         # print("вы получили +5 hp")


# steve_npc = Npc(name="steve", color="black", hp=100)
# steve_npc.get_damage(20)
# # print(steve_npc.hp)

# steve_npc.regenerate(5)
# # print(steve_npc.hp)


class person:

    def __init__(self, name, age):
        self.__user_name = name
        self.__user_age = age

    def print_person(self):
        print(f"имя:{self.__user_name}, возраст:{self.__user_age}")

    @property
    def age(self):
        return self.__user_age

    @age.setter
    def age(self, age):
        # def set_age(self, age):
        if 0 < age and age < 100:
            self.__user_age = age
        else:
            print("недопустимый возраст")

    # def get_age(self):
    #     return self.__user_age


person_tom = person("tom", 37)

print(person_tom.age)
person_tom.age = 19
# для изменения возраста нужно изменить места, принт должен быть внизу
print(person_tom.age)


# print(person_tom.get_age())
# person_tom.set_age(76)

# person_tom.__user_age = -12
# person_tom.print_person()
