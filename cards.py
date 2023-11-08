from faker import Faker


class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

        self._len_first_name_and_last_name = 0

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.phone_number}, {self.email}'

    def contact(self):
        return f'Wybieram numer {self.phone_number} i dzwonie do {self.first_name} {self.last_name}'

    @property
    def len_first_name_and_last_name(self):
        return self._len_first_name_and_last_name

    @len_first_name_and_last_name.setter
    def len_first_name_and_last_name(self, value):
        self._len_first_name_and_last_name = value


class BusinessContact(BaseContact):
    def __init__(self, job, company, company_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.company_phone_number = company_phone_number

    def contact(self):
        return f'Wybieram numer {self.company_phone_number} i dzwonie do {self.first_name} {self.last_name}'

    def __str__(self):
        return f'Zawód: {self.job}, firma: {self.company}, tel. słuzbowy: {self.company_phone_number}, {self.first_name} {self.last_name}, tel. prywatny: {self.phone_number}, {self.email}'


def create_contacts(type_contact, amount_contacts):
    """
       Function returns random contacts (2 types: base contact and businness contact)

       type_contact - specific type contact. 1 - for base contact, 2 - for businness contact
       amount_contacts = specific amount contacts will be returned 
    """
    contacts = []
    fake = Faker('pl_PL')
    for i in range(1, amount_contacts):
        if (type_contact == 1):
            contacts.append(BaseContact(
                fake.first_name(), fake.last_name(), fake.phone_number(), fake.email()))
        else:
            contacts.append(BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_number=fake.phone_number(),
                                            email=fake.email(), job=fake.job(), company=fake.company(), company_phone_number=fake.phone_number()))

    for contact in contacts:
        contact.len_first_name_and_last_name = len(
            contact.first_name) + len(contact.last_name)
        print(contact.len_first_name_and_last_name)
        print(contact.contact())
        print(contact)


create_contacts(1, 15)
