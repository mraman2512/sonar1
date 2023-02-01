import pymongo

class arkcore:
    database_host = ""
    database_port = ""
    database_name = ""
    database_table_prefix = ""
    email_host = ""
    email_port = ""
    email_user = ""
    email_password = ""
    razorpay_key_id = ""
    razorpay_key_secret = ""
    jwtSecret = ""
    appName = ""

    client = None
    db_instance = None

    def __init__(self, **kwargs):
        print(" +------------------------------------------------------------+")
        print(" |                      DEVOPSARK MODULE                      |")
        print(" +------------------------------------------------------------+")
        try:
            if kwargs["database_host"]:
                self.database_host = kwargs["database_host"]
                print(" | [re-configured]  database_host                             |")
        except:
            pass
        try:
            if kwargs["database_port"]:
                self.database_port = kwargs["database_port"]
                print(" | [re-configured]  database_port                             |")
        except:
            pass
        try:        
            if kwargs["database_name"]:
                self.database_name = kwargs["database_name"]
                print(" | [re-configured]  database_name                             |")
        except:
            pass
        try:        
            if kwargs["database_table_prefix"]:
                self.database_table_prefix = kwargs["database_table_prefix"]
                print(" | [re-configured]  database_table_prefix                     |")
        except:
            pass
        try:        
            if kwargs["email_host"]:
                self.email_host = kwargs["email_host"]
                print(" | [re-configured]  email_host                                |")
        except:
            pass
        try:        
            if kwargs["email_port"]:
                self.email_port = kwargs["email_port"]
                print(" | [re-configured]  email_port                                |")
        except:
            pass
        try:        
            if kwargs["email_user"]:
                self.email_user = kwargs["email_user"]
                print(" | [re-configured]  email_user                                |")
        except:
            pass
        try:        
            if kwargs["email_password"]:
                self.email_password = kwargs["email_password"]
                print(" | [re-configured]  email_password                            |")
        except:
            pass  
        try:        
            if kwargs["razorpay_key_id"]:
                self.razorpay_key_id = kwargs["razorpay_key_id"]
                print(" | [re-configured]  razorpay_key_id                           |")
        except:
            pass  
        try:        
            if kwargs["razorpay_key_secret"]:
                self.razorpay_key_secret = kwargs["razorpay_key_secret"]
                print(" | [re-configured]  razorpay_key_secret                       |")
        except:
            pass  
        try:        
            if kwargs["jwtSecret"]:
                self.jwtSecret = kwargs["jwtSecret"]
                print(" | [re-configured]  jwtSecret                                 |")
        except:
            pass  
        try:        
            if kwargs["appName"]:
                self.email_password = kwargs["appName"]
                print(" | [re-configured]  appName                                   |")
        except:
            pass  
        
        self.client = pymongo.MongoClient("mongodb://"+self.database_host+":"+self.database_port+"/")
        self.db_instance = self.client[self.database_name]

        print(" +------------------------------------------------------------+")
        print(" ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(" +------------------------------------------------------------+")
        print(" |             DevopsArk Initialization Complete              |")
        print(" +------------------------------------------------------------+")
        print(" ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(" +------------------------------------------------------------+")