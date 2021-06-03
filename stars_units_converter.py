import pandas as pd

headers = ["Star Name", "Distance (ly)", "Mass (M☉)", "Radius (R☉)"]

dwarf_stars = pd.read_csv("field_brown_dwarfs.csv", index_col = False)
dwarf_stars = dwarf_stars.dropna()

mass_column = dwarf_stars["Mass (MJ)"]
float_mass_column = mass_column.astype(float)

solar_mass_values = []
for value in float_mass_column:
    value = value * 0.000954588
    solar_mass_values.append(value)

dwarf_stars["Mass (MJ)"] = solar_mass_values

radius_column = dwarf_stars["Radius (RJ)"]
float_radius_column = radius_column.astype(float)

solar_radius_values = []
for value in float_radius_column:
    value = value * 0.102763
    solar_radius_values.append(value)

dwarf_stars["Radius (RJ)"] = solar_radius_values

dwarf_stars.to_csv("dwarf_stars_data_converted.csv", index = False, header = headers)
print("CSV file created!")