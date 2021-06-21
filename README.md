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

* products 
    * product
        * name
        * image
        * price
        * created
        * uploaded


* profils
    * profile
        * user
        * bio
        * avatar
        * created
        * updated

* sales
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

* report
    * Repost
        * name
        * image
        * remark
        * author
        * created
        * uploaded
        

#### signals.py : Used to set communication between models

* profiles
    * post_save_create_profile 
        * Here the sender will be the user it will inform the profile which will be the receiver that the user instance has been created and the profile will be created for the this user . 

* sales
    * calculate_total_price
        * Getting the total price from Position module of position app

#### utils.py
* Helper function inside sales 