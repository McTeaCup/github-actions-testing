import uuid

class TestObject():
    uuid = int()
    name = str()

    def __init__(self, name: str) -> None:
        self.uuid = uuid.uuid1()
        self.name = name
    
    def get_uuid(self):
        return self.uuid

# just a test
def create_object(name: str):
    new_object = TestObject(name)
    return new_object