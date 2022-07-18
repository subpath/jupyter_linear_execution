# Jupyter linear execution

Assure that your jupyter's cells executed in order

## Good:


## Bad:

## Use as pre-commit hook:

```yaml
# .pre-commit-config.yaml
- id: jupyter_linear_execution
  name: jupyter_linear_execution
  description: assure jupyter linear execution
  entry: jupyter_linear_execution
  language: python

```