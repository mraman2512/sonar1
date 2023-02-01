import traceback

from .arkcore import arkcore
import pymongo
import json


class mongoUtils():
    acore = None

    def __init__(self, arkcore):
        self.acore = arkcore

    def save(self, email):
        try:
            mydatabase = self.acore.db_instance
            table_name = (self.acore.database_table_prefix + type(self).__name__).lower()
            record = {}
            # for item in dir(self):
            #     if str(type(getattr(self, item)))[8:-2] == 'str' and item != '__module__':
            #         record[item] = getattr(self, item)
            all_result = self.__dict__
            for index, (key, value) in enumerate(all_result.items()):
                if index > 0:
                    record[key] = value

            mycol = mydatabase[table_name]
            record["ark_access_grants"] = {str(email.replace('.', '(<dot>)')): int(16)}
            rec = mycol.insert_one(record)
        except Exception as e:
            status_message = "Failed to push record " + str(e)
            raise Exception(status_message)

    def delete(self, **kwargs):
        try:
            mydatabase = self.acore.db_instance
            table_name = (self.acore.database_table_prefix + type(self).__name__).lower()
            mycol = mydatabase[table_name]
            mycol.delete_one(kwargs)
            print("Delete Function !")
        except Exception as e:
            status_message = "Failed to delete the Record" + str(e)
            raise Exception(status_message)

    def filter(self, **kwargs):
        try:
            mydatabase = self.acore.db_instance
            table_name = (self.acore.database_table_prefix + type(self).__name__).lower()
            mycol = mydatabase[table_name]
            projection = {"_id": 0}
            obj = []
            for doc in mycol.find(kwargs, projection):
                dct = {}
                for key in doc.keys():
                    dct[key] = doc[key]
                obj.append(dct)
            return obj
        except Exception as e:
            status_message = "Failed to Fetch records with given condition" + str(e)
            raise Exception(status_message)

    def get(self, **kwargs):
        try:
            mydatabase = self.acore.db_instance
            table_name = (self.acore.database_table_prefix + type(self).__name__).lower()
            mycol = mydatabase[table_name]
            projection = {"_id": 0}
            result = mycol.find_one(kwargs, projection)
            if not result:
                return {}
            # self.__setattr__("_id",x["_id"])
            # for item in dir(self):
            #     if str(type(getattr(self, item)))[8:-2] == 'str' and item != '__module__':
            #         self.__setattr__(item,x[item])
            return result
        except Exception as e:
            status_message = "Failed to find record with given condition", str(e)
            raise Exception(status_message)

    def update(self, **kwargs):
        try:
            mydatabase = self.acore.db_instance
            table_name = (self.acore.database_table_prefix + type(self).__name__).lower()
            mycol = mydatabase[table_name]
            # query = {"id": kwargs.get("id", "")}
            record = {}
            all_result = self.__dict__
            for index, (key, value) in enumerate(all_result.items()):
                if index > 0:
                    record[key] = value

            newvalue = {"$set": record}
            response = mycol.update_one(kwargs, newvalue)
            return response
        except Exception as e:
            status_message = "Failed to Update record with given condition", str(e)
            raise Exception(status_message)

    def getRaw(self, **kwargs):
        mydatabase = self.acore.db_instance
        table_name = (self.acore.database_table_prefix + type(self).__name__).lower()
        mycol = mydatabase[table_name]
        x = mycol.find_one(kwargs)
        return x

    def grantAccess(self, id, email, roleLevel):
        mydatabase = self.acore.db_instance
        table_name = (self.acore.database_table_prefix + type(self).__name__).lower()
        mycol = mydatabase[table_name]
        query = {"id": id}
        newvalue = {"$set": {"ark_access_grants." + str(email.replace('.', '(<dot>)')): int(roleLevel)
                             }}
        mycol.update_one(query, newvalue)
        return self

    def revokeAccess(self, email):
        mydatabase = self.acore.db_instance
        table_name = (self.acore.database_table_prefix + type(self).__name__).lower()
        mycol = mydatabase[table_name]
        query = {"_id": self._id}
        x = mycol.find_one(query)
        resp = {}
        del x["ark_access_grants"][str(email.replace('.', '(<dot>)'))]
        newvalue = {"$set": {"ark_access_grants": x["ark_access_grants"]
                             }}
        mycol.update_one(query, newvalue)
        return self

    def getAccessGrants(self, id):
        mydatabase = self.acore.db_instance
        table_name = (self.acore.database_table_prefix + type(self).__name__).lower()
        mycol = mydatabase[table_name]
        query = {"id": id}
        x = mycol.find_one(query)
        resp = {}
        for item in x["ark_access_grants"].keys():
            temp = item.replace('(<dot>)', '.')
            # print(item)
            resp[temp] = x["ark_access_grants"][item]
        return resp


class authorization:
    def grant(self):
        print("Grant Function !")

    def revoke(self):
        print("Revoke Function !")


class arkModel(mongoUtils, authorization):
    pass
