from arkcore.arkModel import mongoUtils

class BuildersModel(mongoUtils):
    id = ""
    OrgID = ""
    ProjectID = ""
    Name = ""
    GitUrlHttp= ""
    GitUserCred= ""
    GitBranch= ""
    ContainerRegistryHost= ""
    ContainerRegistryCred= ""
    ContainerRegistryUserEmail = ""
    ContainerTag= ""
    Cluster= ""
    Namespace= ""
    CreatedBy = ""

    def __str__(self):
        return self.Name

class Builds(mongoUtils):
    id = ""
    BuilderID = ""
    logs = ""
    Status = ""
    CreatedBy = ""
    CreatedAt = ""
