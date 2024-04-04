from utils import join_list


class FileDto:
  id: str
  name: str

  def __init__(self, id, name) -> None:
    self.id = id
    self.name = name

  def to_dict(self) -> dict:
    return {
      'id': self.id,
      'name': self.name,
    }


class FileWithContentDto:
  id: str
  name: str
  startContent: str
  endContent: str

  def __init__(self, id, name, startContent, endContent) -> None:
    self.id = id
    self.name = name
    self.startContent = startContent
    self.endContent = endContent

  def to_dict(self) -> dict:
    return {
      'id': self.id,
      'name': self.name,
      'startContent': self.startContent,
      'endContent': self.endContent,
    }


def extract_file_id_name(file: str, separator: str) -> list[str]:
  id = file.split(separator)[0]
  name = join_list(file.split(separator)[1:], separator)
  return [id, name]
