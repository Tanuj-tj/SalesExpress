# SalesExpress

### Apps :

* sales
* reports
* profiles
* products
* customers

### Models

* customers 
    * Customer
        * name
        * logo

* Products 
    * product
        * name
        * image
        * price
        * created
        * uploaded


* Profils
    * profile
        * user
        * bio
        * avatar
        * created
        * updated

* Sales
    * Position
        * product
        * quanity 
        * price
        * created

    * Sales
        * transaction_id
        * positions
        * total_price
        * customer
        * salseman
        * created
        * updated

    * CSV
        * file_name
        * activated
        * created
        * uploaded

#### signals.py : Used to set communication between models
* Here the sender will be the user it will inform the profile which will be the receiver that the user instance has been created and the profile will be created for the this user . 


#### utils.py
* Helper function inside sales 