import lingtypology

#Get the table for UPSID dataset
p = lingtypology.db_apis.Phoible(subset='SPA')
df = p.get_df(strip_na=['tones'])
df.head().to_csv('tables/phoible.csv')

m = lingtypology.LingMap(df.language)
m.colormap_colors = ('white', 'red')
m.add_features(df.tones, numeric=True)
m.legend_title = 'Tones'
m.save_static('images/phoible.png')
