profile = {}

# The name # 1
name = input("Enter the name : ").lower()
profile["name"] = str(name)
print("\n")

# The last name # 2
sname = input("Enter the last name : ").lower()
profile["sname"] = str(sname)
print("\n")


# The date of birth # 3
old_birthday = input("Enter the birthday DDMMYYYY : ")
while len(old_birthday) < 8:
    print("Enter correct birthday : like < DDMMYYYY > : ")
    old_birthday = input("Enter the birthday DDMMYYYY")

# We will need the birthday with zeros to generation, so we will keep it
profile["old birthday"] = old_birthday

# Delete zeros from days and months if present
deleter = old_birthday[0:4]
keeper = old_birthday[4:9]
x = "0"
DDMM = deleter
for i in deleter:
    if i in x:
        DDMM = DDMM.replace(x, "")
birthday = DDMM + keeper
profile["birthday"] = birthday
print("\n")

# star number or special number # 4
snumber = input("Enter special number like (1234) or username : ")
profile["snumber"] = snumber
print("\n")


# Generation the list

# Names
names = [
    name,
    sname,
    snumber,
]

# Capital the words
c_fname = name.capitalize()
ca_fname = name.upper()
c_sname = sname.capitalize()
ca_sname = sname.upper()
c_snumber = snumber.capitalize()
ca_snumber = snumber.upper()

capitals = [
    c_fname,
    ca_fname,
    c_sname,
    ca_sname,
    c_snumber,
    ca_snumber,
]

# reverses
rev_fname = profile["name"][::-1]
rev_sname = profile["sname"][::-1]
# reverse date of birthday
rev_birthday = profile["birthday"][::-1]

# YYYYDDMM
rev_birthday2 = profile["old birthday"][4:9] + DDMM

# reverse the special number
rev_snumber = profile["snumber"][::-1]
reverse = [
    rev_fname,
    rev_sname,
    rev_birthday,
    rev_snumber,
    rev_birthday2,
]

# Birthday collection
birthday_YY = profile["birthday"][-2:]
birthday_YYYY = keeper

# make special list
special = [
    birthday,
    birthday_YYYY,
    birthday_YY,
    rev_birthday2,
    snumber,
]

# Make the list

final = []
for a in names:
    for b in capitals:
        for c in reverse:
            for d in special:
                final.append(birthday)
                final.append(snumber)
                final.append(name + sname + d)
                final.append(d + name + sname)
                final.append(sname + name + d)
                final.append(d + sname + name)
                final.append(c_fname + c_sname + d)
                final.append(d + c_fname + c_sname)
                final.append(a + d)
                final.append(d + a)
                final.append(b + d)
                final.append(d + b)
                final.append(a + a + d)
                final.append(a + c)
                final.append(c + a)
                final.append(name + sname + c)
                final.append(sname + name + c)
                final.append(a + b + d)
                final.append(d + b + a)
                final.append(d + a + b)

# Make the list
name_list = name + ".txt"
lister = open(name_list, "a")
for f in final:
    lister.write(f + "\n")
lister.close()
print("[+] Generation....        " + "\n")
print("[+] Congratulations your list saved as" + " " + name_list + " " + "Good luck")










