# OpenCrossword Dictionaries
This repository contains JSON dictionaries of multiple languages for use in the [OpenCrossword](https://github.com/alexis-martel/Open-Crossword) project. The words are formatted for crossword-making in different languages.
- [./raw-dictionaries](raw-dictionaries) contains raw Aspell language dumps
- [./dictionaries](dictionaries) contains formatted JSON dictionaries
## Generate a dictionary
1. Dump a dictionary from GNU Aspell
    ```bash
    aspell -d $LANGUAGE_CODE dump master | aspell -l en expand > $LANGUAGE_CODE.txt
    ```
    where $LANGUAGE_CODE is the ISO 639-1 code of the language you want to generate a dictionary for.
2. Run the [generate.py](gen_dict.py) script
    ```bash
    python3 gen_dict.py [Raw dictionary path] [Result dictionary path]
    ```
## About the dictionaries
The dictionaries are simple JSON translations of GNU Aspell language dumps. See [GNU Aspell](http://aspell.net/) for more information.