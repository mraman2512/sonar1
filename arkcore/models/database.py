from arkcore.arkModel import mongoUtils

class MongoDb(mongoUtils):
    id = ""
    orgId = ""
    name = ""
    host = ""
    userName = ""
    password = ""
    port = ""
    createdBy = ""

class MongoAccess(mongoUtils):
    id = ""
    parentDbId = ""
    userName = ""
    password = ""
    dbName = ""

class PostgresDb(mongoUtils):
    id = ""
    orgId = ""
    name = ""
    host = ""
    dbName = ""
    userName = ""
    password = ""
    port = ""
    createdBy = ""


class PostgresAccess(mongoUtils):
    id = ""
    parentDbId = ""
    userName = ""
    password = ""
    dbName = ""


class MysqlDb(mongoUtils):
    id = ""
    orgId = ""
    name = ""
    host = ""
    dbName = ""
    userName = ""
    password = ""
    port = ""
    createdBy = ""


class MysqlAccess(mongoUtils):
    id = ""
    parentDbId = ""
    userName = ""
    password = ""
    dbName = ""