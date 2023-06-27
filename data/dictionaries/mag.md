# Microsoft Academic Graph
 
Tables available from Microsoft Academic Graph. MAG is a large graph database containing over 127 million academic publications, along with authors, abstracts, institutions. It can be accessed via API.

 - [Fields of Study](#fields-of-study) 

### Fields of Study

Microsoft Academic Graph is enriched with a field of study taxonomy, covering research disciplines and topics. It is hierarchical, and contains over 600,000 entities.
 
```python 
from igl_data.data.mag import mag_table
mag_fos_df = mag_table('fos')
```

- **`id`** (`int`): MAG FoS ID.
- **`name`** (`str`): Name of field of study.
- **`level`** (`int`): Level in the hierarchy. Lower numbers are less granular research disciplines or areas, lower numbers are more detailed research topics and concepts.
- **`parent_ids`** (`list`): MAG FoS IDs of parent fields.
- **`child_ids`** (`list`): MAG FoS IDs of child fields.
