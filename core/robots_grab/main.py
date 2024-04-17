from requests import get
import sys
URL:str=sys.argv[1]
def filter(url:str) -> str:
    if url[len(url)-1] == "/":
        return url[:len(url)-1]
    else:
        return url
def main():
    try:
        req=get(f"{filter(URL)}/robots.txt")
        status_code=req.status_code
        if int(status_code) == 200:
            print(f"[{filter(URL)}/robots.txt]")
            print(req.text+"\n"+"====="*5+"\n")
    except:
        pass
if __name__=="__main__":
    main()