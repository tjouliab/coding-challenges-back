import os
from django.http import JsonResponse

from wctool.wctoolutils import FileDto, FileWithContentDto, count_bytes, count_characters, count_lines, count_words, extract_file_id_name


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


def get_files_properties_by_id(request) -> JsonResponse:
  if request.method != "GET":
    return JsonResponse({'error': 'Method not allowed'}, status=405)

  options: dict = request.GET.dict()
  fileId: str = options.get('id')
  for filePath in os.listdir(DIRECTORY_NAME):
    if filePath.startswith(fileId):
      with open(DIRECTORY_NAME + filePath, 'r', encoding='utf-8') as file:
        content = file.read()
      with open(DIRECTORY_NAME + filePath, 'rb') as file:
        binary_content = file.read()

  response: dict = {}
  if (int(options.get('byte'))):
    response['byte'] = count_bytes(binary_content)
  if (int(options.get('chars'))):
    response['chars'] = count_words(content)
  if (int(options.get('words'))):
    response['words'] = count_characters(content)
  if (int(options.get('lines'))):
    response['lines'] = count_lines(content)

  return JsonResponse(response)
