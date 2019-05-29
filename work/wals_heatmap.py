import lingtypology

wals = lingtypology.db_apis.Wals('1A')
data = wals.get_df()
data.head().to_csv('tables/Wals1A.csv')
