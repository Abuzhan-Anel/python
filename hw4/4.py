class Time:
    def __init__(self,sec):
        self.sec = sec

    def convert_to_minutes(self):
        return '{} : {} minute'.format(self.sec//60,self.sec%60)

    def convert_to_hours(self):
        return '{:.2f} hour'.format(self.sec/3600)

your = int(input())
s = Time(your)
print(s.convert_to_minutes())
print(s.convert_to_hours())        