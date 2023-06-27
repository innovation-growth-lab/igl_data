# Geographic

Small datasets containing useful geographic information.

### Basic Country Info

```python from igl_data.data import gis

country_df = gis.country_basic_info() 
```

A table of basic information about countries.

- **`alpha2Code`** (`string`):
- **`alpha3Code`** (`string`):
- **`altSpellings`** (`list of string`):
- **`area`** (`float`):
- **`borders`** (`list of string`):
- **`callingCodes`** (`list of int`):
- **`capital`** (`string`):
- **`cioc`** (`string`):
- **`currencies`** (`list of dict`):
- **`demonym`** (`string`):
- **`flag`** (`string`):
- **`gini`** (`float`):
- **`languages`** (`list of dict`):
- **`latlng`** (`list of float`):
- **`name`** (`string`):
- **`nativeName`** (`string`):
- **`numericCode`** (`int`):
- **`population`** (`int`):
- **`region`** (`string`):
- **`regionalBlocs`** (`list of dict`):
- **`subregion`** (`string`):
- **`timezones`** (`list of string`):
- **`topLevelDomain`** (`list of string`):
- **`translations`** (`list of dict`):
- **`lat`** (`float`):
- **`lng`** (`float`):
- **`continent`** (`string`):
