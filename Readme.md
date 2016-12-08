# pyProjectNameGenerator

A project name generator, based on the
[original javascript implementation](https://github.com/aceakash/project-name-generator)
for quirky names like *spiffy-waterfall*, *mature-dew-8239* to use wherever you
need a random memorable name.

Useful for object names, temp folders, passwords, project names, unique ids, etc.


## Install

## Quick Start
```
>>> from project_name_generator import generate
>>> generate(words=3, number=True, alliterative='c')
{'raw': ['cluttered', 'condemned', 'corn', '4913'], 'spaced': 'cluttered condemned corn 4913', 'dashed': 'cluttered-condemned-corn-4913'}
>>> generate()
{'raw': ['nappy', 'cannon'], 'spaced': 'nappy cannon', 'dashed': 'nappy-cannon'}
```

## How To Use

## Tests

## More
