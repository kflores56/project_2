[![GitHub contributors](https://img.shields.io/github/contributors/kflores56/project_2?logo=Github&style=for-the-badge)](https://github.com/kflores56/project_2/graphs/contributors)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/kflores56/project_2?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/kflores56/project_2?style=for-the-badge)


[![Header](https://raw.githubusercontent.com/nadiaaldrich/project_2/main/readme_images/project2_logo.png "Header")](https://asylumseekersapp.herokuapp.com/)


---


# Background:

The UN Refugee Agency, [**UNHCR**](https://www.unhcr.org/en-us/about-us.html), is a global organization dedicated to saving lives, protecting rights and building a better future for refugees, forcibly displaced communities and stateless people.

This agency gathers data that covers the movement of displaced persons.

---

# Objective: 

## Create an interactive web application to help us visualize the movement of people seeking refuge and to answer the following:


### 1. What are the top countries hosting refugees?
### 2. What are the total number of refugees by year?
### 3. What did the concentration of refugees look like globally in 2016? 


---

# Data Used:

File Name | Contents
------------ | -------------
**timeseries.csv** | host_country, origin, year, # of refugees
**demographics.csv** | host_country, total males, total females 
**coordinates_file.csv** | host_country, lat, long, # of refugees

---

# Development: 

<a href="https:github.com/nadiaaldrich/project_2/main/readme_images"><img width="100" align='left' src="readme_images/files_icon.png?raw=true"></a>
<b/> 
---
- `jupyter notebook` to rename and delete columns
- `PostgresSQL` to create databases 
---
<a href="https:github.com/nadiaaldrich/project_2/main/readme_images"><img width="100" align='left' src="readme_images/visuals.png?raw=true"></a> 
<b/>
---
-  `Python` and `Flask` to create APIs
-  `Javascript, D3.js, Leaflet, Mapbox, CSS, Bootstrap, Googleapis.js` to create visualizations 
---
<a href="https:github.com/nadiaaldrich/project_2/main/readme_images"><img width="100" align='left' src="readme_images/cloud.png?raw=true"></a> 
<b/>
---
-  deployment with `Heroku`
--- 







# Our Product:

### API Data

[**Launch API  Website**](https://asylumseekersapp.herokuapp.com/)

### Main Webpage
<a href="https://github.com/kflores56/project_2/tree/main/readme_images/webpage"><img width="900" src="readme_images/webpage.png?raw=true"></a> 
<b/>

### Map Webpage
<a href="https://github.com/kflores56/project_2/tree/main/readme_images/map"><img width="900" src="readme_images/map.png?raw=true"></a> 
<b/>

---

# Analysis 

- In 2016, the Democratic Republic of Congo took in the largest number if refugees, followed Yemen. 
- The United States is never in the top host countries. 
- Middle Eastern countries show consistent refugee movement.  

---

#### Acknowlegdements: 
The original data was downloaded from [kaggle](https://www.kaggle.com/unitednations/refugee-data).




