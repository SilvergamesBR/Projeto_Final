import CRUD as crud
import database
import CLI

db = database.Database("bolt://34.201.33.171:7687","neo4j","validation-drunkeness-shed")
CRUD = crud.CRUD(db)

db.drop_all()

CRUD.create("Marcia",1975,"Comerciante")
CRUD.create("Haroldo",1970,"Fotografo")
CRUD.create("Jasmim",1999,"Medica")
CRUD.create("Ruberio",2001,"Uber")

CRUD.create_relationship("CASADO_COM","Haroldo","Marcia")
CRUD.create_relationship("FILHO_DE","Haroldo","Ruberio")
CRUD.create_relationship("FILHO_DE","Haroldo","Jasmim")
CRUD.create_relationship("FILHO_DE","Marcia","Ruberio")
CRUD.create_relationship("FILHO_DE","Marcia","Jasmim")
CRUD.create_relationship("IRMAO_DE","Jasmim","Ruberio")

pessoa_cli = CLI.PersonCLI(CRUD)
pessoa_cli.run()