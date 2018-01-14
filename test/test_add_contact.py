# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app, json_contacts):
        contact = json_contacts
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


