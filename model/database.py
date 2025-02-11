import mysql.connector as mc
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv

class Database:
    def __init__(self):
        load_dotenv()
        self.host = getenv('DB_HOST')
        self.username = getenv('DB_USER')
        self.password = getenv('DB_PSWD')
        self.database = getenv('DB_NAME')
        self.connection = None
        self.cursor = None

    def conectar(self):
        """Estabelece uma conexão com o banco de dados."""
        try:
            self.connection = mc.connect(
                host = self.host, 
                database = self.database, 
                user = self.username,
                password = self.password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary = True)
                print('Conexão do banco de dados realizada com sucesso!')
        except Error as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursor = None

    def desconectar(self):
        """Encerre a conexão com o banco de dados e o cursor, se existirem"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print('Conexão com o banco de dados encerrada com sucesso!')

    def consultar(self, sql, params=None):
        """Executa uma instrução no banco de dados."""
        if self.connection is None and self.cursor is None:
            print("Conexão ao banco de dados não estabelecida!")
            return None 
        
        try:
            self.cursor.execute(sql,params)
           #self.connection.commit()
            return self.cursor.fetchall() 
        except Error as e:
            print(f'Erro de execução: {e}')
            return None
        
db = Database()
db.conectar()
print(db.consultar('select * from tarefa;'))
db.desconectar
        