
# Multiple Inheritance
class frontend:
    def design(self):
        print("Front Developer works on UI")

class backend:
    def functioning(self):
        print("Backend Developer works on functioning")

class devops( frontend , backend):
    def pipeline(self):
        print("Devops engineer makes Pipelines");


fullstack = devops()
fullstack.design()
fullstack.functioning()
fullstack.pipeline()
