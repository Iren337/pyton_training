from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="222"))


def test_modify_contact_middlename(app):
    app.contact.modify_first_contact(Contact(middlename="2222"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="22222"))


def test_modify_contact_nickname(app):
    app.contact.modify_first_contact(Contact(nickname="222222"))


def test_modify_contact_title(app):
    app.contact.modify_first_contact(Contact(title="title2"))


def test_modify_contact(app):
    app.contact.modify_first_contact(Contact(company="company2"))


def test_modify_contact_address(app):
    app.contact.modify_first_contact(Contact(address="address2"))


def test_modify_contact_home_phone(app):
    app.contact.modify_first_contact(Contact(home_phone="123456782"))


def test_modify_contact_mobile(app):
    app.contact.modify_first_contact(Contact(mobile="23456782"))


def test_modify_contact_work_phone(app):
    app.contact.modify_first_contact(Contact(work_phone="34567892"))


def test_modify_contact_fax(app):
    app.contact.modify_first_contact(Contact(fax="45678902"))


def test_modify_contact_email(app):
    app.contact.modify_first_contact(Contact(email="email2"))


def test_modify_contact_email2(app):
    app.contact.modify_first_contact(Contact(email2="email22"))


def test_modify_contact_email3(app):
    app.contact.modify_first_contact(Contact(email3="email32"))


def test_modify_contact_homepage_ru(app):
    app.contact.modify_first_contact(Contact(homepage_ru="homepage2.ru"))


def test_modify_contact_byear(app):
    app.contact.modify_first_contact(Contact(byear="1842"))


def test_modify_contact_ayear(app):
    app.contact.modify_first_contact(Contact(ayear="1232"))


def test_modify_contact_address2(app):
    app.contact.modify_first_contact(Contact(address2="address secondary2"))


def test_modify_contact_phone2(app):
    app.contact.modify_first_contact(Contact(phone2="home2"))


def test_modify_contact_notes(app):
    app.contact.modify_first_contact(Contact(notes="notes2"))


#def test_modify_contact_all_fields(app):
#    app.contact.modify_first_contact(Contact(firstname="222", middlename="2222", lastname="22222", nickname="222222",
#                                   title="title2", company="company2", address="address2", home_phone="123456782",
#                                   mobile="23456782", work_phone="34567892", fax="45678902", email="email2",
#                                   email2="email22", email3="email32", homepage_ru="homepage2.ru", byear="1842",
#                                   ayear="1232",
#                                   address2="address secondary2", phone2="home2", notes="notes2"))
