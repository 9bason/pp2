import re

N = int(input())

for i in range(N):
    name, email = input().split()
    pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern, email)):
        print(name,email)





import re
class Main():
    def __init__(self):
        self.n = int(input())
        for i in range(self.n):
            self.s = input()
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))
if __name__ == '__main__':
 obj = Main()






 import re

N = int(input())

for i in range(N):
    number = input()
    if(len(number)==10 and number.isdigit()):
        output = re.findall(r"^[789]\d{9}$",number)
        if(len(output)==1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")




string = "100,000,000.000"

regex_pattern = r"[,.]"

import re
print("\n".join(re.split(regex_pattern, string)))




import re

string = input()
substring = input()

pattern = re.compile(substring)
match = pattern.search(string)

if not match: 
    print('(-1, -1)')
    
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(string, match.start() + 1)