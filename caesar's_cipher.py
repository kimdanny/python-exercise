# Exercise 5

#Breaking Caesar's Cipher


def break_cipher(text):
    assert type(text) == str
    cipher = list(text)
    decode = []

    for x in cipher:
        if 78<= ord(x) <=90:
            decode.append(chr(ord(x) - 13))
        elif 65<= ord(x) <=77:
            decode.append(chr(ord(x) + 13))
        elif 110<= ord(x) <=122:
            decode.append(chr(ord(x) - 13))
        elif 97<= ord(x) <=109:
            decode.append(chr(ord(x) + 13))
        
    print(decode)

break_cipher('hello')
break_cipher('uryyb')
break_cipher('HELLO')
break_cipher('URYYB')