# hw_7_2.py

class StringRepeater:
    @staticmethod
    def repeat_string(num, input_str):
        for i in range(num):
            print(input_str)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
