import datetime

class Motor:
    pass


class Fan(Motor):
    def __init__(self, id: str, voltage: float, current: float, air_flow: float, **kwargs):
        self.id = id
        self.voltage = voltage
        self.current = current
        self.air_flow = air_flow
        self.condition = False
        self.start_working = None
        self.end_working = None

        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_info(self):
        return f"Info about Fan\n" \
               f"id - {self.id}\n" \
               f"voltage - {self.voltage} volt\n" \
               f"current - {self.current} current\n" \
               f"air_flow - {self.air_flow} м3/с\n" \
               f"condition - {'Вкл' if self.condition else 'Выкл'}"

    def off(self):
        if self.condition:
            print('OFF')
            self.end_working = datetime.datetime.now()
            # print(f'START WORKING - {self.start_working}\n'
            #       f'END WORKING - {self.end_working}\n'
            #       f'TOTAL TIME IN WORKING - {self.end_working - self.start_working}\n')
            self.condition = False
            return {'START WORKING': self.start_working, 'END WORKING': self.end_working, 'TOTAL TIME IN WORKING': self.end_working - self.start_working}

    def on(self):
        if not self.condition:
            print('ON')
            self.start_working = datetime.datetime.now()
            self.condition = True


fan = Fan('AA1', 1.0, 1.0, 30)
print(fan.get_info())
fan.on()
for i in range(9999):
    z = i ** 999
print(fan.off())

print(fan.start_working)
print(fan.end_working)