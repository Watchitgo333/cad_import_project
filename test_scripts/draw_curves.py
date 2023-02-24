from Autodesk.Revit.DB import Transaction, XYZ, Line, PolyLine, BuiltInParameter, BuiltInCategory, FilteredElementCollector, ImportInstance
import Autodesk.Revit.DB as DB
doc = __revit__.ActiveUIDocument.Document

fec = FilteredElementCollector(doc).OfClass(ImportInstance).WhereElementIsNotElementType()
op = doc.Application.Create.NewGeometryOptions()
op.ComputeReferences = True
op.IncludeNonVisibleObjects = True

for ele in fec:
	if ele.Category.Name == "22150_FP.dwg":
		dwg = ele

#geo = dwg.GetGeometryObjectFromReference(op)
trans = dwg.GetTransform()

geo = dwg.get_Geometry(op)

for g in geo:
	geoInst = g

lines = []
polys = []
for geoEle in geoInst.GetInstanceGeometry():
	if geoEle.GetType().Equals(Line):
		lines.append(geoEle)
	elif geoEle.GetType().Equals(PolyLine):
		polys.append(geoEle)

me_polys = []
for poly in polys:
    name = DB.Document.GetElement(doc, poly.GraphicsStyleId)
    if name.GraphicsStyleCategory.Name.Contains("ME-WALL"):
        me_polys.append(poly)

t = Transaction(doc)

#creates curves with polylines
def get_me_lines():
    me_lines = []
    for ln in lines:
        ln_name = DB.Document.GetElement(doc, ln.GraphicsStyleId)
        #print(ln_name.GraphicsStyleCategory.Name)
        if ln_name.GraphicsStyleCategory.Name.Contains("ME-WALL"):
            me_lines.append(ln)
    return me_lines
 
def loop_through_walls(walls):
    for wall in walls:
        coordinates = wall.GetCoordinates()
        send_couple(coordinates)

def send_couple(coordinates):
    xyz_couple = []
    x = 0
    for x in range(len(coordinates)):
        xyz_couple.append(coordinates[x])
        if x < len(coordinates)-2:
            xyz_couple.append(coordinates[x+1])
            create_curve(xyz_couple)
    create_curve(xyz_couple)

#creates curves with lines
def create_curve(couple):
    xyz1 = couple[0]
    xyz2 = couple[1]
    line = Line.CreateBound(xyz1, xyz2)
    t.Start("Curve")
    doc.Create.NewDetailCurve(doc.ActiveView, line)
    t.Commit()

def create_curve_w_lines():
    for line in get_me_lines():
        t.Start("Curve")
        doc.Create.NewDetailCurve(doc.ActiveView, line)
        t.Commit()

loop_through_walls(me_polys)
create_curve_w_lines()

