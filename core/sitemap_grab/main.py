from requests import get
import sys
URL:str=sys.argv[1]
HEADERS={"Accept": "xml,*/*" ,
         "Accept-Language":"en-US,en",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
def filter(url:str) -> str:
    if url[len(url)-1] == "/":
        return url[:len(url)-1]
    else:
        return url
def main():
    try:
        req=get(f"{filter(URL)}/sitemap.xml",headers=HEADERS)
        status_code=req.status_code
        if int(status_code) == 200:
            print(f"[{filter(URL)}/sitemap.xml]")
            print(req.text+"\n"+"====="*5+"\n")
    except:
        pass
if __name__=="__main__":
    main()