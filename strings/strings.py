from os import listdir, path
from typing import Any, Dict, List, Union

from google_trans_new import google_translator
from cython import udB
from yaml import safe_load

language = [udB.get("language") or "en"]
languages = {}

Trs = google_translator()

strings_folder = path.join(path.dirname(path.realpath(__file__)), "strings")

for file in listdir(strings_folder):
    if file.endswith(".yml"):
        code = file[:-4]
        languages[code] = safe_load(
            open(path.join(strings_folder, file), encoding="UTF-8"),
        )


def get_string(key: str) -> Any:
    lang = language[0]
    try:
        return languages[lang][key]
    except KeyError:
        try:
            tr = Trs.translate(languages["en"][key], lang_tgt=lang)
            if languages.get(lang):
                languages[lang][key] = tr
            else:
                languages.update({lang:{key:tr}})
            return tr
        except KeyError:
            return f"Warning: could not load any string with the key `{key}`"


def get_languages() -> Dict[str, Union[str, List[str]]]:
    return {
        code: {
            "name": languages[code]["name"],
            "natively": languages[code]["natively"],
            "authors": languages[code]["authors"],
        }
        for code in languages
    }
