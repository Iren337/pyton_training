# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

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
            for i in range(5)
            ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()
        app.contact.Create(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_test_add_blank_contact(app):
#        old_contacts = app.contact.get_contact_list()
#        app.contact.Create(Contact(firstname="", middlename="", lastname="", nickname="",
#                                   title="", company="", address="", home_phone="",
#                                   mobile="", work_phone="", fax="", email="",
#                                   email2="", email3="", homepage_ru="", byear="",
#                                   ayear="",
#                                   address2="", phone2="", notes=""))
