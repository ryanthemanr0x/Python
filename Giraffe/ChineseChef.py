#New Class
from Chef import Chef

# Link new class to existing class
class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The chef makes fried rice")

    def make_special_dish(self):
       print("The chef makes Orange Chicken")