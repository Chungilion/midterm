# ---------------------------------------------------------------------------
# build_b3_ne_50m_admin_0_countries.py
# Created on: Sat Aug 19 2017 11:46:53 PM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Set the necessary product code
gp.SetProduct("ArcInfo")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Analysis Tools.tbx")


# Local variables...
ne_50m_admin_0_countries_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_countries.shp"
ne_10m_admin_0_countries_shp__2_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_countries.shp"
ne_10m_admin_0_map_subunits_test_shp__3_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_countries.shp"
ne_10m_admin_0_map_subunits_test_shp__4_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_countries.shp"
ne_10m_admin_0_map_subunits_test_shp__5_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_countries.shp"
ne_10m_admin_0_countries_shp__3_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_countries.shp"
ne_10m_admin_0_countries_shp__5_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_countries.shp"
ne_admin_0_details_level_2_countries_dbf = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\housekeeping\\ne_admin_0_details_level_2_countries.dbf"
ne_50m_admin_0_scale_rank_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_scale_rank.shp"
Output_Feature_Class = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_countries.shp"
ne_10m_admin_0_countries_shp__6_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_countries.shp"
ne_50m_lakes_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_physical\\ne_50m_lakes.shp"
ne_50m_lakes_tmp_admin_0_erase_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_physical\\ne_50m_lakes_tmp_admin_0_erase.shp"
ne_50m_admin_0_countries_lakes_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_countries_lakes.shp"

# Process: Dissolve...
gp.Dissolve_management(ne_50m_admin_0_scale_rank_shp, ne_50m_admin_0_countries_shp, "sr_adm0_a3", "scalerank MIN", "MULTI_PART", "DISSOLVE_LINES")

# Process: Add Field (2)...
gp.AddField_management(ne_50m_admin_0_countries_shp, "scalerank", "SHORT", "", "", "", "", "NON_NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field...
gp.CalculateField_management(ne_10m_admin_0_map_subunits_test_shp__4_, "scalerank", "[MIN_scaler]", "VB", "")

# Process: Add Field...
gp.AddField_management(ne_10m_admin_0_map_subunits_test_shp__5_, "featurecla", "TEXT", "", "", "30", "", "NON_NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (2)...
gp.CalculateField_management(ne_10m_admin_0_map_subunits_test_shp__3_, "featurecla", "\"Admin-0 country\"", "VB", "")

# Process: Delete Field...
gp.DeleteField_management(ne_10m_admin_0_countries_shp__3_, "MIN_scaler")

# Process: Repair Geometry...
gp.RepairGeometry_management(ne_10m_admin_0_countries_shp__5_, "DELETE_NULL")

# Process: Join Field...
gp.JoinField_management(Output_Feature_Class, "sr_adm0_a3", ne_admin_0_details_level_2_countries_dbf, "adm0_a3", "")

# Process: Delete Field (2)...
gp.DeleteField_management(ne_10m_admin_0_countries_shp__2_, "sr_adm0_a3;MIN_scaler")

# Process: Select (3)...
gp.Select_analysis(ne_50m_lakes_shp, ne_50m_lakes_tmp_admin_0_erase_shp, "\"admin\" = 'admin-0'")

# Process: Erase...
gp.Erase_analysis(ne_10m_admin_0_countries_shp__6_, ne_50m_lakes_tmp_admin_0_erase_shp, ne_50m_admin_0_countries_lakes_shp, "")

