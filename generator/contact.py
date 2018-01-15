from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as Err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="")] + [
            Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                                    title=random_string("title", 20), company=random_string("company", 20), address=random_string("address", 30), home_phone=random_string("home_phone", 10),
                                    mobile=random_string("mobile_phone", 10), work_phone=random_string("work_phone", 10), fax=random_string("fax", 10), email=random_string("email", 20),
                                    email2=random_string("email2", 20), email3=random_string("email3", 20), homepage_ru=random_string("homepage", 20), byear=random_string("byear", 4),
                                    ayear=random_string("ayear", 4),
                                    address2=random_string("address", 30), phone2=random_string("phone2", 10), notes=random_string("notes", 30))
            for i in range(n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))