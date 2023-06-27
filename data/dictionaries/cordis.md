# CORDIS
 
Tables available from CORDIS data about EU funded research and innovation
projects.

 - [Organisations](#organisations)
 - [Project Organisations](#project-organisations)
 - [Project Proposal Calls](#project-proposal-calls)
 - [Project Topics](#project-topics)
 - [Projects](#projects)
 - [Proposal Calls](#proposal-calls)
 - [Publications](#publications)
 - [Publications](#publications)
 - [Reports](#reports)
 - [Topics](#topics)

### Organisations
 
Details of organisations involved in CORDIS projects.
 
```python 
from igl_data.data.cordis import cordis_table
cordis_orgs_df = cordis_table('organisations')
```

- **`id`** (`int`): Organisation ID.
- **`name`** (`str`): Organisation name.
- **`country_code`** (`str`): 2 letter alpha ISO country code.
- **`country_name`** (`str`):


### Project Organisation
 
Links projects to organisations.

```python 
from igl_data.data.cordis import cordis_table
cordis_orgs_df = cordis_table('project_organisations')
```

- **`project_rcn`** (`int`): Project ID.
- **`organisation_id`** (`int`): Organisation ID.
- **`address`** (`json`): 
- **`contribution`** (`int`): Project funding awarded to organisation.
- **`type`** (`str`): Role of org in project.
- **`website`** (`str`):


### Project Proposal Calls
 
A link table to connect projects to proposal calls.

```python 
from igl_data.data.cordis import cordis_table
cordis_orgs_df = cordis_table('project_proposal_calls')
```

- **`project_rcn`** (`int`): Project ID.
- **`rcn`** (`int`): Proposal ID.


### Project Topics
 
A link table to connect projects to topics.

```python 
from igl_data.data.cordis import cordis_table
cordis_orgs_df = cordis_table('project_topics')
```

- **`project_rcn`** (`int`): Project ID.
- **`rcn`** (`int`): Topic ID.


### Projects
 
A link table to connect projects to topics.

```python 
from igl_data.data.cordis import cordis_table
cordis_orgs_df = cordis_table('projects')
```

- **`rcn`** (`int`): Project ID.
- **`acronym`** (`int`): Short project name or acronym.
- **`end_date_code`** (`datetime`): 
- **`ec_contribution`** (`int`): Funding amount awarded by EU.
- **`framework`** (`str`): EU framework programme (FP7 or H2020).
- **`funding_scheme`** (`str`): Type of funding.
- **`funded_under`** (`json`): Proposal calls.
- **`objective`** (`str`): Project objective.
- **`project_description`** (`str`): Project description.
- **`start_date_code`** (`datetime`):
- **`status`** (`str`):
- **`title`** (`str`):
- **`total_cost`** (`int`): Total cost of project including funding awarded by EU.
- **`website`** (`str`):


### Proposal Calls
 
Proposal call IDs and descriptions.

```python 
from igl_data.data.cordis import cordis_table
cordis_orgs_df = cordis_table('proposal_calls')
```

- **`rcn`** (`int`): Call ID.
- **`title`** (`str`): Title of proposal call.


### Publications

Publications arising from projects collected from OpenAIRE.

```python 
from igl_data.data.cordis import cordis_table
cordis_orgs_df = cordis_table('publications')
```

- **`id`** (`int`): OpenAIRE ID.
- **`project_rcn`** (`int`): Project Id.
- **`authors`** (`list`):
- **`url`** (`str`):
- **`pid`** (`list`): Publisher publication ID.
- **`publisher`** (`str`):
- **`title`** (`str`):


### Reports
 
Project outcomes.

```python 
from igl_data.data.cordis import cordis_table
cordis_orgs_df = cordis_table('reports')
```

- **`rcn`** (`int`): Report ID.
- **`project_rcn`** (`int`): Project ID.
- **`teaser`** (`str`):
- **`summary`** (`str`):
- **`title`** (`str`):


### Topics

Topic descriptions.

```python 
from igl_data.data.cordis import cordis_table
cordis_orgs_df = cordis_table('description')
```

- **`rcn`** (`int`): Topic ID.
- **`title`** (`str`):
