import json
import os
import pickle


def json_to_pickle(path, extention):
    files = os.listdir(path)
    for i in files:
        if os.path.basename(i):
            file_name_full = i
            file_name, ext = os.path.splitext(file_name_full)
            if str(ext[1:]).lower() == extention.lower():
                with open(file_name_full, 'r', encoding="utf-8") as j, open(file_name + '.pickle', 'wb') as f:
                    file_json = json.load(j)
                    pickle.dump(file_json, f)

