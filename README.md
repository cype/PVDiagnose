# PVDiagnose
----------------------------------------------------------------------------------------

[Energy Hackdays 2019](https://hack.opendata.ch/event/24#top) / Challenge D / [PV-Diagnose](https://hack.opendata.ch/project/302)

We created a web app that allows users to check the status of their solar installations by evaluating if the energy production is at a normal state. Our application aims at providing a quick verification of the monthly energy production of roof top solar panels. The user will provide the following input:

1. Location of the solar panel: address
2. Size of PV: area in m2
3. Capacity kWp
4. PV installation specifications:
  * m2 (or kWp)
  * 12 months of production data
  
The app looks up the estimations from sonnendach, compares the the input and returns:  

1. Location on map
2. Status: ok or not ok
3. Monthly comparison of actual vs. reference as a bar chart

See our [wiki](https://github.com/cype/PVDiagnose/wiki) or visit the [opendata.ch](https://opendata.ch/) [energy hackdays](https://hack.opendata.ch/event/24#top) page.

# Prototype

[Input](http://energy-data-hackdays-d.s3-website.eu-central-1.amazonaws.com/)

[Results](http://energy-data-hackdays-d.s3-website.eu-central-1.amazonaws.com/results.html)


# Data sources

Main data: [GeoAdmin](http://api3.geo.admin.ch/) and BFE's [sonnendach](https://www.uvek-gis.admin.ch/BFE/sonnendach/?lang=de)

# Open Questions
