import json
from typing import List
import argparse


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


# TODO: move this to tests
# assert not cells_executed_in_order([1, 2, 3, 4, 6, 7, 5])
# assert cells_executed_in_order([1, 2, 3, 4, 5, 6])
# assert not cells_executed_in_order(
#     get_execution_counts(
#         get_code_cells(load_jupyter_to_json("example/bad_notebook.ipynb"))
#     )
# )
# assert cells_executed_in_order(
#     get_execution_counts(
#         get_code_cells(load_jupyter_to_json("example/valid_notebook.ipynb"))
#     )
# )


def main():
    parser = argparse.ArgumentParser(
        description="Check linear execution of the jupyter cells"
    )
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()
    for filename in args.filenames:
        if filename.endswith(".ipynb"):
            assert cells_executed_in_order(
                get_execution_counts(get_code_cells(
                    load_jupyter_to_json(filename)))
            ), f"cells are not executed in order: {filename}"


if __name__ == "__main__":
    main()
