import os
from django.http import JsonResponse

from utils import join_list
from wctool.wctoolutils import FileDto, FileWithContentDto, extract_file_id_name


DIRECTORY_NAME = "./wctool/texts/"
FILE_SEPARATOR = '-'
CHAR_NUMBER = 200
WORDS_SEPARATOR = [' ', '\n']


def get_all_files_names(request) -> JsonResponse:
  if request.method != "GET":
    return JsonResponse({'error': 'Method not allowed'}, status=405)

  files: list[FileDto] = []
  for file in os.listdir(DIRECTORY_NAME):
    if file.endswith('.txt'):
      [id, name] = extract_file_id_name(file, FILE_SEPARATOR)
      files.append(FileDto(id, name).to_dict())
  return JsonResponse(files, safe=False)


def get_files_by_id(request) -> JsonResponse:
  if request.method != "GET":
    return JsonResponse({'error': 'Method not allowed'}, status=405)

  fileId: str = request.GET.get('id', '')
  if not fileId:
    return JsonResponse({'error': 'File ID not provided'}, status=400)

  for file in os.listdir(DIRECTORY_NAME):
    if file.startswith(fileId + '-'):
      filePath: str = file
      break

  if not os.path.exists(DIRECTORY_NAME + filePath):
    return JsonResponse({'error': 'File not found'}, status=404)

  with open(DIRECTORY_NAME + filePath, 'r', encoding='utf-8') as file:
    content = file.read()
    [id, name] = extract_file_id_name(filePath, FILE_SEPARATOR)
    print('len(content)', len(content))
    if (len(content) <= 2 * CHAR_NUMBER):
      startContent: str = content
      endContent: str = ''
    else:
      wordLength = -1
      while ((content[CHAR_NUMBER + wordLength] not in WORDS_SEPARATOR) & (CHAR_NUMBER + wordLength <= len(content))):
        wordLength += 1
      startContent: str = content[:CHAR_NUMBER + wordLength]

      wordLength = 0
      while ((content[-CHAR_NUMBER + wordLength] not in WORDS_SEPARATOR) & (-CHAR_NUMBER + wordLength >= -len(content))):
        wordLength -= 1
      endContent: str = content[-CHAR_NUMBER + wordLength + 1:]

  return JsonResponse(FileWithContentDto(
      id,
      name,
      startContent,
      endContent,
    ).to_dict())
