# GRID
 
Tables available from the Global Researcher Identifier Database.

 - [Aliases](#aliases)
 - [Institutes](#institutes)

### Aliases
 
Alternative names for GRID institutes.
 
```python 
from igl_data.data.grid import grid_table
grid_alias_df = grid_table('aliases')
```

- **`id`** (`int`): Database row ID.
- **`grid_id`** (`str`): GRID institute ID.
- **`alias`** (`str`): Alias institute name.


### Institutes
 
Name and location of GRID institutes.
 
```python 
from igl_data.data.grid import grid_table
grid_alias_df = grid_table('institutes')
```

- **`id`** (`int`): GRID institute ID.
- **`name`** (`str`): Institute name.
- **`address_line_1`** (`str`):
- **`address_line_2`** (`str`):
- **`address_line_3`** (`str`):
- **`city`** (`str`):
- **`geonames_city_id`** (`str`):
- **`state`** (`str`):
- **`state_code`** (`str`):
- **`country`** (`str`):
- **`country_code`** (`str`): 2 letter ISO alpha country code.
- **`latitude`** (`float`):
- **`longitude`** (`float`):


