from arkcore.arkModel import mongoUtils

class Cluster(mongoUtils):
    id = ""
    OrgID = "" 
    Name = "" 
    authh = ""
    ClusterType = ""
    CreatedBy = ""


class K8sMasterCluster(mongoUtils):
    id = ""
    orgId = ""
    name = ""
    osType = ""
    serverIp = ""
    userName = ""
    password = ""
    masterToken = ""


class K8sChildCluster(mongoUtils):
    id = ""
    orgId = ""
    masterK8Id = ""
    name = ""
    osType = ""
    serverIp = ""
    userName = ""
    password = ""
