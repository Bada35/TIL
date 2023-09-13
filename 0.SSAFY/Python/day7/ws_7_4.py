# ws_7_4.py

class Shape:
   def __init__(self, Width, Height):
      self.Width = Width
      self.Height = Height

   def print_info(self):
      print(f'Width: {self.Width}\nHeight: {self.Height}\nArea: {self.Width * self.Height}\nPerimeter: {self.Width*2 + self.Height*2}')
      

shape1 = Shape(5, 3)
shape1.print_info()
