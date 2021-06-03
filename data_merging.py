import pandas as pd

brightest_stars = pd.read_csv("brightest_stars.csv")
dwarf_stars = pd.read_csv("dwarf_stars_data_converted.csv")

brightest_stars["Mass (M☉)"] = pd.to_numeric(brightest_stars["Mass (M☉)"], errors = 'coerce')
brightest_stars["Radius (R☉)"] = pd.to_numeric(brightest_stars["Radius (R☉)"], errors = 'coerce')

brightest_stars = brightest_stars.dropna()

dwarf_stars["Distance (ly)"] = dwarf_stars["Distance (ly)"].astype(object)

star_data = brightest_stars.merge(dwarf_stars, how = 'outer')

star_data.to_csv("final_star_data.csv", index = False)
print("CSV file created!")