# Waggl.y
Wagg.ly is a small start up company that aim to help dog owners identify dog walkers in their area. They currently have not yet secured mobile development funding, therefore this is a prototype for the website. This will be cloud based, and allow both dog owners, and dog walkers to add their details to the Waggl.y Database, so they can be connected later. \
This repository holds all the documents required for the prototype, and below are instructions on how it was created. 


# HTML Front End
Firstly the HTML Website was created. This was built in Visual Studio.
A new file was created by going to *File -> New File* and typing index.html in the file name. This is then saved within a working file for Wagg.ly.\
The HTML was then written to add the title, forms and buttons on screen for the user to interact with. The inputs to the form were given unique names so once the user presses submit, these could later be matched to the names within the SQL database, and functions.
An image was also added of dog pawprints. The HTML Document and the image Pawprints must be saved in the same file at all times for the image to display correctly. 

https://github.com/RBerry21/CloudWaggly/blob/main/index.html    \
https://github.com/RBerry21/CloudWaggly/blob/main/Pawprints1.png   


# SQL Database
The SQL Database was created using the Azure platform. To do this find the *"Create Resource"* link, followed by *SQL Database*. Then create a new SQL database server using SQL Authentication. 
  -  Set Service and Compute tier to  basic.
  -  Make sure 'Add current IP address and "allow Azure serviers and resources to access this server settings in the networking tab are set to yes.
  - Once the SQL database is live, click in to it and open the 'Query editor' which can be found on the left hand menu. Sign in and add the following script to create the tables required for the prototype, then press run. The tables and columns will then be available on the menu on the left to the script area. \
https://github.com/RBerry21/CloudWaggly/blob/main/SQL/sqlquery.sql 
- Finally, whilst in the database navigate to Settings - > Connection strings and copy the conenction string called 'ADO.NET (SQL Authentication' Paste this in to word, and replace the {your_password} with the password used to access the database. Keep this to conenct to the database later. 

# Functions
The functions were created in Visual Studio. 
 - The following things are required to do this:
   -  Visual Studio Code
   -  Python
   - Phyhon Extension for VS Code
   - Azure Function Extension for VS Code
- Open Visual Studio Code, and go to the Azure Extension on the left hand menu and sign in to Azure.
- Within the Azure window on visual studio code, go to workspace and then press the Azure Functions icon. Select Create new Project.
  - Save the project in the same folder the index.html was saved.
  - Select Phython as the language
  - Model 2 as the programming model.
  - HTTP Trigger for the Function template
  - Call the function adddogs
  - Select Anonymous for the authorizisation level.
  - Go back to work space and select create function.
  - Follow the previous steps again, but call this function addwalkers. 
- Within the "function_app.py" file, copy in the Function code: https://github.com/RBerry21/CloudWaggly/blob/main/functions/function_app.py
- Within the Resources Section of the Azure window, select "Create a Resource" then "Create function app in azure."
  - Call the Function CloudWaggly
  - Select Python 3.11 as the runtime stack
  - Select UK South as the location. This will then create the app. 
- Once created find the app in the Resources Menu - under Function App. Right click on the function app and select "Deploy to Function App"
- Right click on the function app and select "Application Settings", Then "Add New Setting". Call it SQLConnectionString.
- Copy over the connection string from the database that was saved earlier.
- Finally right click on each function and select "Copy Function Url" paste these in to word as they will be required later. 

# Azure Static App 
An Azure static app was used to create the website. This was set up within the Azure portal. 
 - Create a git hub resposity mirroring this one. The index.html and Pawprints1.png must be paid in the root of the repositry. 
 - Within the index.html file update API links with the function UrRL copied earlier.
 - Within Azure go to Create a resource and static web app.
 - Call the app Waggly
 - Ensure the Deployment Details Source is Github and sign in to the correct account underneath.
 -  Set the Organization to the name of the Github account, select the repositry name, and then select main as the branch.
 -  Set the app location to "/", the API location to "/functions" and leave the output location blank.
 -  Then select create.

Once created find the app in Azure, and open it. The overview page has a link to "View the Site" as well as the URL given to the application. 

The full-stack application should now be functional. 
