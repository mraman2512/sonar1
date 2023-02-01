from arkcore.arkModel import mongoUtils

class Environment(mongoUtils):
    Name = ""
    Description = ""
    OrgID = ""
    ProjectID = ""
    id = ""
    
class EnvMember(mongoUtils):
    EnvID = ""
    MemberEmail = ""
    Role = ""