
#single Inheritance

class Device:
    def power_on(self):
        print("Device is now ON.")

class Phone(Device):
    def call(self):
        print("Placing a call...")

myphone = Phone()
myphone.power_on()
myphone.call()