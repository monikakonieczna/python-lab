def split(string, sep = None, maxsplit = -1):
  if maxsplit < 0:
    maxsplit = float('inf')
  count, i = 0, 0
  len_string = len(string)
  len_sep = 1 if sep is None else len(sep)
  result = ['']
  while i < len_string and count < maxsplit + (sep is None):
    if test := ((add := string[i]) in '\f\r\n\t\v ') and sep is None:
      add = ''
    if string[i:i+len_sep] == sep:
      result.append('')
      i += len_sep
      count += 1
      continue
    elif test:
      if not result[-1]:
        i += 1
        continue
      else:
        count += 1
        if count > maxsplit: break
        result.append('')
    result[-1] += add
    i += 1
  if sep is None and not result[-1]: result = result[:-1]
  if result: result[-1] += string[i:]
  return result