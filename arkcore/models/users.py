
from arkcore.arkModel import mongoUtils
import jwt
from bson.objectid import ObjectId
from datetime import datetime, timedelta

class RoleMapping(mongoUtils):
    id = None
    role = None
    user = None
    component = None
    component_role = None
    grantedBy = None
    grantedAt = None


class User(mongoUtils):
    FirstName = ""
    LastName = ""
    Email = ""
    Phone = ""
    SecondaryPhone = ""
    Password = ""
    EmailVerified = ""
    PhoneVerified = ""
    SecondaryPhoneVerified = ""
    TwoStepVerificationEnabled = ""
    SystemType = ""
    AuthSystem = ""
    MetaData = ""
    Enabled = ""
    ExternalUser = ""
    JWT = ""
    createdAt = ""
    updatedAt = ""
    lastLoginAt = ""

    def save(self, email):
        if self.getRaw(Email=self.Email) != None:
            raise Exception("Email Already Exists")
        elif self.getRaw(Phone=self.Phone) != None:
            raise Exception("Phone Already Exists")
        else:
            super().save(email)

    def auth(self):
        endTimestamp = datetime.now() + timedelta(days=5)
        startTimestamp = datetime.now()
        jwtCode = {
            "FirstName": self.FirstName,
            "LastName": self.LastName,
            "Email": self.Email,
            "Phone": self.Phone,
            "SecondaryPhone": self.SecondaryPhone,
            "EmailVerified": self.EmailVerified,
            "PhoneVerified": self.PhoneVerified,
            "SecondaryPhoneVerified": self.SecondaryPhoneVerified,
            "TwoStepVerificationEnabled": self.TwoStepVerificationEnabled,
            "AuthSystem": self.AuthSystem,
            "Enabled": self.Enabled,
            "ExpireOn": endTimestamp.timestamp(),
            "CreatedOn": startTimestamp.timestamp()
        }
        jwtCodeDecode = {
            "FirstName": self.FirstName,
            "LastName": self.LastName,
            "Email": self.Email,
            "Phone": self.Phone,
            "SecondaryPhone": self.SecondaryPhone,
            "EmailVerified": self.EmailVerified,
            "PhoneVerified": self.PhoneVerified,
            "SecondaryPhoneVerified": self.SecondaryPhoneVerified,
            "TwoStepVerificationEnabled": self.TwoStepVerificationEnabled,
        }

        encoded_jwt = jwt.encode(jwtCode, "thisiscool", algorithm="HS256")
        self.__setattr__("JWT",encoded_jwt)
        return {"token": encoded_jwt, "tokenDecoded": jwtCodeDecode}