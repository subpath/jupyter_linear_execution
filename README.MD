# Jupyter linear execution checker

Assure that your jupyter's cells executed in order

## Good:
<img width="402" alt="image" src="https://user-images.githubusercontent.com/11722602/179580929-f496e762-b69a-4abe-b197-47d2f95a3f31.png">

## Bad:
<img width="687" alt="image" src="https://user-images.githubusercontent.com/11722602/179581148-314b01e0-a63a-4cde-99b7-e841e37de84e.png">

## Use as pre-commit hook:

add this to your `.pre-commit-config.yaml`
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/subpath/jupyter_linear_execution
    rev: v0.1.0 # or some other latest tag from this repo
    hooks:
      - id: jupyter-linear-execution
```
