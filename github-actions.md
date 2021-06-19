# GitHub Actions

## Events that trigger workflows


```yml

# Manual
on: workflow_dispatch

# Triggered when code is pushed to any branch in a repository
on: push

# Triggers the workflow on push or pull request events
on: [push, pull_request]

# Triggers on schedule
on:
  schedule:
    # * is a special character in YAML so you have to quote this string
    - cron:  '30 5,17 * * *'

```
