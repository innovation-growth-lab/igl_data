IGL Tutorial Material
=====================

Welcome to IGL's tutorial material repository! 📚

## Introduction

This is a forked version of Nesta's [Innovation Mapping tutorials](https://github.com/nestauk/im_tutorials). Here you will find all relevant data for IGL tutorials, including data dictionaries. Past tutorials covering practical implementations of data science techniques including data collection, machine learning, natural language processing, network science and data visualisation can be found in the archived repository.

## Data

Open datasets are made available to download or pull in to notebooks directly. This can be done easily using functions available in the `igl_data` package, which load data straight into Pandas DataFrames. For example, if we want to load projects from Gateway to Research, we can simply do:

```python
from igl_data.data.gtr import gtr_table
gtr_projects_df = gtr_table('projects')
```

More information on the datasets available and how to access them can be found in the [data dictionaries](https://github.com/nestauk/im_tutorials/tree/master/data).
