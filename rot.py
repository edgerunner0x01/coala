class Rot:
    def __init__(self,key):
        self.key=int(key)
    def encrypt(self,message):
        enc=""
        for i in message:
            if ord(i) >= 65 and ord(i) <= 90:
                if ord(i)+self.key <= 90:
                    enc=enc+str(chr(ord(i)+self.key))
                else:
                    enc=enc+str(chr(64 + ord(i)+self.key - 90))
                    
            elif ord(i) >= 97 and ord(i) <= 122:      
                if ord(i)+self.key <= 122:
                    enc=enc+str(chr(ord(i)+self.key))
                else:
                    enc=enc+str(chr(96 + ord(i)+self.key - 122))
            else:
                enc=enc+str(chr(ord(i)))
        return enc
    
    def decrypt(self,message):
        dec=""
        for i in message:
            if ord(i) >= 65 and ord(i) <= 90:
                if ord(i)+26-self.key <= 90:
                    dec=dec+str(chr(ord(i)+26-self.key))
                else:
                    dec=dec+str(chr(64 + ord(i)+26-self.key - 90))
                    
            elif ord(i) >= 97 and ord(i) <= 122:      
                if ord(i)+26-self.key <= 122:
                    dec=dec+str(chr(ord(i)+26-self.key))
                else:
                    dec=dec+str(chr(96 + ord(i)+26-self.key - 122))
            else:
                dec=dec+str(chr(ord(i)))
        return dec
