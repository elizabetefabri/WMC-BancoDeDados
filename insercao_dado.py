import sqlite3

conexao = sqlite3.connect(r'banco_mercado.db')
cursor = conexao.cursor()

# Ativando as chaves estrangeiras (foreign keys)
cursor.execute('PRAGMA foreign_keys = ON;')


# Insert tabela da classe "cliente"

# cursor.execute("INSERT INTO Clientes(id_cliente, nome, telefone, endereco) VALUES (1, 'João Sousa', '123456', 'São Paulo')")
# cursor.execute("INSERT INTO Clientes(id_cliente, nome, telefone, endereco) VALUES (2, 'Gabriel Sousa', '258741', 'Brasilia')")
# cursor.execute("INSERT INTO Clientes(id_cliente, nome, telefone, endereco) VALUES (3, 'Heitor Fabri', '369852', 'Paris')")
# cursor.execute("INSERT INTO Clientes(id_cliente, nome, telefone, endereco) VALUES (4, 'Barbara Lima', '021547', 'Bahia')")

# Insert tabela da classe "produto"
# cursor.execute("INSERT INTO Produtos(id_produto, nome_produto, preco, categoria, quantidade_estoque) VALUES (1, 'Notebook Dell', 5000.00, 'Eletronico', 22)")
# cursor.execute("INSERT INTO Produtos(id_produto, nome_produto, preco, categoria, quantidade_estoque) VALUES (2, 'Celular Motorola', 2700.00, 'Eletronico', 5)")
# cursor.execute("INSERT INTO Produtos(id_produto, nome_produto, preco, categoria, quantidade_estoque) VALUES (3, 'Televisão Samsung', 2000.00, 'Eletronico', 8)")
# cursor.execute("INSERT INTO Produtos(id_produto, nome_produto, preco, categoria, quantidade_estoque) VALUES (4, 'Nintendo Switch', 1800.00, 'Eletronico', 40)")

# Insert tabela da classe "transacao"
cursor.execute("INSERT INTO Transacoes(id_transacao, quantidade_estoque, data_hora, cliente_id, produto_id) VALUES  (1, 3, '2024-08-24 12:3200:00', 1, 1) ")
cursor.execute("INSERT INTO Transacoes(id_transacao, quantidade_estoque, data_hora, cliente_id, produto_id) VALUES  (2, 2, '2024-08-24 12:3200:00', 1, 2)")
cursor.execute("INSERT INTO Transacoes(id_transacao, quantidade_estoque, data_hora, cliente_id, produto_id) VALUES  (3, 3, '2024-08-24 12:3200:00', 3, 3) ")





conexao.commit()
conexao.close()