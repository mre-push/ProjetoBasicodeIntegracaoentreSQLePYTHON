#!/usr/bin/env python
# coding: utf-8

# Projeto básico feito em plataforma JUPYTER, apenas para fins didáticos e profissionais de integração entre PYTHON e SQL

# In[4]:


pip install pyodbc


# In[5]:


import pyodbc


# In[8]:


import pyodbc
print(pyodbc.drivers())


# In[14]:


dados_conexao = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-2ML60F0\\SQLEXPRESS;"
    "Database=PythonSQL;"
    "Trusted_Connection=yes;"
)


# In[15]:


conexao = pyodbc.connect(dados_conexao)

print("Conexão Bem Sucedida")


# In[16]:


cursor = conexao.cursor()

id = 3
cliente = "Lira Python"
produto = "Carro"
data = "25/08/2021"
preco = 5000
quantidade = 1

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
	({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()


# In[ ]:




