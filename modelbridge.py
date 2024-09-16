from pathlib import Path
import ollama
import json



knowledge_folder = Path("../knowledge")

def getExtensionsCatagory(exts:list[str], catagories:list[str]):
    def swap_dict(dic:dict):
        return {value: key for key, values in dic.items() for value in values}
    unknown_exts = []
    ext_knowledge = knowledge_folder / "extensionCatagory.json"
    with open(ext_knowledge) as file:
        knowledge = json.load(file)
    print(knowledge)

print(swap_dict({"Videos": ["mkv", "mp4"]}))
