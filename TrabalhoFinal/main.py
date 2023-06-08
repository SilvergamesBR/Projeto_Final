import CRUD as crud
import database
import CLI

db = database.Database("bolt://34.201.33.171:7687","neo4j","validation-drunkeness-shed")
CRUD = crud.CRUD(db)

db.drop_all()

CRUD.create("Ruberio",2001,"Uber")
CRUD.create("Marcia",2000,"Influencer")
CRUD.create("Haroldo",1980,"Modelo de Onlyfans")
CRUD.create("Jasmim",1999,"Dona da Blaze")

print(CRUD.read("Haroldo"))

CRUD.create_relationship("SE_RELACIONA","Haroldo","Ruberio")

CRUD.delete("Marcia")

pessoa_cli = CLI.PersonCLI(CRUD)
pessoa_cli.run()