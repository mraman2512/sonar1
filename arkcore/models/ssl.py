from arkcore.arkModel import mongoUtils

class Ca(mongoUtils):
    id = ""
    name = ""
    OrgID = ""
    certificateLocation = ""
    category = ""

    country = ""
    state = ""
    locality = ""
    organization = ""
    organizationUnit = ""
    commonName = ""
    email = ""

    expiry = ""
    createdBy = ""
    createdAt = ""


class SslCertificate(mongoUtils):
    id = ""
    name = ""
    OrgID = ""
    certificateLocation = ""
    category = ""

    country = ""
    state = ""
    locality = ""
    organization = ""
    organizationUnit = ""
    commonName = ""
    email = ""

    expiry = ""
    createdBy = ""
    createdAt = ""