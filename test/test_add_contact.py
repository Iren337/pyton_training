# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="1111", middlename="11111", lastname="111111", nickname="1111111",
                                   title="title1", company="company", address="address", home_phone="12345678",
                                   mobile="2345678", work_phone="3456789", fax="4567890", email="email",
                                   email2="email2", email3="email3", homepage_ru="homepage.ru", byear="1841",
                                   ayear="1234",
                                   address2="address secondary", phone2="home", notes="notes")
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
