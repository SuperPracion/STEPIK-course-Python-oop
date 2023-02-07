import datetime


class Switch:
    # TODO требуется реализовать ID для каждого Switch с хранением в общем атрибуте класса
    def __init__(self, start_pos=False, max_history_len=100):
        self.__pos = start_pos
        self.__max_history_len = max_history_len
        self.__history = {}

    def __iter__(self):
        return iter(self.__history.items())

    def __eq__(self, other) -> bool:
        """Метод позволяет сравнить текущие позицию Switch c эквивалентом Switch или типом bool"""
        if isinstance(other, bool):
            return self.__pos == other
        if isinstance(other, Switch):
            return self.__pos == other.__pos
        raise ValueError(f'Не возможно сравнить {other} с Switch')

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def switch(self):
        """Переводит .pos в противоположный текущему. При включенном Switch - TRUE (ON), переведёт в FALSE (OFF)"""
        self.__history_defrag()
        self.__pos = not self.__pos
        self.__history[datetime.datetime.now()] = self.get_pos

    def __history_defrag(self):
        """Метод отвечает за контроль длинны истории и ей очистку"""
        if len(self.__history) > self.__max_history_len:
            del self.__history[self.__history.keys()][0]

    @property
    def get_pos(self) -> bool:
        """Возвращает текущую позицию переключателя, где FALSE - OFF, TRUE - ON"""
        return self.__pos

    @property
    def get_history(self) -> dict:
        """Возвращает историю переключений Switch в формате {datetime: bool}, где FALSE - OFF, TRUE - ON"""
        return self.__history


p1 = Switch(max_history_len=200)
p2 = Switch(start_pos=True)

print(p1 != False)
