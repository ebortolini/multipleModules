import sys

from pathlib import Path
BASE_PATH = Path(__file__).parent.parent.parent
print (BASE_PATH)
sys.path.append(BASE_PATH._str)

from lib import Math

m = Math()
n1 = 2
n2 = 3
result = m.sumIntegers(n1,n2)

print ("The result of " + str(n1) + " + " + str(n2) + " is: " + str(result))