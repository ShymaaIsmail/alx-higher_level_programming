#!/usr/bin/python3
class MyList(List):
  def __init__(self):
    super().__init__(self)
  def print_sorted(self):
    super().sort(self)
    print(super().items)
