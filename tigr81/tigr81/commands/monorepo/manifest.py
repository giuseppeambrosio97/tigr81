from typing import List, Optional
from graphviz import Digraph
from pydantic import BaseModel
import pathlib as pl

import yaml
from tigr81.commands.monorepo import MANIFEST_FILE_NAME

from tigr81.commands.scaffold.project_template import ProjectTemplate, ProjectTypeEnum

class Manifest(BaseModel):
    name: Optional[str] = "my-monorepo"
    relative_path: Optional[pl.Path] = pl.Path("src")
    description: Optional[str] = "A monorepo for my project"
    components: Optional[List[ProjectTemplate]] = []


    def to_graphviz_digraph(self) -> Digraph:
        dg = Digraph(name=self.name, filename="manifest", format="png")

        for component in self.components:
            fillcolor = "white"
            if component.project_type == ProjectTypeEnum.FAST_API:
                fillcolor = "slateblue1"

            name = component.project_options.name
            label = f"{component.project_options.name}\n\n{component.project_options.description}"
            
            dg.node(
                name=name,
                label=label,
                shape="box",
                style="filled",
                fillcolor=fillcolor
            )

            for dependency in component.dependencies:
                dg.edge(tail_name=dependency.name, head_name=name)

        return dg


    def to_yaml(self) -> None:
        with open(MANIFEST_FILE_NAME, "w") as f:
            yaml.dump(
                data=self.model_dump(mode="json"), 
                stream=f,
                default_flow_style=False,
                sort_keys=False
            )
