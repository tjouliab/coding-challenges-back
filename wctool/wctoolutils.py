import string
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


class FileCountOptionsDto:
    id: string
    byte: bool
    chars: bool
    words: bool
    lines: bool


class FileCountResultDto:
    id: string
    byteCount: int
    charsCount: int
    wordsCount: int
    linesCount: int


def extract_file_id_name(file: str, separator: str) -> list[str]:
    id = file.split(separator)[0]
    name = join_list(file.split(separator)[1:], separator)
    return [id, name]


def count_bytes(binary_content: bytes) -> int:
    return len(binary_content)


def count_words(content: str) -> int:
    return len(content.split())


def count_characters(content: str) -> int:
    return len(content)


def count_lines(content: str) -> int:
    return len(content.splitlines())
