from CRUD import CRUD

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class PersonCLI(SimpleCLI):
    def __init__(self, pessoa_model):
        super().__init__()
        self.pessoa_model = pessoa_model
        self.add_command("create", self.create_pessoa)
        self.add_command("create relationship", self.create_relationship)
        self.add_command("relationship query", self.relationship_query)
        self.add_command("read", self.read_pessoa)
        self.add_command("update", self.update_pessoa)
        self.add_command("delete", self.delete_pessoa)
        self.add_command("show occupation",self.show_occupation)

    def create_pessoa(self):
        name = input("Enter the name: ")
        ano_nasc = int(input("Enter the year: "))
        profissao = input("Enter the Occupation: ")
        self.pessoa_model.create(name, ano_nasc, profissao)

    def create_relationship(self):
        tipo = input("Enter the relationship: ")
        name1 = input("Enter the fist name: ")
        name2 = input("Enter the second name: ")
        self.pessoa_model.create_relationship(tipo, name1, name2)

    def relationship_query(self):
        relationship = input("Enter the relationship: ")
        name1 = input("Enter the fist name: ")
        name2 = input("Enter the second name: ")
        print(self.pessoa_model.relationship_query(name1, name2, relationship))

    def read_pessoa(self):
        name = input("Enter the name: ")
        pessoa = self.pessoa_model.read(name)
        print(pessoa)

    def show_occupation(self):
        self.pessoa_model.show_occupation()

    def update_pessoa(self):
        name = input("Enter the name: ")
        newOcc = input("Enter the new Occupation: ")
        self.pessoa_model.update(name, newOcc)

    def delete_pessoa(self):
        name = input("Enter the name: ")
        self.pessoa_model.delete(name)

    def run(self):
        print("Welcome to the person CLI!")
        print("Available commands: create, create relationship, read, update, delete, quit, relationship query, show occupation")
        super().run()