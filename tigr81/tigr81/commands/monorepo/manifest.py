from typing import List, Optional
from pydantic import BaseModel
import pathlib as pl

from tigr81.commands.scaffold.project_template import ProjectTemplate
from tigr81.utils.read_yaml import read_yaml

class Manifest(BaseModel):
    name: str
    relative_path: Optional[pl.Path] = pl.Path(".")
    description: Optional[str]
    components: List[ProjectTemplate]



if __name__ == '__main__':
    dct = read_yaml("/home/giambrosio/projects/personal/tigr81/tigr81/manifest.yml")
    
    manifest = Manifest(**dct)

    for component in manifest.components:
        print(component)