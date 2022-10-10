import time
import subprocess
subprocess.run(["sudo",'apt-get','-y','install','xterm'])
subprocess.run(['sudo', 'apt-get', '-y', 'install', 'gnome-terminal'])
subprocess.run(['clear']) 
print(r"""
  ______   ______  _____ ____    _   _    _  _____
 / ___\ \ / / __ )| ____|  _ \  | | | |  / \|_   _|
| |    \ V /|  _ \|  _| | |_) | | |_| | / _ \ | |
| |___  | | | |_) | |___|  _ <  |  _  |/ ___ \| |
 \____| |_| |____/|_____|_| \_\ |_| |_/_/   \_\_|

 ____   ___  _    _   _ _____ ___ ___  _   _ ____
/ ___| / _ \| |  | | | |_   _|_ _/ _ \| \ | / ___|
\___ \| | | | |  | | | | | |  | | | | |  \| \___ \
 ___) | |_| | |__| |_| | | |  | | |_| | |\  |___) |
|____/ \___/|_____\___/  |_| |___\___/|_| \_|____/

info@cyberhatsolutions.com
please follow our social media page's:
Instagram:	-----> https://www.instagram.com/cyberhatsolutions/
Facebook:	-----> https://m.facebook.com/cyberhatsolutions/
Linkdin:	-----> https://in.linkedin.com/company/cyberhatsolutions/
""")

if __name__=="__main__":

	code=input("Please type your ID-number:\n\n\t(~/cyberhatsolutions@CHS) $")
	a="7671"
	if code==a:
		print('\n')
		print("WELCOME")
		print("\n")
		print("HELLO STUDENTS,welcome to THE GREAT CYBER HAT HACKATHON .")
		print(r"""

 _____ _                                 _                _
|_   _| |__   ___    __ _ _ __ ___  __ _| |_    ___ _   _| |__   ___ _ __
  | | | '_ \ / _ \  / _` | '__/ _ \/ _` | __|  / __| | | | '_ \ / _ \ '__|
  | | | | | |  __/ | (_| | | |  __/ (_| | |_  | (__| |_| | |_) |  __/ |
  |_| |_| |_|\___|  \__, |_|  \___|\__,_|\__|  \___|\__, |_.__/ \___|_|
                    |___/                           |___/
 _           _     _                _         _   _
| |__   __ _| |_  | |__   __ _  ___| | ____ _| |_| |__   ___  _ __
| '_ \ / _` | __| | '_ \ / _` |/ __| |/ / _` | __| '_ \ / _ \| '_ \
| | | | (_| | |_  | | | | (_| | (__|   < (_| | |_| | | | (_) | | | |
|_| |_|\__,_|\__| |_| |_|\__,_|\___|_|\_\__,_|\__|_| |_|\___/|_| |_|




""")

		print('\n')
		print("Now you are entering in to the CTF challenge,")
		print('\n')
		outcome=input("This is a HACKATHON challenge, To start the HACKATHON type YES or Y: \n\n\t(~/cyberhatsolutions@CHS) $")
		while True:
			if outcome == 'y' or outcome=='Y' or outcome=='yes' or outcome=='YES':
				print("\n \n LIST OF CHALLENGES ARE:")
				print("""\n 1.BRUTE-FORCE \n 2.CRYPTOGRAPHY \n 3.EXPLOITATION \n 4.FORENSICS \n 5.OPEN-SOURCE INTELLIGENCE(OSINT) """)
				challenge=int(input("please enter the challenge number:\n\n\t(~/cyberhatsolutions@CHS) $"))


				if challenge==1:
					print("you are entering in to 'BRUTE-FORCE' challenge.")
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
					subprocess.run(["xterm","-e","bash","-c","cd brute;bash brute.sh; exec bash"])

				elif challenge==2:
					print("you are entering in to 'CRYPTOGRAPHY' challenge.")
					time.sleep(1)
					print("5.....")
					time.sleep(1)
					print("\t 4....")
					time.sleep(1)
					print('\t \t 3...')
					time.sleep(1)
					print('\t \t \t 2..')
					time.sleep(1)
					print('\t \t \t \t 1.')
					time.sleep(0.5)
					print("challenge has started")
					print("This is an one way hash format.")
					subprocess.run(["xterm",'-e','bash','-c','cd crypto;bash 1.sh; exec bash'])

				elif challenge==3:
					print("you are entering in to 'EXPLOITATION' challenge.")
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
					subprocess.run(["xterm",'-e','bash','-c','cd explo;bash explo.sh; exec bash'])

				elif challenge==4:
					print("you are entering in to 'FORENSICS' challenge.")
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
					subprocess.run(["xterm",'-e','bash','-c','cd foren;bash foren.sh; exec bash'])

				elif challenge==5:
					print("you are entering in to 'OSINT' challenge.")
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
					subprocess.run(["xterm",'-e','bash','-c','cd OSINT;bash osint.sh; exec bash'])
				else:
					subprocess.run(['clear'])
					print("\n \n \t \tplease enter a valid number:","can't you see that there is No option with",challenge)

			else:
				subprocess.run(['exit()'])
				print("you are not allowed into the CTF challenge.")

	elif code!=a:
		print("\n\nyour ID is Invalid")
		exit()



