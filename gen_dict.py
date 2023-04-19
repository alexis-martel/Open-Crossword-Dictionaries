import json
import os
import sys

try:
    RAW_DICT_PATH = os.path.join(sys.argv[1])
    RESULT_DICT_PATH = os.path.join(sys.argv[2])
except IndexError:
    print('Please provide the path to the raw dictionary and the path to the result dictionary.\nUsage: python3 '
          'gen_dict.py [Raw dictionary path] [Result dictionary path]')
    sys.exit(1)

WORD_LIST = []

with open(RAW_DICT_PATH) as f:
    lines = f.readlines()
    for line in lines:
        WORD_LIST.append(
            line.strip().lower().replace('\'', '').replace('é', 'e').replace('è', 'e').replace('ê', 'e').replace('ë',
                                                                                                                 'e').replace(
                'ô', 'o').replace('â', 'a').replace('à', 'a').replace('î', 'i').replace('ï', 'i').replace('ç',
                                                                                                          'c').replace(
                'û', 'u').replace('-', ''))  # Removes single quotes and whitespace

RESULT_DICT = {'words': sorted((set(WORD_LIST)))}  # Removes duplicates and sorts the list

with open(RESULT_DICT_PATH, 'w') as f:
    f.write(json.dumps(RESULT_DICT))
