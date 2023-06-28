import pandas as pd
import numpy as np
import numpy.testing as npt
import pytest

from igl_data.data.arxiv import (
    arxiv_table,
    arxiv_articles,
    arxiv_sample_2017
)

from igl_data.data.cordis import (
    cordis_table,
    cordis_table_list,
    h2020_projects
)

from igl_data.data.gis import (
    country_basic_info
)

from igl_data.data.grid import (
    grid_table
)

from igl_data.data.gtr import (
    gtr_sample,
    gtr_table,
    gtr_link_table,
    gtr_table_list
)

from igl_data.data.mag import (
    mag_table
)

from igl_data.data.meetup import (
    meetups
)

from igl_data.data.ons import (
    patents_100k,
    patents_10k
)

from igl_data.data.sdg import (
    sdg_web_articles
)

from igl_data.data.world_report import (
    world_report_mesh
)

from igl_data.data.google_patents import (
    google_patents,
    list_countries
)

from igl_data.data.openalex import (
    openalex,
    cols_to_function
)

@pytest.mark.arxiv
@pytest.mark.parametrize("table", [
    'article_categories', 
    'article_corex_topics', 
    'article_fields_of_study', 
    'article_institutes', 
    'categories', 
    'corex_topics'
])
def test_arxiv_table(table):
    df = arxiv_table(table)
    assert isinstance(df, pd.DataFrame)

@pytest.mark.arxiv
@pytest.mark.parametrize("chunk", np.arange(16))
def test_arxiv_articles(chunk):
    df = arxiv_articles(chunk)
    assert isinstance(df, pd.DataFrame)

@pytest.mark.arxiv
def test_arxiv_sample_2017():
    df = arxiv_sample_2017()
    assert isinstance(df, pd.DataFrame)

@pytest.mark.cordis
@pytest.mark.parametrize("table", cordis_table_list())
def test_cordis_table(table):
    df = cordis_table(table)
    assert isinstance(df, pd.DataFrame)

@pytest.mark.cordis
def test_cordis_h2020():
    df = h2020_projects()
    assert isinstance(df, pd.DataFrame)

@pytest.mark.gis
def test_country_basic_info():
    df = country_basic_info()
    assert isinstance(df, pd.DataFrame)

@pytest.mark.grid
@pytest.mark.parametrize("table", [
    'aliases',
    'institutes'
])
def test_grid_table(table):
    df = grid_table(table)
    assert isinstance(df, pd.DataFrame)

@pytest.mark.gtr
@pytest.mark.parametrize("table", gtr_table_list())
def test_gtr_table(table):
    df = gtr_table(table)
    assert isinstance(df, pd.DataFrame)
    
@pytest.mark.gtr
@pytest.mark.parametrize("table", gtr_table_list())
def test_gtr_link_table(table):
    if table != 'organisations_locations':
        df = gtr_link_table(table)
        assert isinstance(df, pd.DataFrame)

@pytest.mark.gtr
def test_gtr_sample():
    df = gtr_sample()
    assert isinstance(df, pd.DataFrame)

@pytest.mark.mag
def test_mag_table():
    df = mag_table()
    assert isinstance(df, pd.DataFrame)

@pytest.mark.meetup
def test_meetups():
    df = meetups()
    assert isinstance(df, pd.DataFrame)

@pytest.mark.ons
def test_patents_100k():
    df = patents_100k()
    assert isinstance(df, pd.DataFrame)

@pytest.mark.ons
def test_patents_10k():
    df = patents_10k()
    assert isinstance(df, pd.DataFrame)

@pytest.mark.sdg
def test_sdg_web_articles():
    df = sdg_web_articles()
    assert isinstance(df, pd.DataFrame)

@pytest.mark.world_report
def test_world_report_mesh():
    df = world_report_mesh()
    assert isinstance(df, pd.DataFrame)

@pytest.mark.google_patents
@pytest.mark.parametrize("country", list_countries())
def test_google_patents(country):
    df = google_patents(country)
    assert isinstance(df, pd.DataFrame)

@pytest.mark.openalex
@pytest.mark.parametrize("col", cols_to_function().keys())
def test_openalex(col):
    df = openalex(col)
    assert isinstance(df, pd.DataFrame)

if __name__ == "__main__":
    pytest.main()
    #  run with pytest -m arxiv to run the arxiv tests