from pprint import pprint
import csv
import re


def update_contact(row, new_record):
    for i in range(len(row)):
        if new_record[i]:
            row[i] = new_record[i]


def format_phone(phone):
    pattern = r'(\+7|8)\s*\(?(\d{3})[\)|-]?\s*(\d{3})-?(\d{2})-?(\d{2})\s?\(?(доб.\s\d{4})?\)?'
    substitution = r'+7(\2)\3-\4-\5 \6'
    new_phone_format = re.sub(pattern, substitution, phone)
    return new_phone_format.strip()


def main():
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    fixed_contacts = list()
    fixed_contacts.append(contacts_list[0])
    index = 1
    contact_indexes = dict()

    for contact in contacts_list[1:]:
        line = list()

        for record in contact[:3]:
            if record:
                line.extend(record.split())
        if len(line) < 3:
            line.append('')

        line += contact[3:5]
        line += [format_phone(contact[5])]
        line += contact[6:]

        name = ' '.join(line[0:2])
        contact_index = contact_indexes.get(name)
        if contact_index:
            update_contact(fixed_contacts[contact_index], line)
        else:
            contact_indexes[name] = index
            index += 1
            fixed_contacts.append(line)
        # print(contact)
        # print(len(contact))

    pprint(fixed_contacts)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(fixed_contacts)


if __name__ == '__main__':
    main()
