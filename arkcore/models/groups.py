from arkcore.arkModel import mongoUtils

class Group(mongoUtils):
    Name = ""
    OrgID = ""
    ParentID = ""
    id = ""

class GroupMemberRelation(mongoUtils):
    GroupID = ""
    MemberEmail = ""
    Role = ""