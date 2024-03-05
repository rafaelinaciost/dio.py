from pymongo import MongoClient

# Configurar a conexão ao MongoDB Atlas
def get_mongo_connection():
    client = MongoClient('mongodb')
    return client

# Criar banco de dados e coleção
def create_mongo_collection():
    client = get_mongo_connection()
    db = client['banco_nosql']
    return db['clientes']

# Inserir documentos no MongoDB
def insert_documents(collection):
    dados_cliente1 = {'nome': 'João', 'cpf': '12345678901', 'endereco': 'Rua A, 123', 'contas': [{'tipo': 'corrente', 'agencia': '001', 'numero': '123', 'saldo': 1000}]}
    dados_cliente2 = {'nome': 'Maria', 'cpf': '98765432101', 'endereco': 'Rua B, 456', 'contas': [{'tipo': 'poupanca', 'agencia': '002', 'numero': '456', 'saldo': 500}, {'tipo': 'corrente', 'agencia': '002', 'numero': '789', 'saldo': 1500}]}

    collection.insert_many([dados_cliente1, dados_cliente2])

# Recuperar dados do MongoDB
def retrieve_data(collection):
    cliente_maria = collection.find_one({'nome': 'Maria'})
    print(f'Cliente: {cliente_maria["nome"]}, CPF: {cliente_maria["cpf"]}, Endereço: {cliente_maria["endereco"]}')
    for conta in cliente_maria['contas']:
        print(f'Conta - Tipo: {conta["tipo"]}, Agência: {conta["agencia"]}, Número: {conta["numero"]}, Saldo: {conta["saldo"]}')

# Fechar a conexão do MongoDB
def close_mongo_connection(client):
    client.close()

if __name__ == "__main__":
    client = get_mongo_connection()
    collection = create_mongo_collection()
    insert_documents(collection)
    retrieve_data(collection)
    close_mongo_connection(client)  