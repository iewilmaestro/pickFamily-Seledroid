import os, sys, time, json
from urllib.parse import urlparse
from seledroid import webdriver
from seledroid.webdriver.common.by import By

title = "pickFamily"
versi = "1.0.4"
youtube = "https://youtube.com/@iewil"

#
# NOTED
# MENAMBAH URL /HOST
# HARUS MENGHAPUS OUTPUT.JSON
#

hosts = [
"https://litepick.io/",
"https://tronpick.io/",
"https://bnbpick.io/",
"https://tonpick.game/"
]

# Fungsi
# Cooldown tmr in second
def timer(tmr):
	timr = time.time() + tmr
	sym = [' ─ ', ' / ', ' │ ', ' \\ ']
	a = 0
	while True:
		a += 1
		res = timr - time.time()
		if res < 1:
			break
		print(sym[a % 4] + str(int(res / 3600)) +  ":" + str(int((res % 3600) / 60)) + ":" + str(int(res % 60)), end="\r")
		time.sleep(0.1)

# Banner
def Ban():
	# Bersihkan layar
	os.system("cls" if os.name == "nt" else "clear")
	print(" Scrypt by iewil ")
	print(" "+title + " "+ versi)
	print('─'*50)

# Delay
def delay():
	time.sleep(3)

# line /garis batas
def line():
	print('─'*50)
	
# Fungsi Seledroid get Element by ID
def element_ready(element_id):
	try:
		element = driver.find_element(By.ID, element_id)
		
		if(element):
			#print("element ditemukan")
			return True
		else:
			return False
	except Exception as e:
		#print(f"Error: {e}")
		return False
		
# Fungsi Seledroid get Element by Name
def is_turnstile_solved():
	try:
		captcha_input = driver.find_element(By.NAME, "cf-turnstile-response")
		captcha_value = captcha_input.get_attribute("value")
		
		# menunggu turnstile di selesaikan
		if captcha_value and captcha_value != "":
			return True
		else:
			return False
	except Exception as e:
		#print(f"Error: {e}")
		return False


# Nama file JSON
json_file = "output.json"

# Periksa apakah file JSON sudah ada
if os.path.exists(json_file):
	# Baca file JSON jika ada
	with open(json_file, "r") as file:
		data = json.load(file)
else:
	# Buat struktur data awal jika file tidak ada
	data = {"data": [{"host": host} for host in hosts]}
	
# Tambahkan atau perbarui username dan password
for item in data["data"]:
	# Periksa apakah data sudah ada
	if "username" in item and "password" in item:
		print(f"Data untuk host {item['host']} sudah ada, melewati...")
	else:
		print(f"Konfigurasi untuk host: {item['host']}")
		email = input("Input Email: ")
		password = input("Input Password: ")
		item["username"] = email
		item["password"] = password
		
# Simpan data ke file JSON
with open(json_file, "w") as file: #write
	json.dump(data, file, indent=4)

with open(json_file, "r") as file: #read
	data = json.load(file)

Ban()
while(1):
	# Cek File JSON
	for user in data["data"]:
		
		host = user["host"]
		# Set Email & Password
		set_email = user["username"]
		set_password = user["password"]
		
		print(host)
		
		# Membuka Chrome Seledroid
		driver = webdriver.Chrome()
		delay()
		
		# Direct ke halaman login
		driver.get(host + "login.php")
		
		# Nunggu Clodpler
		# Cek elemen user_email sudah ada atau belum
		while not element_ready("user_email"):
			time.sleep(10)
		
		# Jika element sudah ada
		# Menentukan lokasi yang akan kita isi Username & Password
		email = driver.find_element(By.ID,"user_email")
		password = driver.find_element(By.ID,"password")
		
		try:
			# mengisi Element Username & Password
			email.send_text(set_email)
			password.send_text(set_password)
		except:
			# Jika pengisian Gagal
			# Chrome kita close & berhenti
			# Karena mungkin metode sudah ganti
			# Kalo di lanjut ke BAN
			driver.close()
			exit()
		
		# menunggu Turnstile di halaman Login
		while not is_turnstile_solved():
			time.sleep(5)
		delay()
		# Menentukan Element tombol Login
		login_button = driver.find_element(By.ID, "process_login")
		# Klik tombol login
		login_button.click()
		delay()
		
		
		# Direct ke halaman Faucet
		driver.get(host + "faucet.php")
		
		# menunggu Turnstile di halaman Faucet
		while not is_turnstile_solved():
			time.sleep(3)
		delay()
		
		# Menentukan Element tombol Claim
		claim_button = driver.find_element(By.ID, "process_claim_hourly_faucet")
		
		# Klik tombol claim
		claim_button.click()
		time.sleep(5)
		
		# Mencoba
		try:
			# Element Balance
			balance = driver.find_element_by_css_selector(".top_balance .user_balance")
			print(balance)
			line()
		except Exception as e:
			print(f"Error: {e}")
		
		# Menutup Chrome srledroid
		driver.close()
		delay()
	
	# Menunggu 1 Jam
	timer(3600)
