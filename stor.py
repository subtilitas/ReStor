class ReStor(object):
    def __init__(self, subclass_path=None, data=None):
        self._subclass_path = subclass_path
        self._data = data
        self._recurse_data(data=data)

    def _recurse_data(self, data):
        if type(data) is dict:
            for key in data.keys():
                if type(key) is int:
                    new_attr = "N%d" % key
                else:
                    new_attr = "%s" % key.replace(" ", "_")
                if self._subclass_path:
                    new_scp = self._subclass_path
                    new_scp += "." + new_attr
                else:
                    new_scp = new_attr

                # print("SCP: ", new_scp)
                # while data is dict create more ReStor classes as members matching the names

                if type(data[key]) is dict:
                    setattr(self, new_attr, ReStor(data=data[key], subclass_path=new_scp))
                else:
                    setattr(self, new_attr, data[key])

        else:
            self._data = None

    def __getitem__(self, item):
        if type(item) is int:
            return getattr(self, "N%d" % item)
        else:
            return getattr(self, item)
