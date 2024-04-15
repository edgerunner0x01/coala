import rot
def main():
    with open("./encrypted_urls.txt" ,"r") as f:
        for i in f.readlines():
            url=rot.Rot(13).decrypt(i).strip("\n")
            print(url.replace("https://",""))
if __name__=="__main__":
    try:
        main()
    except Exception as E:
        print("Error: "+str(E))
