import sys
from . import init


def readstdin():
	num = 0
	while True:
		text = sys.stdin.readline()
		if text != "":
			print(text, end='')

if __name__ == '__main__':
	init()
	readstdin()



	
