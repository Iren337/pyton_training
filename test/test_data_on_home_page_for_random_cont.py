import re
from random import randrange

from test.test_phones import merge_phones_like_on_home_page, merge_emails_like_on_home_page


def test_all_data_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert clear2(contact_from_home_page.lastname) == clear2(contact_from_edit_page.lastname)
    assert clear2(contact_from_home_page.firstname) == clear2(contact_from_edit_page.firstname)
    assert clear2(contact_from_home_page.address) == clear2(contact_from_edit_page.address)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear2(s):
    return re.sub(" ", "", s)