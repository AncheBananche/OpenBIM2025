# BIManalyst group 02

Focus Area: We will be choosing to focus on the architectural components of this ifc file such as number of desks, facade transparency, floors, gross floor area (GFA).

Claim: 200 permanent desk spaces (pg.2, 25-06-D-ARCH Client Report)

Findings:
import ifcopenshell

# Path to IFC file
model_path = "/Users/annadavies/Desktop/25-16-D-ARCH.ifc"
model = ifcopenshell.open(model_path)

# Get all IfcBuildingElementProxies
proxies = model.by_type("IfcBuildingElementProxy")

# Search substring (lowercase for safety)
target_substring = "furniture_office-desks-tables_lavoro-design_advance"

desks = [p for p in proxies if p.Name and target_substring in p.Name.lower()]

print(f"Desks: {len(desks)}")

Result: 420 Desks Found. (Claim is FALSE)

# Description of Code
The code stated above is scanning through the .ifc file for the number of desks found with the name "furniture_office-desks-tables_lavoro-design_advance". The script opens up the model and finds all related objects with that title and then prints the number at the end.
