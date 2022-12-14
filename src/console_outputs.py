from abc import ABC, abstractmethod


class ConsoleOutput(ABC):
    @abstractmethod
    def render(self):
        pass


class ShowAllContactsConsoleOutput(ConsoleOutput):
    def __init__(self, data):
        self.data = data
    def render(self):
        contacts = ''
        page_number = 1
        for page in self.data.iterator():
            contacts += f'Page №{page_number}\n'
            for record in page:
                contacts += f'{record.get_info()}\n'
                page_number += 1
        return contacts


class GetInfoConsoleOutput(ConsoleOutput):
    def __init__(self, data):
        self.data = data
    def render(self):
        birthday_info = ''
        email_info = ''
        address_info = ''
        phones_info = ', '.join([phone.value for phone in self.data.phones])
        if self.data.birthday:
            birthday_info = f' Birthday : {self.data.birthday.value}'
        if self.data.email:
            email_info = f' Email : {self.data.email.value}'
        if self.data.address:
            address_info = f' Address : {self.data.address.value}'
        return f'{self.data.name.value} : {phones_info}{birthday_info}{email_info}{address_info}'


class ShowNoteConsoleOutput(ConsoleOutput):
    def __init__(self, data):
        self.data = data
    def render(self):
        result = 20 * "-" + "\n"
        result += f"note id - {self.data.note_id}\n"
        result += f"note text - {self.data.note_text}\n"
        if self.data.note_tags:
            result += f"tags - {' '.join(sorted(tag for tag in self.data.note_tags))}\n"
        return result


class ShowNotesConsoleOutput(ConsoleOutput):
    def __init__(self, data):
        self.data = data

    def render(self):
        result = ""
        for note in self.data.get_notes():
            result += note.get_info()
        return result
