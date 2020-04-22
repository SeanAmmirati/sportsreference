
from pyquery import PyQuery as pq
from .constants import SEASON_PAGE_URL


def _determine_leagues_from_year(year):
    if 1960 <= year <= 1969:
        leagues = ['NFL', 'AFL']
    elif 1946 <= year <= 1949:
        leagues = ['NFL', 'AAFC']
    elif 1950 <= year <= 1959:
        leagues = ['NFL']
    elif 1920 <= year <= 1921:
        leagues = ['APFA']
    else:
        leagues = ['NFL']
    return leagues


def _generate_season_page_url(year, league):
    if league == 'NFL':
        return pq(SEASON_PAGE_URL % year)
    else:
        return pq(SEASON_PAGE_URL % (year + f'_{league}'))
