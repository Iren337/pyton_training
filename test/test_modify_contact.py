from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.Create(Contact(firstname="name", lastname="lastname"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="333", lastname="lastname2")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(middlename="3333"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name", lastname= "lastname"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname="22222"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


#def test_modify_contact_nickname(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(nickname="222222"))


#def test_modify_contact_title(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(title="title2"))


#def test_modify_contact(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(company="company2"))


#def test_modify_contact_address(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(address="address2"))


#def test_modify_contact_home_phone(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(home_phone="123456782"))


#def test_modify_contact_mobile(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(mobile="23456782"))


#def test_modify_contact_work_phone(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(work_phone="34567892"))


#def test_modify_contact_fax(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(fax="45678902"))


#def test_modify_contact_email(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(email="email2"))


#def test_modify_contact_email2(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(email2="email22"))


#def test_modify_contact_email3(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(email3="email32"))


#def test_modify_contact_homepage_ru(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(homepage_ru="homepage2.ru"))


#def test_modify_contact_byear(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(byear="1842"))


#def test_modify_contact_ayear(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(ayear="1232"))


#def test_modify_contact_address2(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(address2="address secondary2"))


#def test_modify_contact_phone2(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
#    app.contact.modify_first_contact(Contact(phone2="home2"))


#def test_modify_contact_notes(app):
#    if app.contact.count() == 0:
#        app.contact.Create(Contact(firstname="name"))
 #   app.contact.modify_first_contact(Contact(notes="notes2"))


#def test_modify_contact_all_fields(app):
#    app.contact.modify_first_contact(Contact(firstname="222", middlename="2222", lastname="22222", nickname="222222",
#                                   title="title2", company="company2", address="address2", home_phone="123456782",
#                                   mobile="23456782", work_phone="34567892", fax="45678902", email="email2",
#                                   email2="email22", email3="email32", homepage_ru="homepage2.ru", byear="1842",
#                                   ayear="1232",
#                                   address2="address secondary2", phone2="home2", notes="notes2"))
