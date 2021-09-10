from scraper.team_scraper import team_scraper
from scraper.player_scraper import player_scraper
from scraper.results_scraper import results_scraper
from database_create import database_create


team_scraper()
results_scraper()
player_scraper()
database_create()