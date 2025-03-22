import pikepdf
from tqdm import tqdm
passwords = []
for wachtwoord in open("woorden.txt"):
    passwords.append(wachtwoord.strip())
for wachtwoord in passwords:
    pikepdf.open("hacking.pdf", password = password)
    pass