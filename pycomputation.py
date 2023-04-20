import os

class PyComputation():

  def __init__(self, nums):
    # takes in string
    self.nums = nums

  def add(self):
    num_list = self.nums.split(" ")
    total = 0
    for i in num_list:
      if i != ',':
        total += int(i)
    return total
    
  def subtract(self):
    num_list = self.nums.split(" ")
    total = int(num_list[0])
    num_list.pop(0)
    for i in num_list: 
      total -= int(i)
    return total
      
  def multiply(self):
    num_list = self.nums.split(" ")
    total = int(num_list[0])
    num_list.pop(0)
    for i in num_list:
      total = total * int(i)
    return total
  
  def divide(self):
    num_list = self.nums.split(" ")
    total = int(num_list[0])
    num_list.pop(0)
    for i in num_list: 
      total /= int(i)
    return total
  
  def square_root(self):
    target = int(self.nums)
    low = 1
    high = target
    while low < high:
      mid = (high + low)//2
      if mid * mid == target:
        return mid
      elif mid * mid > target:
        high = mid - 1
      elif mid * mid < target:
        mid = low
    return low
    

  def exponent(self):
    num_list = self.nums.split(" ")
    total = int(num_list[0])
    num_list.pop(0)
    for i in num_list:
      total = total ** int(i)
    return total
    
  def root(self):
    target = int(self.nums)
    for i in range(2, target):
      total = 1
      while total <= target:
        total *= i
        if total == target:
          return i
    if total > target:
      print("This number does not have a root.")
      
  def index_root(self):
    num_list = self.nums.split(" ")
    x = int(num_list[0]) 
    return int(num_list[1])**(1/x)
    
  def absolute_value(self):
    i = int(self.nums)
    if int(i) < 0:
        return int(i) * -1
    else:
        return int(i)
        
  def trig(self):
    #enter numbers in a^2 + b^2 = c^2 order format
    num_list = self.nums.split(" ")
    if num_list[0] == 'x':
      a_squared = int(num_list[2])**2 - int(num_list[1])**2
      return a_squared**0.5
    elif num_list[1] == 'x':
      b_squared = int(num_list[2])**2 - int(num_list[0])**2
      return b_squared**0.5
    elif num_list[2] == 'x':
      c_squared = int(num_list[0])**2 + int(num_list)**2
      return c_squared**0.5
    
    
    
'''        
TEST FUNCTIONS

addition = PyComputation("1 2 3")
sub = PyComputation("24 3 1")
mult = PyComputation("2 2 3")
division = PyComputation("24 6 2")
exponent = PyComputation("2 2 2")
root = PyComputation("216")
square = PyComputation("64")
av = PyComputation("-16")
trig = PyComputation("x 4 5")

print(addition.add())
print(sub.subtract())
print(mult.multiply())
print(division.divide())
print(exponent.exponent())
print(root.root())
print(square.square_root())
print(av.absolute_value())
print(trig.trig())

'''
