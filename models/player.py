class Player:
    def __init__(self, **kwargs):
        self.Name = kwargs.get("Name")
        self.Health = 100 if kwargs.get("Health") is None else kwargs.get("Health")
        self.HealthMax = 100 if kwargs.get("HealthMax") is None else kwargs.get("HealthMax")
