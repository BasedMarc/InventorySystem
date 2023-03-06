password = input()

for old, new in {"i": "!", "a": "@", "m": "M", "B": "8", "o": "."}.items():
    password = password.replace(old, new)

password += "q*s"

print(password)