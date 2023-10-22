from typing import List, Optional
from pydantic import BaseModel
import pathlib as pl

import yaml
from tigr81.commands.monorepo import MANIFEST_FILE_NAME

from tigr81.commands.scaffold.project_template import ProjectTemplate
from tigr81.utils.read_yaml import read_yaml

class Manifest(BaseModel):
    name: Optional[str] = "my-monorepo"
    relative_path: Optional[pl.Path] = pl.Path("src")
    description: Optional[str] = "A monorepo for my project"
    components: Optional[List[ProjectTemplate]] = []


    def to_yaml(self) -> None:
        with open(MANIFEST_FILE_NAME, "w") as f:
            yaml.dump(
                data=self.model_dump(mode="json"), 
                stream=f,
                default_flow_style=False,
                sort_keys=False
            )
