import re
from model.contact import Contact

def test_all_contacts_home_page(app, db):
    home_page_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(home_page_contacts)):
        db_contact = db_contacts[i]
        home_page_contact = home_page_contacts[i]
        assert clear2(home_page_contact.firstname) == clear2(db_contact.firstname)
        assert clear2(home_page_contact.lastname) == clear2(db_contact.lastname)
        assert clear2(home_page_contact.address) == clear2(db_contact.address)
        assert clear(home_page_contact.all_phones_from_home_page) == merge_phones_like_on_home_page(db_contact)
        assert clear(home_page_contact.all_emails_from_home_page) == merge_emails_like_on_home_page(db_contact)


def clear(s):
    return re.sub("[() .-]", "", s)

def clear2(s):
    return re.sub(" ", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                            filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                            filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile, contact.work_phone, contact.phone2]))))