import unittest

from jupyter_linear_execution.main import *


class testLinearExecution(unittest.TestCase):

    def test_cells_executed_in_order(self):

        self.assertFalse(cells_executed_in_order([1, 2, 3, 4, 6, 7, 5]))
        self.assertTrue(cells_executed_in_order([1, 2, 3, 4, 5, 6]))
        self.assertFalse(cells_executed_in_order(
            get_execution_counts(
                get_code_cells(load_jupyter_to_json(
                    "example/bad_notebook.ipynb"))
            )
        ))
        self.assertTrue(cells_executed_in_order(
            get_execution_counts(
                get_code_cells(load_jupyter_to_json(
                    "example/valid_notebook.ipynb"))
            )
        ))


if __name__ == '__main__':
    unittest.main()
