def analyze(numbers):
  result = []
  index = {}
  min = None
  max = None

  for n in numbers:
    index[n] = True
    if not max or n > max:
      max = n
    if not min or n < min:
      min = n
  
  for n in range(min + 1, max):
    if not n in index:
      result.append(n)

  return result

li = [-1,2,6,-7]
print analyze(li)
