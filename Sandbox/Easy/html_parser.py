import urllib2
def GetNext(content, last_location):
  start = content.find('<', last_location)
  if start == -1:
    return None, -1

  end = content.find('>', start + 1)
  if end == -1:
    return None, -1

  t = content[start:end + 1]

  return (t, start)

def GetType(t):
  if t[1] == '/' or t[1] == '!':
    return None

  space = t.find(' ')
  if space != -1:
    return t[1:space]
  else:
    return t[1:-1]

def GetCounts(url):
  counts = {}
  response = urllib2.urlopen(url)
  content = response.read()
  next_location = 0
  while True:
    t, last_location = GetNext(content, next_location)
#    print t, last_location
    if not t:
      break

    t_type = GetType(t)
    if t_type:
      if not t_type in counts:
        counts[t_type] = 0
      counts[t_type] = counts[t_type] + 1

    next_location = last_location + len(t) + 1
  return counts

#GetCounts('http://python.org/')
print GetCounts('http://python.org/')
