#polymorphism
class pycharm:
    def execute(self):
        print("compiling")
        print("running")
class vscode:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("running")        
class laptop:
    def code(self, ide):
        ide.execute()
ide=pycharm()
lap1 = laptop()
lap1.code(ide)    
# if there is a method i no need which class it is we a that method this is polymorphism duck typing(walk like a duck, swim like a duck simplily it is a duck)    