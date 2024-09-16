import ollama
from extension_catagory import ExtensionCatagory as Ext
import json

# class AskLLM:
#     pass

  #  what are the suitable folders out of ['Documents', 'Videos', 'Archives', 'Music', 'Other'] to store files with these extensions? ['zip', 'rar', 'wav', 'knr', 'mp4', 'docx', 'pdf'] output as json {string:string} key is the extension, value is the folder name

def classify_file_exts(exts: list[str], catagories: list[str]):
    system = "give only json output. do not start conversation"
    task_1 = "what are the suitable folders out of {catagories} to store files with these extensions? {extensions} output as json {{string:string}} key is the extension, value is the folder name"
    task_2 = "whst are the possible folder names for files with these extensions {extensions} give common suitable folder name andfif  the decided folder names are too specific use 'Uncommon' folder.since uncommon is a folder name it should not be a key only a value. output should be in json {{string:string}} key is the extension, value is the folder name"
    response = json.loads(ollama.generate(model='mistral', prompt=task_1.format(catagories=str(catagories+['Others']), extensions=str(exts+['zip', 'exe', 'pdf', 'msi', 'appx', 'docx', 'pptx'])), system=system, format='json')['response'])
    other_exts = list()
    available_exts = dict()
    new_exts = {}
    for key, val in response.items():
        if val != 'Others':
            available_exts[key] = val
        else:
            other_exts.append(key)
    print(available_exts, other_exts)
    
    response2 = json.loads(ollama.generate(model='mistral', prompt=task_2.format(extensions=str(other_exts)), system=system, format='json')['response'])
    print(response2)


res = classify_file_exts(Ext().exts(), Ext().folders())