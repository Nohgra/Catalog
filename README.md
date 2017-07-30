# Item Catalog

by Philip Harms


### About

This project contains a Web App that displays a dynamic catalog, including items from different sports. Users can add new categories and items or edit and delete them. The application is based on the Flask framework which accesses a database. User can LogIn via OAuth2 authentication for editing or deleting items and categories.

### Requirements

- Python (https://www.python.org/)
- VirtualBox (https://www.virtualbox.org/)
- Vagrant (https://www.vagrantup.com/)

### How to Run

Launch Vagrant by running "vagrant up". Log in by running "vagrant ssh".
To initialize the database, run "database_setup.py" within the "Project4"-Folder. To populate the database with a few items from my favourite soccer team, the HSV, run "database_init.py".
Afterwards, execute "python app.py" from the command line to start the web app. The application can now be visited locally on http://localhost:5000
The JSON Endpoints of the web app can be accessed as follows:

Catalog: `/catalog/JSON`
    
Categories: `/catalog/categories/JSON`
    
Category Items: `/catalog/<path:category_name>/items/JSON`
    
Category Item: `/catalog/<path:category_name>/<path:item_name>/JSON`
    