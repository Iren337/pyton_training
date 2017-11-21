from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="222", middlename="2222", lastname="22222", nickname="222222",
                                   title="title2", company="company2", address="address2", home_phone="123456782",
                                   mobile="23456782", work_phone="34567892", fax="45678902", email="email2",
                                   email2="email22", email3="email32", homepage_ru="homepage2.ru", byear="1842",
                                   ayear="1232",
                                   address2="address secondary2", phone2="home2", notes="notes2"))
    app.session.logout()
