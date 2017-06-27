import re
import string
import numpy as np
import pandas as pd

# password strengths
strengths = {"28 bits": "Very Weak",
             "28 - 35 bits": "Weak",
             "36 - 59 bits": "Reasonable",
             "60 - 127 bits": "Strong",
             "128+ bits": "Overkill"}

# data frame for passwords
st = pd.DataFrame({"Entropy": list(strengths.keys()), "Strength": list(strengths.values())})

# setting regex expressions for alphabets and other characters
alps = re.compile(r'[a-zA-Z]')
hspec = re.compile(r'^[^a-zA-Z]+')
lspec = re.compile(r'[^a-zA-Z]+$')

# dict that keeps track of what types of characters are used
sets = {'d':0, 'p':0, 'l':0, 'u':0}

# assigning corresponding keys to groups
types = {}
types['d_vals'] = string.digits
types['p_vals'] = string.punctuation
types['l_vals'] = string.ascii_lowercase
types['u_vals'] = string.ascii_uppercase

# entropy calculation
def entropy(pw):
    charset = 0
    plist = list(pw)

    if [val for val in plist if val in set(types['d_vals'])]:
        charset += len(types['d_vals'])
        sets['d'] = 1
    if [val for val in plist if val in set(types['p_vals'])]:
        charset += len(types['p_vals'])
        sets['p'] = 1
    if [val for val in plist if val in set(types['l_vals'])]:
        charset += 26
        sets['l'] = 1
    if [val for val in plist if val in set(types['u_vals'])]:
        charset += 26
        sets['u'] = 1

    # entropy calculation
    N = charset ** len(pw)
    ent = np.math.log(N, 2)

    return float("{:.2f}".format(ent))

# deciding what to do with the password
def what(pw):
    # entropy of the password
    pass_ent = entropy(pw)
    print("The entropy value of your password is {0}".format(pass_ent))
    if pass_ent < 60:
        print("Your password is not strong enough! Let's make it stronger.\n")
        make_stronger(pw)
    elif pass_ent > 127:
        print("Your password is just a *little* overkill, so as long as you can keep track of it...")
    else:
        print("Your new password - {0} - is perfect for use.\n".format(pw))

def make_stronger(pw):
    # if there are no letters at all, add some until len is at least 8
    if not sets['l'] and not sets['u']:
        temp = ['l', 'u']
        while len(pw) < 8:
            n = np.random.randint(0,2)
            if n == 0:
                sets['l'] = 1
            else:
                sets['u'] = 1
            pw = types[temp[n] + '_vals'][np.random.randint(0,len(types[temp[n] + '_vals']))] + p

    # going through the types that are missing and adding them
    for x in ['d', 'p']:
        if not sets[x]:
            pw += types[x + '_vals'][np.random.randint(0,len(types[x + '_vals']))]
            sets[x] = 1

    # if there are no lowercase letters, add some
    if not sets['l']:
        for i in range(len(pw)):
            if pw[i].isupper():
                pw = list(pw)
                pw[i] = pw[i].lower()
                pw = ''.join(pw)
                break
        sets['l'] = 1

    # if there are no uppercase letters, add some
    if not sets['u']:
        for i in range(len(pw)):
            if pw[i].islower():
                pw = list(pw)
                pw[i] = pw[i].upper()
                pw = ''.join(pw)
                break
        sets['u'] = 1


    # evaluating the redone pw
    if entropy(pw) > 60:
        what(pw)
    else:
        temp = ['d', 'p']
        x = temp[np.random.randint(0, 2)]
        while entropy(pw) <= 60:
            pw = types[x + '_vals'][np.random.randint(0,len(types[x + '_vals']))] + pw
            pw += types[x + '_vals'][np.random.randint(0,len(types[x + '_vals']))]
        sets[x] = 1
        what(pw)

# printing entropy guide
print("Entropy strengh guide: ------- \n")
print(st)
print()

# interacting with user
password = input("Enter your password:\n")

what(password)
