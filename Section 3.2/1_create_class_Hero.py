class Hero:
    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        return '\n'.join(*sorted([f'{key}: {value}' for key, value in self.__dict__.items()]))