from arkcore.arkModel import mongoUtils

class Organisation(mongoUtils):
    id = ""
    Name = ""
    ParentID = ""
    LogoURL = ""
    Subscription = ""
    
    # def save(self, *args, **kwargs):
    #     super(Organisation, self).save(*args, **kwargs)
    #     url = 'http://localhost:8000/users/roleMapping/'
    #     myobj = {'id': str(self.id), 'model_name': "Organisation"}
    #     x = requests.post(url, json=myobj, headers=kwargs.get('header', ''))


class OrganisationMemberRelation(mongoUtils):
    OrgID = ""
    MemberEmail = ""
    Role = ""