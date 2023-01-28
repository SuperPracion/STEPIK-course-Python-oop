class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        for id, value in enumerate(self._notes, 1):
            print(f'{id}.{value}')

note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list