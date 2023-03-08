from Autodesk.Revit.DB import Transaction, XYZ, BuiltInParameter, BuiltInCategory, FilteredElementCollector, ImportInstance
import Autodesk.Revit.DB as DB
doc = __revit__.ActiveUIDocument.Document
op = doc.Application.Create.NewGeometryOptions()
op.ComputeReferences = True
op.IncludeNonVisibleObjects = True
t = Transaction(doc)

fec = FilteredElementCollector(doc, doc.ActiveView.Id)
fec2 = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_CLines)
c = doc.Settings.Categories.get_Item(BuiltInCategory.OST_Lines)

sub = c.SubCategories

for line in sub:
	if line.Name.Contains("ME-WALL"):
		me_wall = line
		#print(me_wall)
geo = []
eles = []
for ele in fec:
	if ele.GetType().Equals(ModelLine):
		geo.append(ele.get_Geometry(op))
		eles.append(ele)
		#print(ele.get_Geometry(op).GetType())
	
g = geo[0]
e = eles[0]
#print(g, e)
me_walls = []
for ln in eles:
	if ln.LineStyle.Name == "ME-WALL":
		# me_walls.append(doc.Create.NewLine())
		t.Start("Ref")
		doc.Create.NewSpaceBoundaryLines(doc.ActiveView.SketchPlane, ln, doc.ActiveView)
		t.Commit()