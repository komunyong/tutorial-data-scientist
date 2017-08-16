import pandas as pd
import numpy as np

def is_weekend(dayofweek):
    if dayofweek == 5 or dayofweek == 6:
        return 1
    else:
        return 0

def quarter_time(hour):
    if hour > 6 and hour <= 9:
        return 0 # 'morning'
    elif hour > 9 and hour <= 18:
        return 1 # 'working_time'
    elif hour >18 and hour <= 22:
        return 2 # 'evening'
    elif hour > 22 and hour <= 24 or hour >= 0 and hour <= 6:
        return 3 # 'sleep'

def unique_cat(categories):
    unique_categories = []
    for cat in categories:
        if cat.strip() and cat is not None:
            unique_categories.append(cat)
    return unique_categories

def word_matrix(row):
    input_list = row['bought_categories']
    for x in input_list:
        row[x] += 1
    return row

def discretize(df_column, bins):
    col = df_column.as_matrix()
    col_bin = np.array(bins)
    return pd.DataFrame(np.digitize(col, col_bin, right=True))


# Saved parameters

# parent_categories = ['lifestyle', 'men_fashion', 'women_fashion']
# bought_categories = [
#     'all', 'lifestyle_crafts', 'lifestyle_for_home', 'lifestyle_gadget_tech', 
#     'lifestyle_gift_ideas', 'lifestyle_other', 'lifestyle_phone_accessories', 'lifestyle_sports', 
#     'lifestyle_stationeries', 'men_bags_wallets', 'men_glasses', 
#     'men_hats', 'men_jewelry', 'men_pants', 'men_shoes', 'men_shorts', 'men_tops', 
#     'men_underwear', 'men_watches', 'women_bags_wallets', 'women_dresses', 
#     'women_glasses', 'women_hats', 'women_jackets_blazers', 
#     'women_jewelry', 'women_other', 'women_pants_leggings', 'women_shoes', 
#     'women_shorts', 'women_skirts', 'women_sports', 'women_swimwear', 'women_tops', 
#     'women_watches'
# ]

# Find all noise category to remove
# parent_categories = list()
# for index, row in df['bought_categories'].iteritems():
#     for cat in row:
#         if cat not in parent_categories and cat.strip() and cat is not None:
#             parent_categories.append(cat)
# parent_categories.sort()