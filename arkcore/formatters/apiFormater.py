class ResponseReturn:
    def successfn(data):
        res = {}
        res["type"] = "Success"
        res["data"] = data
        return res

    def failurefn(data):
        res = {}
        res["type"] = "Fail"
        res["data"] = data
        return res