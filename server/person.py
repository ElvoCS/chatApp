class Person:
    """
    represent a person, holds name, socket client & IP address
    """
    def __init__(self, addr, client):
        self.addr = addr
        self.client = client
        self.name = None
        
    def set_name(self, name):
        """
        sets the persons name
        :param name: str
        return:
        """
        self.name = name
        
        
    def __repr__(self):
        return f"Person({self.addr}, {self.name})"
    