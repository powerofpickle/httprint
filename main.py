import httprint
from time import sleep

httprint.init()
httprint.set_global_title("StatBot")

print("TEST")
print("TEST@@@")

for i in range(0, 100):
	print(i)
	sleep(1)

