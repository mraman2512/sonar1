from arkcore.arkModel import mongoUtils

class arkapp(mongoUtils):
    id = ""
    OrgID = ""
    Name = ""
    KubernetesID = ""
    Namespace = ""
    ApplicationiType = "" 
    cron_frequency = ""
    CPU_Resource_Request = ""
    CPU_Resource_Limit = ""
    RAM_Resource_Request = ""
    RAM_Resource_Limit = ""
    Container_Count = ""
    Container_Private = ""
    Container_Registry_URL = ""
    Container_Registry_Cred = ""
    Container_Registry_User_Email = ""
    Container_URL = ""
    CreatedBy = ""
    CreatedAt = ""

    # def __str__(self):
    #     return self.Name

class arkvolume(mongoUtils):
    id = ""
    Name = ""
    arkappID = ""
    Capacity = ""
    mountpath = ""
    CreatedBy = ""
    CreatedAt = ""

    # def __str__(self):
    #     return self.Name

class arkSSL(mongoUtils):
    id = ""
    Name = ""
    arkappID = ""
    certificate = ""
    certificateAuthority = ""
    PrivateKey = ""
    CreatedBy = ""
    CreatedAt = ""

    # def __str__(self):
    #     return self.Name

class arkRoute(mongoUtils):
    id = ""
    Name = ""
    arkappID =  ""
    PortNumber = ""
    hostname = ""
    sslEnabled = "" 
    tlssecretID = ""
    CreatedBy = ""
    CreatedAt = ""

    # def __str__(self):
    #     return self.Name

class arkEnvironmentVars(mongoUtils):
    id = ""
    arkappID = ""
    Key = ""
    Value = ""
    CreatedBy = ""
    CreatedAt = ""

    # def __str__(self):
    #     return self.Key

class arkHistory(mongoUtils):
    id = ""
    arkappID = ""
    Snapshot = ""
    CreatedBy = ""
    CreatedAt = ""

    # def __str__(self):
    #     return str(self.CreatedAt)+" | "+str(self.CreatedBy)
