import time
import subprocess
subprocess.run(['clear'])
if __name__=="__main__":

	print("The first challenge of hackathon.")
	time.sleep(1)
	print("please follow this steps carefully.")
	time.sleep(1)
	print("WIFI handsahake file will be there in the HACKATHON server machine.")
	time.sleep(1)
	print("You can download the handshake file from HACKATHON server machine.")
	time.sleep(1)
	print("\n\t OR")
	time.sleep(1)
	print("\nYou can start the attack on the server machine itself.")
	time.sleep(1)
	print("After getting the handsake file, crack the wifi password by Dictionary attack using wordlist file.")
	time.sleep(1)
	print("\n DO you need any help to generate a wordlist file.")
	help=input("\n\n If yes type YES/Y if not type NO/N: \n\n\t\t(~/cyberhatsolutions@CHS) $")
	if help == 'y' or help=='Y' or help=='yes' or help=='YES':
		print("lets create the wordlist file.")
		print("The tool I'm using here is crunch tool.")
		print("This is the following command to generate a wordlist file")
		print("\tcrunch minimun-len  maximum-len  characteristics  -o filename")
		min=input("\nEnter the minimum length of the wordlist: \n\n\t\t(~/cyberhatsolutions@CHS) $")
		max=input("\nEnter the maximum length of the wordlist: \n\n\t\t(~/cyberhatsolutions@CHS) $")
		char=input("\nSpecify the what are the characteristics should be in wordlist: \n\n\t\t(~/cyberhatsolutions@CHS) $")
		name=input("\nGive a name to the wordlist file: \n\n\t\t(~/cyberhatsolutions@CHS) $")
		subprocess.run(['crunch', min, max, char, '-o', name])
		subprocess.run(["cat", name])
		time.sleep(2)
		subprocess.run(['clear'])
		print("\n\n\t\tDon't worry wordlist file was saved in the name of",name)

	else:
		print('\nGreat goahead and crack the password.\n\n\n',':)',':)',':)')
