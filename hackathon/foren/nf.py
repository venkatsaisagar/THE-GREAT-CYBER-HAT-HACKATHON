import subprocess
import time
subprocess.run(['clear'])
print("welocme to forensic challenge.")
print("In this challenge you have to find the user credentials, from Pcap file.")
print("Get the .CAP file from hackathon server machine.")
print("Use WIRESHARK tool")
print("DO you know which filter should be used.")
req=input("Do you need any help?, If yes type YES/Y. \n\n\t\t(~/cyberhatsolutions@CHS) $")
if req=='y' or req=='Y' or req=='yes' or req=='YES':
	print("The HINT is loading kindly wait for few minutes.")
	time.sleep(15)
	print("\n\tuse *** POST *** you will find the login credentials.")
	time.sleep(5)
	print("\nOpen a new terminal and run the wireshark with .CAP file.")
