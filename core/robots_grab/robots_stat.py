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
        status_code=get(f"{filter(URL)}/robots.txt").status_code
        print(f"[{status_code}] - {filter(URL)}/robots.txt")
    except:
        pass
if __name__=="__main__":
    main()