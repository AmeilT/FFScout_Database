import os
from pathlib import Path
from dotenv import load_dotenv
import numpy as np

load_dotenv()
chromdriverpath = r"C:\Users\ameil\chromedriver.exe"
start_url = f"https://members.fantasyfootballscout.co.uk/player-stats/defenders/goal-threat/"
user_id = os.environ.get("FFS_USERNAME")
password = os.environ.get("FFS_PASSWORD")

seasons=[2021]
gameweeklist = list(np.arange(1, 2))
player_tables = ["involvement", "distribution", "goal-threat", "defending", "set-pieces","kpi-attacking","kpi-defending","expected"]

team_tables=["goal-threat", "defending","expected"]
cwd=Path(os.getcwd())
player_stored_path=rf"{str(cwd.absolute())}/data/player data"
team_stored_path =rf"{str(cwd.absolute())}/data/team data"