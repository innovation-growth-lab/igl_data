# Sustainable Development Goals

Data from projects involving the sustainable development goals.

 - [SDG Web Articles](#sdg-web-articles) 

### SDG Web Articles

A set of articles collected from the web that describe SDG related activities, with SDG labels.
 
```python 
from igl_data.data.sdg import sdg_web_articles
sdg_df = sdg_web_articles()
```

- **`index`** (`int`): Row ID.
- **`title`** (`str`): Articles title.
- **`url`** (`str`): Original article URL.
- **`text`** (`str`): Article body text.
- **`sdg_goals`** (`list of int`): Labels corresponding to SDG goal numbers.
- **`source`** (`str`): Original website name. Includes [RELX](https://sdgresources.relx.com/) and [IISD](http://sdg.iisd.org).
