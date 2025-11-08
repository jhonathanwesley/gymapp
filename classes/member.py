class Member:

    def __init__(self, name: str, last_name: str, birth_date, address: str, telephone, email: str, plan_type, start_date, active, id: None = None):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.address = address
        self.telephone = telephone
        self.email = email
        self.plan_type = plan_type
        self.start_date = start_date
        self.active = active
        self.id = id

