from arkcore.arkModel import mongoUtils

class Project(mongoUtils):
    Name = ""
    OrgID = ""
    ParentID = ""
    id = ""

class ProjectMemberRelation(mongoUtils):
    ProjectID = ""
    MemberEmail = ""
    Role = ""