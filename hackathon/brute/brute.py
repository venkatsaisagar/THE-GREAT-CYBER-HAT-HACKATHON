import subprocess
import time

if __name__=="__main__":

	req=input("Press ENTER to continue the challenge.")
	while True:
		if req=="" :
			subprocess.run(['clear'])
			print("Welcome to 'The Great cyber Hat Hackathon'.")
			print("This is the brute force challenge:")
			print(" \n\t\t 1. 'WIFI-HANDSHAKE BRUTE FORCE ATTACK / DICTIONARY ATTACK'.")
			print(" \n\t\t 2. 'WEB DIRECTORY BRUTE FORCE'.")
			flag=int(input("\n \n select the above challenge: \n\n\t(~/cyberhatsolutions@CHS) $"))

			if flag==1:
				print("you are entering in to 'DICTIONARY ATTACK.")
				time.sleep(1)
				print("5.....")
				time.sleep(1)
				print("\t 4....")
				time.sleep(1)
				print("\t \t 3...")
				time.sleep(1)
				print("\t \t \t 2..")
				time.sleep(1)
				print("\t \t \t \t 1.")
				time.sleep(0.5)
				print("challenge has started")
				subprocess.run(["xterm","-e","bash","-c","bash dicti.sh; exec bash"])

			elif flag==2:
				print("you are entering in to 'WEB DIRECTORY BRUTE FORCE ATTACK.")
				time.sleep(1)
				print("5.....")
				time.sleep(1)
				print("\t 4....")
				time.sleep(1)
				print("\t \t 3...")
				time.sleep(1)
				print("\t \t \t 2..")
				time.sleep(1)
				print("\t \t \t \t 1.")
				time.sleep(0.5)
				print("challenge has started")
				subprocess.run(["xterm","-e","bash","-c","cd brute;bash webdir.sh; exec bash"])
			else:
				print("<===== go back and start again.")

