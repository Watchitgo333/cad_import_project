# cad_import_project
This project is test project with attempts to create revit elements and geometry from cad import lines.

The current py scripts lines_to_referenceplanes and lines_to_spaceboundaries both accomplish their file name says respectably.
The project and cad import both require some set up.
1. The import needs to be set up in autocad with making the walls all into one layer, these scripts are looking for "ME-WALL" which is a consistent layer representing the walls of the import.
2. Next the dwg needs to be loaded into revit and imported
3. Once imported, it should be completely exploded
4. Then the scripts can run