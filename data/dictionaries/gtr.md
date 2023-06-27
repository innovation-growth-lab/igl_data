# Gateway to Research

Tables available from Gateway to Research. Funders include AHRC, BBSRC, EPSRC, ESRC, Innovate UK, MRC, NC3Rs, NERC and STFC.

  - [Projects Sample](#projects_sample)
  - [Funds](#funds)
  - [Organisations](#organisations)
  - [Organisation Locations](#organisations-locations)
  - [Outcomes](#outcomes)
  - [Participant](#participant)
  - [Persons](#persons)
  - [Projects](#projects)
  - [Topic](#topic)
  - [Link Tables](#link-tables)

### Projects Sample

A sample dataset of Gateway to Research projects with some metadata.

```python 
from igl_data.data.gtr import gtr_sample 
gtr_project_sample_df = gtr_sample()
``` 

This dataset contains basic information about the content, year and funder of
a project in Gateway to Research.

- **`project_id`** `(string)`: A URL with a unique ID for the project. The URL links to an XML representation of the project on GtR 
- **`start_year`** `(int)`: The year that the project began. Minimum value of 1975 and maximum of 2019.
- **`research_topics`** `(list of strings)`: A list of project research topics. There are 607 topics.
- **`research_subjects`** `(list of strings)`: A list of project research subjects. There are 82 subjects.
- **`abstract_texts`** `(string)`: Full text of abstract that describes the project.
- **`funder_name`** `(string)`: Acronym of funder.


### Funds

Funding amounts and types.

:warning: This table contains duplicates.

:warning: The fund dates range from start dates in 1975 and end dates in 2121. This may be due to errors. The majority of funds are between 2006 and 2018.

```python 
from igl_data.data.gtr import gtr_table
gtr_fund_df = gtr_table('funds')
```

- **`id`** `(string)`: Fund ID.
- **`start`** `(datetime)`: Funding period start date.
- **`end`** `(datetime)`: Funding period end date.
- **`category`** `(datetime)`: Type of funding.
- **`amount`** `(datetime)`: Funding amount.
- **`currencyCode`** `(datetime)`: 3 letter currency code.


### Organisations
 
Research organisation information.

```python 
from igl_data.data.gtr import gtr_table
gtr_org_df = gtr_table('organisations')
```

- **`id`** `(string)`: Org ID.
- **`name`** `(string)`: Org name.
- **`addresses`** `(json)`: Registered org addresses 


### Organisations Locations
 
Research organisation locations.

```python 
from igl_data.data.gtr import gtr_table gtr_org_loc_df
= gtr_table('organisations_locations') ```

- **`id`** `(string)`: Org ID.
- **`country_name`** `(string)`:
- **`country_alpha_2`** `(string)`: 2 letter ISO alpha country code.
- **`country_alpha_3`** `(string)`: 3 letter ISO alpha country code.
- **`country_numeric`** `(int)`: Numeric country code.
- **`continent`** `(string)`:
- **`latitude`** `(float)`:
- **`longitude`** `(float)`:


### Outcomes

There are many tables for outcomes from Gateway to Research projects, each with their own fields.

```python 
from igl_data.data.gtr import gtr_table
gtr_outcome_df = gtr_table(<outcome table name>)
```

The table names available are:

- outcomes_artisticandcreativeproducts
- outcomes_collaborations
- outcomes_disseminations
- outcomes_furtherfundings
- outcomes_impactsummaries
- outcomes_intellectualproperties
- outcomes_keyfindings
- outcomes_policyinfluences
- outcomes_products
- outcomes_publications
- outcomes_researchdatabaseandmodels
- outcomes_researchmaterials
- outcomes_softwareandtechnicalproducts
- outcomes_spinouts


### Participant

Project-organisation participation information.

```python 
from igl_data.data.gtr import gtr_table
gtr_participant_df = gtr_table('participant')
```

- **`id`** `(string)`: Participation ID.
- **`organisation_id`** `(string)`: Org ID.
- **`project_cost`** `(int)`: Total cost of project that participant was involved in.
- **`grantOffer`** `(int)`: Amount awarded to participant.


### Persons

Researchers involved in projects, e.g. PIs, students and collaborators.

```python 
from igl_data.data.gtr import gtr_table
gtr_ppl_df = gtr_table('persons')
```

- **`id`** `(string)`: Person ID.
- **`firstName`** `(string)`:
- **`otherNames`** `(string)`:
- **`lastName`** `(string)`:

### Projects

Basic project information.

```python 
from igl_data.data.gtr import gtr_table
gtr_project_df = gtr_table('projects')
```

- **`id`** `(string)`: Project ID.
- **`end`** `(datetime)`: (often NULL)
- **`title`** `(string)`: Project title.
- **`status`** `(string)`: Whether the project is ongoing or not.
- **`grantCategory`** `(string)`: Type of grant award.
- **`leadFunder`** `(string)`: Main funding body.
- **`abstractText`** `(string)`: Project description.
- **`start`** `(datetime)`: (often NULL)
- **`created`** `(datetime)`: Date that database record was created.
- **`leadOrganisationDepartment`** `(string)`:
- **`potentialImpact`** `(string)`: Impact statement for some projects.
- **`techAbstractText`** `(string)`: Extra info for BBSRC funded projects.


### Topic

Many projects in GtR are tagged with research topics. There are three categories:

- Topic: Granular (~600) research categories.
- Subject: Less granular (~90) research categories.
- Activity: Medical research categories (~50).

```python 
from igl_data.data.gtr import gtr_table
gtr_topic_df = gtr_table('topic')
```

- **`id`** `(string)`: Topic ID.
- **`text`** `(string)`: Topic description.
- **`topic_type`** `(string)`: One of *researchActivity*, *researchSubject* or *researchTopic*.


### Link Tables

There are link tables which can be used to link many of the entities above to projects. This is a many to many mapping table that has been broken down in to parts that can map a particular table to the project table.

```python 
from igl_data.data.gtr import gtr_link_table
gtr_link_df = gtr_link_table(<link table name>)
```

Every link table has the same fields. These are:

- **`id`** `(string)`: Entity ID. For example, if the link table is for funds, then this will be the fund ID.
- **`project_id`** `(string)`: The project ID that this entity is linked to.
- **`rel`** `(string)`: The relationship between the project and the entity.
- **`table_name`** `(string)`: The related table.

The link table names available are:

- funds
- organisations
- organisations_locations
- outcomes_artisticandcreativeproducts
- outcomes_collaborations
- outcomes_disseminations
- outcomes_furtherfundings
- outcomes_impactsummaries
- outcomes_intellectualproperties
- outcomes_keyfindings
- outcomes_policyinfluences
- outcomes_products
- outcomes_publications
- outcomes_researchdatabaseandmodels
- outcomes_researchmaterials
- outcomes_softwareandtechnicalproducts
- outcomes_spinouts
- participant
- persons
- projects
- topic


