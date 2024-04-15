from rot import Rot
import sys
try:
    print(Rot(13).encrypt(sys.argv[1]))
except:
    print("[Error] No text to encrypt was given !")
