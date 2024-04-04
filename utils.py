def join_list(values: list, separator: str = '') -> str:
  if len(values) == 0:
    return ''

  result: str = str(values[0])
  for value in values[1:]:
    result += separator + str(value)
  return result
