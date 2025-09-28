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
