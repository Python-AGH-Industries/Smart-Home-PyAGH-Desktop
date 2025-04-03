from math import log10

class FloatRounder():
    def __init__(self):
        pass

    def roundFloat5(self, number):
        num_len = int(log10(number)) + 1
        if abs(number) < 1:
            return round(number, 5 + self.zerosCount(number))
        elif 1 <= num_len <= 5:
            return round(number, 5 - num_len)
        else:
            return int(number)
        
    def zerosCount(self, number):
        if abs(number) < 1:
            cnt = 0
            while abs(number) < 1:
                cnt += 1
                number *= 10
            return cnt - 1
        else:
            return None