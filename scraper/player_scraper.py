from scraper.scraper_functions import get_historicals_by_gw
from scraper.scraper_constants import seasons, player_tables, player_stored_path,gameweeklist
import numpy as np
import os

import logging

def player_scraper():

    logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')

    logging.info("Scraping Player Data")
    ffs_tables = [f'{x}_' + str(season) for season in seasons for x in player_tables]
    ffs_df_dict = {}
    for season in seasons:
        for feature in player_tables:
            df = get_historicals_by_gw(str(season), gameweeklist, feature)
            ffs_df_dict[f"{feature}_{season}"] = df
            print(f"Scraped {feature, season}")

    for table in ffs_tables:
        output_file_path = os.path.join(player_stored_path, f"{table}")
        ffs_df_dict[table].to_csv(output_file_path)
