from notes import user_notes
from notes_decorator import input_error
from console_outputs import ShowNotesConsoleOutput

@input_error
def add_note(data):
    note_text = data
    user_notes.add_note(note_text)
    return "New note added"


@input_error
def show_notes():
    return ShowNotesConsoleOutput(user_notes).render()


@input_error
def add_tags(data: str) -> str:
    note_id, *tags = data.split(" ")

    if not tags:
        return "There are no tags in your input"
    user_notes.add_tags(int(note_id), tags)
    return "Tags added"


@input_error
def delete_note(data: str) -> str:
    note_id = int(data)
    user_notes.delete_note(note_id)
    return f"Note [{note_id}] deleted"


@input_error
def edit_note(data: str) -> str:
    note_id, *note_text_list = data.split(" ")
    note_id = int(note_id)
    note_text = " ".join(note_text_list)

    user_notes.edit_note(note_id, note_text)
    return f"Note [{note_id}] edited"



@input_error
def search_notes(data):
    result = ""
    for note in user_notes.search_notes(data).values():
        result += note.get_info()
    return result


@input_error
def search_notes_by_tags(data):
    tags = data.split(" ")
               
    search_results = user_notes.search_notes_by_tags(tags)

    if not search_results:
        return "There are no notes with these tags"

    output = ''

    for tag in sorted(search_results):
        output += f"Tag - {tag}:\n"

        for key, note in search_results[tag].items():
            output += f"  {key}: {note.note_text}\n"
        output += "------------------------------------\n"

    return output


def sort_notes() -> str:
    result = ""
    for note in user_notes.sort_notes().values():
        result += note.get_info()
    return result
