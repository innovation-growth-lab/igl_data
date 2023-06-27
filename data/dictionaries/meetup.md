# Meetup

Data from [meetup.com](https://meetup.com). 

### Meetup Groups

Mostly tech focused meetups from the EU and US.

```python from igl_data.data import meetup

meetup_groups_df = meetup.meetups()
```

- **`category`** (`int`):
- **`category_id`** (`int`)
- **`category_name`** (`string`):
- **`category_shortname`** (`string`):
- **`city`** (`string`):
- **`country`** (`string`):
- **`country_code`** (`string`):
- **`country_name`** (`string`):
- **`created`** (`int`):
- **`created_at`**
- **`db`** (`string`):
- **`description`** (`string`):
- **`group_name`** (`string`):
- **`id`** (`list of int`:)
- **`lang`** (`string`):
- **`lat`** (`float`):
- **`lon`** (`float`):
- **`members`** (`int`):
- **`name`** (`string`):
- **`timestamp`** (`datetime`):
- **`topics`** (`list of dict`):
- **`urlkey`** (`string`:)
- **`urlname`** (`string`):
- **`year`** (`int`):
- **`topic_names`** (`list of string`):
