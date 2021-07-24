import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
chromdriverpath = r"C:\Users\ameil\chromedriver.exe"
start_url = f"https://members.fantasyfootballscout.co.uk/player-stats/defenders/goal-threat/"
user_id = os.environ.get("FFS_USERNAME")
password = os.environ.get("FFS_PASSWORD")

seasons=[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

player_tables = ["involvement", "distribution", "goal-threat", "defending", "set-pieces","kpi-attacking","kpi-defending","expected"]

team_tables=["goal-threat", "defending","expected"]
cwd=Path(os.getcwd())
player_stored_path=rf"{str(cwd.absolute())}/data/player data"
team_stored_path =rf"{str(cwd.absolute())}/data/team data"

