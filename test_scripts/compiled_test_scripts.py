from Autodesk.Revit.DB import Transaction, BuiltInParameter, BuiltInCategory, FilteredElementCollector, ImportInstance
import Autodesk.Revit.DB as DB
doc = __revit__.ActiveUIDocument.Document

fec = FilteredElementCollector(doc).OfClass(ImportInstance).WhereElementIsNotElementType()
op = doc.Application.Create.NewGeometryOptions()
op.ComputeReferences = True
op.IncludeNonVisibleObjects = True

for ele in fec:
	if ele.Category.Name == "22150_FP.dwg":
		print(ele.Category.Name)
		dwg = ele

#geo = dwg.GetGeometryObjectFromReference(op)
trans = dwg.GetTransform()

geo = dwg.get_Geometry(op)

for g in geo:
	print(g)
	geoInst = g

for geoEle in geoInst.GetInstanceGeometry():
	print(geoEle)
#DB.GeometryInstance.GetInstanceGeometry()



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
	#print(geoEle.GetType().Equals(Line))
	if geoEle.GetType().Equals(Line):
		lines.append(geoEle)
	elif geoEle.GetType().Equals(PolyLine):
		polys.append(geoEle)

for poly in polys:
	#print(poly.GetCoordinates())
	coords = poly.GetCoordinates()
	first = coords[0]
	last = coords[len(coords)-1]
	#Line.CreateBound(first, last)
	
ln = Line.CreateBound(XYZ(0,0,0), XYZ(10,0,0))

t = Transaction(doc)
t.Start("Curve")
doc.Create.NewDetailCurve(doc.ActiveView, ln)
t.Commit()

xyz = polys[len(polys)-4]

print(xyz)

for c in xyz.GetCoordinates():
	ln = Line.CreateBound(c
ln = Line.CreateBound(XYZ(8.174468911, 6.237104126,0), XYZ(-6.533864422, 6.237104126,0))

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
	#print(geoEle.GetType().Equals(Line))
	if geoEle.GetType().Equals(Line):
		lines.append(geoEle)
	elif geoEle.GetType().Equals(PolyLine):
		polys.append(geoEle)

for poly in polys:
	#print(poly.GetCoordinates())
	coords = poly.GetCoordinates()
	first = coords[0]
	last = coords[len(coords)-1]
	#Line.CreateBound(first, last)

#gets graphic names
# for poly in polys:
# 	#print(poly.GraphicsStyleId)
# 	name = DB.Document.GetElement(doc, poly.GraphicsStyleId)
# 	print(ele.GraphicsStyleCategory.Name)

xyz = polys[len(polys)-4]

#print(xyz.GetCoordinates()[0])

xyzs = xyz.GetCoordinates()
#for c in xyz.GetCoordinates():
#	ln = Line.CreateBound(c,)
ln1 = Line.CreateBound(xyzs[0], xyzs[1])
ln2 = Line.CreateBound(xyzs[1], xyzs[2])
ln3 = Line.CreateBound(xyzs[2], xyzs[3])
ln4 = Line.CreateBound(xyzs[3], xyzs[4])
lines = [ln1,ln2,ln3,ln4]
t = Transaction(doc)
for l in lines:
	t.Start("Curve")
	doc.Create.NewDetailCurve(doc.ActiveView, l)
	t.Commit()


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

me_walls = []
for poly in polys:
 	name = DB.Document.GetElement(doc, poly.GraphicsStyleId)
 	if name.GraphicsStyleCategory.Name.Contains("ME-WALL"):
 		me_walls.append(poly)
 
#for wall in me_walls:
	#print(wall.GetCoordinates())
	
print(me_walls[1].GetCoordinates().Count)

xyzs0 = me_walls[0].GetCoordinates()
xyzs1 = me_walls[1].GetCoordinates()
xyzs2 = me_walls[2].GetCoordinates()

ln1 = Line.CreateBound(xyzs0[0], xyzs0[1])
ln2 = Line.CreateBound(xyzs0[1], xyzs0[2])
ln3 = Line.CreateBound(xyzs0[2], xyzs0[3])
ln4 = Line.CreateBound(xyzs0[3], xyzs0[4])
ln5 = Line.CreateBound(xyzs0[4], xyzs0[5])

ln6 = Line.CreateBound(xyzs1[0], xyzs1[1])
ln7 = Line.CreateBound(xyzs1[1], xyzs1[2])
ln8 = Line.CreateBound(xyzs1[2], xyzs1[3])
ln9 = Line.CreateBound(xyzs1[3], xyzs1[4])
ln10 = Line.CreateBound(xyzs1[4], xyzs1[5])
ln11 = Line.CreateBound(xyzs2[0], xyzs2[1])
lines = [ln1,ln2,ln3,ln4,ln5,ln6,ln7,ln8,ln9,ln10,ln11]

t = Transaction(doc)
for l in lines:
	t.Start("Curve")
	doc.Create.NewDetailCurve(doc.ActiveView, l)
	t.Commit()
	

from Autodesk.Revit.DB import Transaction, XYZ, Line, PolyLine, BuiltInParameter, BuiltInCategory, FilteredElementCollector, ImportInstance
import Autodesk.Revit.DB as DB
doc = __revit__.ActiveUIDocument.Document

t = Transaction(doc)
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
	#print(geoEle)
	if geoEle.GetType().Equals(Line):
		lines.append(geoEle)
	elif geoEle.GetType().Equals(PolyLine):
		polys.append(geoEle)

me_walls = []
me_lines = []
for poly in polys:
    name = DB.Document.GetElement(doc, poly.GraphicsStyleId)
    if name.GraphicsStyleCategory.Name.Contains("ME-WALL"):
        me_walls.append(poly)

for ln in lines:
	ln_name = DB.Document.GetElement(doc, ln.GraphicsStyleId)
	#print(ln_name.GraphicsStyleCategory.Name)
	if ln_name.GraphicsStyleCategory.Name.Contains("ME-WALL"):
		me_lines.append(ln)
print(len(me_lines))

for line in me_lines:
	print(line)
	t.Start("Curve")
	DB.Grid.Create(doc, line)
	t.Commit()

from Autodesk.Revit.DB import Transaction, BuiltInParameter, BuiltInCategory, FilteredElementCollector, ImportInstance
import Autodesk.Revit.DB as DB
doc = __revit__.ActiveUIDocument.Document

c = doc.Settings.Categories.get_Item(BuiltInCategory.OST_Lines)

sub = c.SubCategories

for line in sub:
	if line.Name.Contains("ME-WALL"):
		me_wall = line
		print(me_wall)

from Autodesk.Revit.DB import Transaction, BuiltInParameter, BuiltInCategory, FilteredElementCollector, ImportInstance
import Autodesk.Revit.DB as DB
doc = __revit__.ActiveUIDocument.Document
op = doc.Application.Create.NewGeometryOptions()
op.ComputeReferences = True
op.IncludeNonVisibleObjects = True

fec = FilteredElementCollector(doc, doc.ActiveView.Id)
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
print(g, e)

from Autodesk.Revit.DB import Transaction, BuiltInParameter, BuiltInCategory, FilteredElementCollector, ImportInstance
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

for ln in eles:
	print(ln.GeometryCurve)
	t.Start("Curve")
	doc.Create.NewDetailCurve(doc.ActiveView, ln.GeometryCurve)
	t.Commit()