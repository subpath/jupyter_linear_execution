import argparse
import json
from typing import List


def load_jupyter_to_json(path: str):
    with open(path, "r") as f:
        notebook = json.load(f)
    return notebook


def get_code_cells(notebook_dict):
    return [cell for cell in notebook_dict["cells"] if cell["cell_type"] == "code"]


def get_execution_counts(code_cells):
    return [
        cell["execution_count"]
        for cell in code_cells
        if cell.get("execution_count") is not None
    ]


def cells_executed_in_order(executions: List[int]) -> bool:
    assert isinstance(executions, list)
    if executions:
        for index, value in enumerate(executions[1:]):
            if value <= executions[index]:
                return False
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Check linear execution of the jupyter cells"
    )
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()
    bad_notebooks = []
    for filename in args.filenames:
        if filename.endswith(".ipynb"):
            if not cells_executed_in_order(
                get_execution_counts(get_code_cells(
                    load_jupyter_to_json(filename)))
            ):
                bad_notebooks.append(filename)
    if bad_notebooks:
        for notebook in bad_notebooks:
            print(f"{notebook} is not executed linearly")
        return exit(1)


if __name__ == "__main__":
    main()
