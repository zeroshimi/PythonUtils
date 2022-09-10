import json
import np

def JsonSave(fileName: str, data: any):
    with open(fileName ,mode='w') as f:
            json.dump({"result": data}, f, cls = MyEncoder)


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)