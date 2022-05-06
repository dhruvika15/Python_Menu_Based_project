import os
import subprocess
import smtplib, ssl
import getpass

#os.system("tput setaf 2")
print("\t\t\t\tWelcome to my menu")
os.system("espeak-ng -v en+m1 'Welcome to my Menu' -s120")
print("\t\t\t\t------------------")
print()
print("Where do you wanna run your program?(local/remote):", end="")
os.system("espeak-ng -v en+m4 'Where do you wanna run your program?(local/remote):'")
myhost = input()

if myhost == "remote":
	remote_ip=input("Enter your remote host ip:")	
	os.system("espeak-ng -v en+m1 'Enter your remote host ip:' -s120")
while True:
	if myhost == "local":
		print("Choose any of the option below:")
		os.system("espeak-ng -v en+m1 'Choose any of the option below:' -s120")
		print("""
			Press 1: Linux
			Press 2: Data Structures and algorithms
			Press 3: Data Science
			Press 4: Docker
			""")
		#print("Enter your choice:", end="")
		#os.system("espeak-ng -v en+m1 'Enter your choice:' -s120")
		#ch = input()
		os.system("espeak-ng -v en+m4 'Enter your choice:'")
		ch = subprocess.getoutput("zenity --entry --title='Enter your choice:'")
		print(ch[93:])
		ch = ch[93:]
		os.system("clear")
		while True:
			if int(ch)==1:
				print("Linux \n")
				print("""
			Press 1: Basic Linux Commands
			Press 2: Funny Linux Commands
			Press 3: Sending email using python.
			Press 4: Setup your web server.
			Press 5: Main Menu""")
				print("Choose any of the option below:")
				os.system("espeak-ng -v en+m1 'Choose any of the option below:' -s120")
				l = input()
				if int(l)==1:
					print("Baisc Linux Commands \n")
					print("""
					Press 1: date
					Press 2: cal
					Press 3: ls
					Press 4: pwd
					Press 5: Main menu""")
					print("Enter your choice:",end="")
					os.system("espeak-ng -v en+m1 'Enter your choice:' -s120")
					x = input()
					if int(x)==1:
					
						os.system("date")
						os.system("espeak-ng -v en+f2 'date command executed' -s120")
					elif int(x)==2:
					
						os.system("cal")
						os.system("espeak-ng -v en+f2 'calendar command executed' -s120")
					elif int(x)==3:
					
						os.system("ls")
						os.system("espeak-ng -v en+f2 'list command executed' -s120")
					elif int(x)==4:
					
						os.system("pwd")
						os.system("espeak-ng -v en+f2 'pwd command executed' -s120")
					elif int(x)==5:
						os.system("espeak-ng -v en+f2 'You are going back to main menu' -s120")
						break
					else:
						os.system("espeak-ng -v en+f2 'exit command executed' -s120")
						exit()			
				elif int(l)== 2:	
					print("Funny Linux Command \n")
					print("Choose any of the option below:")
					os.system("espeak-ng -v en+m1 'Choose any of the option below:' -s120")
					print("""
					Press 1: sl
					Press 2: cowsay
					Press 3: cmatrix
					Press 4: banner
					Press 5: Main menu""")
					print("Enter your choice:",end="")
					os.system("espeak-ng -v en+m1 'Enter your choice:' -s120")
					x = input()
					if int(x)==1:
						os.system("espeak-ng -v en+f2 'sl command executed' -s120")
						os.system("sl")
					elif int(x)==2:
						os.system("espeak-ng -v en+f2 'cowsay command executed' -s120")
						print("Enter a String")
						xyz = input()
						os.system("cowsay {}".format(xyz))
						os.system("espeak-ng -v en+f2 '{}' -s120".format(xyz))
					elif int(x)==3:
						print("Press q to exit from cmatrix")
						os.system("espeak-ng -v en+f2 'cmatrix command executed' -s120")
						os.system("cmatrix")
					elif int(x)==4:
						os.system("espeak-ng -v en+f2 'banner command executed' -s120")
						print("Enter a String")
						abc = input()
						os.system("banner {}".format(abc))
						os.system("espeak-ng -v en+f2 '{}' -s120".format(abc))
					elif int(x)==5:
						os.system("espeak-ng -v en+f2 'You are going back to main menu' -s120")
						break
					else:
						os.system("espeak-ng -v en+f2 'exit command executed' -s120")
						exit()
				elif int(l)==3:
					os.system("clear")
					your_id = "blackwidow91477@gmail.com"
					passwd = "Blackwidow@91477"
					message = "Hello, How are you?"
					os.system("espeak-ng -v en+m4 'Enter receiver's mail-id:'")
					receiver_mail = input("Enter the receiver mail:")
					server = smtplib.SMTP_SSL("smtp.gmail.com",465)
					server.login(your_id,passwd)
					server.sendmail(your_id,receiver_mail,message)
					server.quit()
					print("Successfully sent")
					os.system("espeak-ng -v en+m1 'Successfully Sent' -s120")
					print("Press enter to continue...")
					input() 
				elif int(l)==4:
					os.system("systemctl start httpd")
					os.system("systemctl stop firewalld")
					print("Your IP is:")
					os.system("ifconfig enp0s3")
					os.system("espeak-ng -v en+m1 'Your web server has been setup now you can visit your website!' -s120")
					break
				elif int(l)==4:
					os.system("espeak-ng -v en+f2 'You are going back to main menu' -s120")
					break

			elif int(ch)==2:
				print("DSA \n")
				os.system("clear")
				print("Choose any of the below:")
				os.system("espeak-ng -v en+m1 'Choose any of the option below:' -s120")
				print("""
						Press 1: Main Menu
					""")
				print("Enter your choice:", end='')
				os.system("espeak-ng -v en+m1 'Enter your choice:' -s120")
				l = int(input())
				if l == 1:
					os.system("espeak-ng -v en+f2 'You are going back to main menu' -s120")
					break
			elif int(ch)==3:
				print("Data Science")
				print("Choose any of the option below:")
				os.system("espeak-ng -v en+m1 'Choose any of the option below:' -s120")
				print("""
					Press 1: Salary Prediction 
					Press 2: Computer Vision
					Press 3: View Your Live Sketch
					Press 4: Face Recognizer
					Press 5: Main Menu """)
				print("Enter your choice:",end="")
				os.system("espeak-ng -v en+m1 'Enter your choice:' -s120")
				x = int(input())
				if x == 1:
					os.system("python3 Salary_predict.py")
				if x == 2:
					os.system("python3 cv.py")
				if x == 3:
				    os.system("python3 live_sketch.py")
				if x == 4:
					os.system("python3 Face_recognizer.py Dhruvika")
				if x == 5:
					os.system("espeak-ng -v en+f2 'You are going back to main menu' -s120")
					break
			elif int(ch)==4:
				print("Docker")
				print("Choose any of the option below:")
				os.system("espeak-ng -v en+m1 'Choose any of the option below:' -s120")
				print("""
					Press 1: View Your Resume
					Press 2: Main Menu """)
				print("Enter your choice:",end="")
				os.system("espeak-ng -v en+m1 'Enter your choice:' -s120")
				x = int(input())
				if x == 1:
					os.system("python3 docker.py")
				if x == 2:
					break
			else:
				#print("Local Error")
				os.system("zenity --info --text='Local Error'")
				exit()
			os.system("espeak-ng -v en+m2 'Press any key to continue' -s120")
			input("Press enter to continue. .")
			os.system("clear")
	elif myhost == "remote":
		print("Choose any of the option below:")
		os.system("espeak-ng -v en+m1 'Choose any of the option below:' -s120")											
		print("""
			Press 1: Basic Linux Commands
			Press 2: Funny Linux Commands
			Press 3: Send an E-mail using Python""")
		#print("Enter your choice:", end="")
		#os.system("espeak-ng -v en+m1 'Enter your choice:' -s120")
		#ch = input()
		os.system("espeak-ng -v en+m4 'Enter your choice:'")
		ch = subprocess.getoutput("zenity --entry --title='Enter your choice:'")
		print(ch[93:])
		ch = int(ch[93:])
		os.system("clear")
		while True:
			if int(ch)==1:
				print("Choose any of the option below:")
				os.system("espeak-ng -v en+m1 'Choose any of the option below:' -s120")
				print("""
					Press 1: date
					Press 2: cal
					Press 3: ls
					Press 4: pwd
					Press 5: Main menu""")
				print("Enter your choice:",end="")
				os.system("espeak-ng -v en+m1 'Enter your choice:' -s120")
				x = input()
				if int(x)==1:
					os.system("espeak-ng -v en+f2 'date command executed' -s120")
					os.system("ssh {} date".format(remote_ip))
				elif int(x)==2:
					os.system("espeak-ng -v en+f2 'calendar command executed' -s120")
					os.system("ssh {} cal".format(remote_ip))
				elif int(x)==3:
					os.system("espeak-ng -v en+f2 'list command executed' -s120")
					os.system("ssh {} ls".format(remote_ip))
				elif int(x)==4:
					os.system("espeak-ng -v en+f2 'pwd command executed' -s120")
					os.system("ssh {} pwd".format(remote_ip))
				elif int(x)==5:
					os.system("espeak-ng -v en+f2 'You are going back to main menu' -s120")
					break
				else:
					os.system("espeak-ng -v en+f2 'exit command executed' -s120")
					exit()			
			elif int(ch)==2:
				print("Funny Linux Commands.")
				print("Choose any of the option below:")
				os.system("espeak-ng -v en+m1 'choose any of the option below:' -s120")
				print("""
					Press 1: sl
					Press 2: cowsay
					Press 3: cmatrix
					Press 4: banner
					Press 5: Main menu""")
				print("Enter your choice:",end="")
				os.system("espeak-ng -v en+m1 'Enter your choice:' -s120")
				x = input()
				if int(x)==1:
					os.system("espeak-ng -v en+f2 'sl command executed' -s120")
					os.system("ssh {} sl".format(remote_ip))
				elif int(x)==2:
					#os.system("espeak-ng -v en+f2 'cowsay command executed' -s120")			
					print("Enter a String")
					xyz = input()
					#os.system("cowsay {}".format(xyz))
					os.system("ssh {} cowsay {}".format(remote_ip,xyz))
					os.system("espeak-ng -v en+f2 '{}' -s120".format(xyz))
					
				elif int(x)==3:
					os.system("espeak-ng -v en+f2 'cmatrix command executed' -s120")
					print("Press q to exit from cmatrix")
					os.system("ssh {} cmatrix".format(remote_ip))
				elif int(x)==4:
					#os.system("espeak-ng -v en+f2 'banner command executed' -s120")
					print("Enter a String")
					abc = input()
					#os.system("banner {}".format(abc))
					os.system("ssh {} banner {}".format(remote_ip,abc))
					os.system("espeak-ng -v en+f2 '{}' -s120".format(abc))	
				elif int(x)==5:
					os.system("espeak-ng -v en+f2 'You are going back to main menu' -s120")
					break
				else:
					os.system("espeak-ng -v en+f2 'exit command executed' -s120")
					exit()
			elif int(ch)==3:
				while True:
					os.system("clear")
					print("Choose any of the below:")
					os.system("espeak-ng -v en+m1 'Choose any of the option below:' -s120")
					print(""" 
						Press 1: send-mail
						Press 2: exit
					""")
					print("Enter your choice:", end='')
					os.system("espeak-ng -v en+m1 'Enter your choice:' -s120")
					x = int(input())
					if x == 1:
						os.system("clear")
						your_id = "blackwidow91477@gmail.com"
						passwd = "Blackwidow@91477"
						message = "Hello, How are you?"
						os.system("espeak-ng -v en+m4 'Enter receiver's mail-id:'")
						receiver_mail = input("Enter the receiver mail:")
						server = smtplib.SMTP_SSL("smtp.gmail.com",465)
						server.login(your_id,passwd)
						server.sendmail(your_id,receiver_mail,message)
						server.quit()
						print("Successfully sent")
						os.system("espeak-ng -v en+m1 'Message  sent' -s120")
						print("Press enter to continue...")
						input() 
					else:
						exit()	
			
			else:
				#print("Remote Error")
				os.system("zenity --info --text='Remote Error'")
				exit()
			input("Press enter to continue. .")
			os.system("clear")
	else:
		#print("Wrong Inputs:")
		os.system("zenity --info --text='Wrong Inputs'")
		exit()
	input("Press enter to continue...")
	os.system("clear")
			
