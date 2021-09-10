import os
from pathlib import Path

seasons=[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
tables = ["involvement", "distribution", "goal-threat", "defending", "set-pieces", "kpi-attacking", "kpi-defending","expected"]
cwd=Path(os.getcwd())
player_data_file_path=rf"{str(cwd.parent.absolute())}/scraper/data/player data"
team_data_file_path=rf"{str(cwd.parent.absolute())}/scraper/data/team data"

#Large file so save outside of repo
dataframe_save_path=rf"{str(cwd.parent.parent.absolute())}"
