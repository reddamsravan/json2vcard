from os import linesep

class Vcard:
    BEGIN = 'BEGIN:VCARD'
    END = 'END:VCARD'
    VERSION = 'VERSION:4.0'

    def __init__(self, props) -> None:
        self.props = props

    def toString(self) -> str:
        card = ''
        card += linesep
        card += self.BEGIN
        card += linesep
        card += self.VERSION

        for prop in self.props:
            card += linesep
            card  += prop.upper() + ':' + self.props[prop]

        card += linesep
        card += self.END

        return card

