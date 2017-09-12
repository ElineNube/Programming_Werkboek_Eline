def new_password():
    res = newpassword != oldpassword and len(newpassword)>=6 and len(oldpassword)>=6
    return res

oldpassword = input('Wat is je oude wachtwoord?')
newpassword = input('Wat is je nieuwe wachtwoord?')

if new_password():
    print('Het wachtwoord is goedgekeurd!')

else:
    print('Helaas, het wachtwoord is niet goed. Kies een ander wachtwoord.')