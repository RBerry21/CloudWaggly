# Waggl.y
Wagg.ly is a small start up company that aim to help dog owners identify dog walkers in their area. They currently do not yet secured mobile development funding, therefore this is a prototype for the website. This will be cloud based, and allow both dog owners, and dog walkers to add their details to the Waggl.y Database, so they can be connected later. 


# HTML Front End
Firstly the HTML Website was created. This was built in Visual Studio.
Firstly a new file was created by going to File -> New File and typing index.html in the file name. This is then saved within a working file for Wagg.ly.
The HTML was then written to add the title, forms and buttons on screen for the user to interact with. The inputs to the form were given unique names so once the user presses submit, these could later be matched to the names within the SQL database, and functions. 
An image was also added of dog pawprints. The HTML Document and the image Pawprints must be saved in the same file at all times for the image to display correctly. 

index.html


# SQL Database
The SQL Database was created using the Azure platform. 
To do this find the "Create Resource" link, followed by SQL Database. 
Create a new SQL database server using SQL Authentication. 
    Set Service and Compute tier to  basic. 
    Make sure 'Add current IP address and "allow Azure serviers and resources to access this server settings in the networking tab are set to yes. 
Once the SQL database is live, click in to it and open the 'Query editor' which can be found on the left hand menu. Sign in and add the following script to create the tables required for the prototype, then press run. The tables and columns will then be available on the menu on the left to the script area. 
  https://github.com/RBerry21/CloudWaggly/blob/main/SQL/sqlquery.sql
Also, whilst in the database navigate to Settings - > Connection strings and copy the conenction string called 'ADO.NET (SQL Authentication' Paste this in to word, and replace the {your_password} with the password used to access the database. Keep this to conenct to the database later. 

# Functions
The functions were created in Visual Studio. 

# Azure Static App 
An Azure static app was used to create the website. This was set up within the Azure portal. 
