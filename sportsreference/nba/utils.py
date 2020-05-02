
from pyquery import PyQuery as pq
from .constants import SEASON_PAGE_URL


def _determine_leagues_from_year(year):
    if 1950 <= year <= 1967:
        leagues = ['NBA']
    elif 1968 <= year <= 1976:
        leagues = ['NBA', 'ABA']
    elif 1947 <= year <= 1949:
        leagues = ['BAA']
    else:
        leagues = ['NBA']
    return leagues


def _generate_season_page_url(year, league):
    return pq(SEASON_PAGE_URL.replace('NBA', league) % year)
