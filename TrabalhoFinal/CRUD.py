import database


class CRUD:
    def __init__(self, database: database.Database):
        self.db = database

    def create(self, name, ano_nasc, profissao):  # cria uma pessoa no BD
        query = "CREATE (:Pessoa{nome:$nome,ano_nasc:$ano_nasc,profissao:$profissao})"
        parameters = {"nome": name, "ano_nasc": ano_nasc, "profissao": profissao}
        return self.db.execute_query(query, parameters)

    def read(self, name):  # retorna uma pessoa com o nome informado
        query = "Match (p:Pessoa{nome:$nome}) return p limit 1"
        parameters = {"nome": name}
        return self.db.execute_query(query, parameters)

    def delete(self, name):  # deleta pessoa com base no name
        query = "Match (p:Pessoa{nome:$nome}) detach delete p"
        parameters = {"nome": name}
        return self.db.execute_query(query, parameters)

    def create_relationship(self, tipo, nome1,nome2):  # cria um relacionamento do tipo escolhido entre 2 nos do tipo pessoa
        query = "Match (p1:Pessoa{nome:$nome1}),(p2:Pessoa{nome:$nome2}) create (p1)-[:" + tipo + "]->(p2)"
        parameters = {"nome1": nome1, "nome2": nome2, "tipo": tipo}
        return self.db.execute_query(query, parameters)

    def update(self,nome,profissao):#muda a profissao de um no dado o seu nome
        query = "Match (p:Pessoa{nome:$nome}) set p.profissao = \""+ profissao+"\""
        parameters = {"nome":nome}
        return self.db.execute_query(query,parameters)

    def relationship_query(self,nome1,nome2,relationship):
        query = "match (p1:Pessoa{nome:$nome1})<-[i:"+relationship+"]->(p2:Pessoa{nome:$nome2}) return i"
        parameters = {"nome1": nome1, "nome2": nome2}
        if self.db.execute_query(query, parameters):
            return True
        else:
            return False

    def show_occupation(self):
        query = "match (n:Pessoa) return n.profissao"
        print(self.db.execute_query(query))
