# This is example for For Loop !!
import sys

a = sys.argv[1]
for i in range(int(a)):
    print("Executing this line",a,"times !!")


teams = ["CSK", "RCB", "RR", "KKR", "MI","GT","LSG","DL"]
for team in teams:
    print(team,"This is a IPL team")
