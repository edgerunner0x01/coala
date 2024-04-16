import requests
import sys
URL : str = sys.argv[1]
def main():
    try:
        status_code=requests.get(URL).status_code
        print(f"[{status_code}] - {URL}")
    except Exception as E:
        pass
        #print(E)
if __name__=="__main__":
    main()