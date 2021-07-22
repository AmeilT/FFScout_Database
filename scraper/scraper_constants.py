import os
from pathlib import Path

chromdriverpath = r"YOUR CHROMEDRIVER PATH"
start_url = f"https://members.fantasyfootballscout.co.uk/player-stats/defenders/goal-threat/"
user_id = "Your UserName"
password = "Your Password"
seasons = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
player_tables = ["involvement", "distribution", "goal-threat", "defending", "set-pieces", "kpi-attacking", "kpi-defending"]
team_tables=["goal-threat","defending"]
cwd=Path(os.getcwd())
player_stored_path=rf"{str(cwd.absolute())}/data/player data"
team_stored_path =rf"{str(cwd.parent.absolute())}/data/team data"
