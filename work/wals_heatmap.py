import lingtypology

#Get WALS page 1A
wals = lingtypology.db_apis.Wals('1A')
data = wals.get_df()
#Write dataframe to CSV
data.head().to_csv('tables/Wals1A.csv')

#First initialize LingMap without languages
m = lingtypology.LingMap()
#Add heatmap from  the Wals data where the inventory is large
m.add_heatmap(data[data._1A_desc == 'Large'].coordinates)
#Add title
m.title = 'Large Consonant Inventories'
#Save as PNG
m.save_static('images/WalsHeatmap.png')
