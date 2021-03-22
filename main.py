###solution to exercise 83 from ben stephenson's "the python workbook".

def price(items):
  if items == 1:
    return 10.95
  else:
    return 8 + items * 2.95

num_ = int(input('Enter a number of items: '))
print(f'The price is ${price(num_)}.')
