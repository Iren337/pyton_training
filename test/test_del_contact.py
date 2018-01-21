from model.contact import Contact
import random


def test_delete_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.Create(Contact(firstname="name", lastname= "lastname"))
    old_contacts = db.get_contact_list()
    #index = randrange(len(old_contacts))
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if db.check_ui == 'true':
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)