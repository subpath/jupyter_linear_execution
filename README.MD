# Jupyter linear execution

Assure that your jupyter's cells executed in order

## Good:
<img width="402" alt="image" src="https://user-images.githubusercontent.com/11722602/179580929-f496e762-b69a-4abe-b197-47d2f95a3f31.png">

## Bad:
<img width="687" alt="image" src="https://user-images.githubusercontent.com/11722602/179581148-314b01e0-a63a-4cde-99b7-e841e37de84e.png">

## Use as pre-commit hook:

```yaml
# .pre-commit-config.yaml
- id: jupyter_linear_execution
  name: jupyter_linear_execution
  description: assure jupyter linear execution
  entry: jupyter_linear_execution
  language: python

```
