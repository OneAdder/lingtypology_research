import os
os.chdir('images')
import lingtypology

wals_page = lingtypology.db_apis.Wals('1a', '2a').get_df()
m = lingtypology.LingMap(wals_page.language)
m.add_custom_coordinates(wals_page.coordinates)
m.add_features(wals_page._1A)
m.legend_title = 'Consonant Inventory'
m.colors = lingtypology.gradient(5, 'yellow', 'green')
m.unstroked = False
m.save_static('FoliumStrokeAppearance.png')
 
