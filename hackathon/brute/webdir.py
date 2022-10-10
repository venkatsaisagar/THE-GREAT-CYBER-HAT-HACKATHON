import time
import subprocess
subprocess.run(['clear'])
if __name__=="__main__":

	print("The first challenge of hackathon.")
	time.sleep(1)
	print("Please follow this steps carefully.")
	time.sleep(1)
	print("Make sure that your have a good internet connection.")
	time.sleep(1)
	print("To run the website, just type IP address of HACKATHON server machine in your kali-linux machine. ")
	time.sleep(1)
	print("\nYou can start attack on your kali-linux treminal machine by using any 'Web directory brute force tools'.")
	time.sleep(1)
	print("\n DO you need any help on how to perform a directory brute-force.")
	help=input("\n\n If yes type YES/Y if not type NO/N: \n\n\t\t(~/cyberhatsolutions@CHS) $")
	if help == 'y' or help=='Y' or help=='yes' or help=='YES':
		print("\nopen your 'FIREFOX' in kali-linux")
		print("\nType IP address of HACKATHON server machine in your kali-linux machine.")
		print("here the tool used is dirbuster")
		print("this is the following command used.")
		print("\n example:")
		print("\tdirb http://192.168.1.1 wordlist.txt")
		print("\nNow try working on the tool ")
		time.sleep(1)
		print("A new terminal is going to open now, remember the command and tool.")
		bf=input("Are you ready to perform the attack, type YES/Y: \n\n\t\t(~/cyberhatsolutions@CHS) $")
		if bf=='y' or bf=='yes' or bf=='YES' or bf=='Y' :
			time.sleep(2)
			subprocess.run(['gnome-terminal'])
		else:
			print("You are suspended.")

	else:
		print('\n\n\n\n:(',':(',':(')

