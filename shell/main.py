import validators

class Shell:
    Commands=["emails","comments"]
    def __init__(self,no:int=0):
        self.no=no
        self.target:str=None
        
    def Run(self):
        while 1:
            prompt=str(input("> ")).replace(" ","")
            if(prompt in Shell.Commands):
                print(prompt)
            else:
                print(0)



    def Set_Target(self):
        try:
            self.target:str=str(input("[*] Set Target : "))
            if validators.url(self.target):
                print(f"[+] Target is set to '{self.target}' Successfully ")
            else:
                print("[!] Target should be a URL ")
        except Exception as E:
            print(E)
    
    def Help(self):
        pass

if __name__=="__main__":
    Shell().Run()
