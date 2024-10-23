from InquirerPy import prompt

from tigr81.commands.scaffold.project_template import (
    ICON_MAPPING,
    ProjectTypeEnum,
)


def select_project_type_interactive() -> ProjectTypeEnum:
    """Prompt user to select a project type interactively"""
    choices = [{"name": f"{ICON_MAPPING[pt]} {pt.name}", "value": pt} for pt in ProjectTypeEnum]
    questions = [
        {
            "type": "list",
            "name": "project_type",
            "message": "Select the project type to scaffold",
            "choices": choices,
        }
    ]
    answers = prompt(questions)
    return answers["project_type"]
