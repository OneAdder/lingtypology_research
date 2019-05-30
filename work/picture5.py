import lingtypology

df = lingtypology.db_apis.Phoible(subset='UPSID', aggregated=False).get_df()
#Get all languages with ejectives
df = df[df.raisedLarynxEjective == '+']
#Remove duplicates
df = df.drop_duplicates(subset='Glottocode')

m = lingtypology.LingMap(df.Glottocode, glottocode=True)
#Tiles with terrain
m.tiles = 'Stamen Terrain'
m.title = 'Languages with Ejectives'
m.radius = 5
m.opacity = 0.5
m.colors = ('blue',)
m.save_static('images/Picture6.png')
