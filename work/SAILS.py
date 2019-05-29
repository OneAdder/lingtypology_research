import lingtypology

#Get SAILS data for pages 'ICU3' and 'ICU4'
sails = lingtypology.db_apis.Sails('ICU3', 'ICU4')
df = sails.get_df()
df.head().to_csv('tables/sails.csv')

m = lingtypology.LingMap(df.language)
m.add_features(df.ICU3_desc)
#Use page description as legend title
m.legend_title = sails.feature_descriptions('ICU3').Description.at[0]
m.start_location = (9, -79)
m.start_zoom = 5
m.legend_position = 'bottomleft'
m.save_static('images/sails.png')
