
class phone:
    def call(self):
        print("Phone's can make call.")

class AntinaPhone(phone):
    def seventysphone(self):
        print("Seventy's phones have anitna")

class keypad(AntinaPhone):
    def nokiaKeypad(self):
        print("Keypad phone can make call and play music without antina")


class smartphone(keypad):
    def playvideo(self):
        print("Keypad Phones can make call , play song and video without antina and kaypad")


sm = smartphone()
sm.seventysphone()
sm.nokiaKeypad()
sm.playvideo()