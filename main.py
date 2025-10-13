from classes import *

# ----------------------------------------------------
# Exemplo de Uso (simulação de interface de terminal)
# ----------------------------------------------------

cliente = ListaDeTarefas()  # criando a classe ListaDeTarefas
cliente._carregar_tarefas() #verificando se existe alguma lista
cliente.adicionar_tarefa('Comprar café') #adiconando a primeira tarefa
cliente.listar_tarefas() # listando todas as tarefas
cliente.salvar_tarefa() #salvando a tarefa
cliente.marcar_concluida(1) #passar o id como str
cliente.remover_tarefa('1') #passar o id como str