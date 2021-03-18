import sys

print(sys.argv)

pgname = sys.argv[0] #### name of program being executed
filename = sys.argv[1] ### First argument

userinput = input("Please which date for processing log --- ")
print(userinput)
print(type(userinput))

from datetime import datetime as dt

try:
    dateuser = dt.strptime(userinput,'%Y-%m-%d')
except:
    print("Please enter date in YYYY-MM-DD");
    exit(0)
    
print("Hello" + dateuser.strftime('%Y-%b-%d') ) 