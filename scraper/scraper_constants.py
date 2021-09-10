import os
from pathlib import Path
from dotenv import load_dotenv
import numpy as np

load_dotenv()
chromdriverpath = r"C:\Users\ameil\chromedriver.exe"
start_url = f"https://members.fantasyfootballscout.co.uk/player-stats/defenders/goal-threat/"
user_id = os.environ.get("FFS_USERNAME")
pw = os.environ.get("FFS_PASSWORD")

seasons=[2011]
gameweeklist = list(np.arange(1, 39))
player_tables = ["involvement", "distribution", "goal-threat", "defending", "set-pieces","kpi-attacking","kpi-defending","expected"]

team_tables=["goal-threat", "defending","expected"]
cwd=Path(os.getcwd())
os.chdir("..")
player_stored_path=r"scraper/data/player data"
team_stored_path =r"scraper/data/team data"