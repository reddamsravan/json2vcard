import json
from os import linesep
from vCard import Vcard

VCARD_VERSION = '4.0'

def generateVcardFile(contacts):
    cards = ''
    for contact in contacts:
        vCard = Vcard(contact)
        cards += vCard.toString()

    cards += linesep
    with open('contacts.vcf', 'w') as file:
        file.write(cards)


def main():
    file = open('contacts.json')
    contacts = json.load(file)
    generateVcardFile(contacts)

if __name__ == '__main__':
    main();
