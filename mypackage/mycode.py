def calc_area_square(side_length: float) -> float:
  ''' return area of a square '''
  if side_length < 0:
    raise ValueError(f'side_length cannot be negative, got {side_length}')
  return side_length ** 2

from math import pi

def calc_area_circle(radius:float) -> float:
  ''' return area of a circle'''
  return pi * radius ** 2