import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
chromdriverpath = r"C:\Users\ameil\chromedriver.exe"
start_url = f"https://members.fantasyfootballscout.co.uk/player-stats/defenders/goal-threat/"
user_id = os.environ.get("FFS_USERNAME")
password = os.environ.get("FFS_PASSWORD")

seasons = [2020]


player_tables = ["expected"]

player_tables = ["expected"]

team_tables=["goal-threat","defending","expected"]
cwd=Path(os.getcwd())
player_stored_path=rf"{str(cwd.absolute())}/data/player data"
team_stored_path =rf"{str(cwd.parent.absolute())}/data/team data"

