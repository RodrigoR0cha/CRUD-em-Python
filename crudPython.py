import mysql.connector

# Método de conexão do software e o banco de dados Mysql Workbench

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ex_fk',
)

cursor = conexao.cursor()

# Create

comando = 'insert into curso (idcurso, nome, descricao, carga, totaulas, ano) values ("7", "Lorem", "Django", "215", "120", "2020")'
cursor.execute(comando)
conexao.commit()

# Read

comando = 'select * from curso'
cursor.execute(comando)
select = cursor.fetchall()
print(select)


# Update

comando = 'update curso set nome = "Ipsum" where idcurso = 7'
cursor.execute(comando)
conexao.commit()

# delete

comando = 'delete from curso where idcurso = 7'
cursor.execute(comando)
conexao.commit()


conexao.close()
cursor.close()