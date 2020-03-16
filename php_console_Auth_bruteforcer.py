import hashlib

# tried bruteforcing it wish hash("IP"+hash({password}+"NeverChangeIt:)")

pubkey = ' '
with open('rockyou.txt', 'r', encoding='utf8', errors='ignore') as file:
  for passwor in file:
    password = password.strip()
    tmp = hashlib.sha256(f'{password}NeverChangeIt:)'.encode()).hexdigest()
    pk = hashlib.sha256(f'10.255.0.2{tmp}.encode()).hexdigest()
    if pk == pubkey:
      print(password)
      break
