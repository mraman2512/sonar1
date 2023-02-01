
from arkcore.arkModel import mongoUtils


class UserAndPassword(mongoUtils):
    id = ""
    OrgID = ""
    name = ""
    userName = ""
    treatUserAsSecret = ""
    password = ""
    description = ""

class GithubApp(mongoUtils):
    id = ""
    OrgID = ""
    name = ""
    description = ""
    appId = ""
    key = ""
    owner = ""

class SshUserWithPrivateKey(mongoUtils):
    id = ""
    OrgID = ""
    name = ""
    userName = ""
    description = ""
    treatUserAsSecret = ""
    privateKey = ""
    key = ""
    passphrase = ""

class SecretFile(mongoUtils):
    id = ""
    OrgID =""
    name = ""
    description = ""
    secretFile = ""

class SecretText(mongoUtils):
    id = ""
    OrgID = ""
    name = ""
    description = ""
    secret = ""

 
class Certificate(mongoUtils):
    id = ""
    OrgID = ""
    name = ""
    description = ""
    password = ""
    certificateFile = ""

