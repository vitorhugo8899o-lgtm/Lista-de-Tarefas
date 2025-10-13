import json
import os 

class ListaDeTarefas:
    """Gerencia uma lista de tarefas, com suporte a persistência em arquivo JSON."""
    
    NOME_ARQUIVO = 'tarefas.json'

    def __init__(self):
        # Dicionário principal para as tarefas
        self.tarefas = {}
        # Próximo ID a ser usado
        self.proximo_id = 1
        
        # Tenta carregar as tarefas ao iniciar
        self._carregar_tarefas()

    def _carregar_tarefas(self):
        """Carrega as tarefas do arquivo JSON, se ele existir."""
        if os.path.exists(self.NOME_ARQUIVO):
            try:
                with open(self.NOME_ARQUIVO, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    self.tarefas = dados.get('tarefas', {})
                    self.proximo_id = dados.get('proximo_id', 1)
                print(f"Tarefas carregadas com sucesso de {self.NOME_ARQUIVO}.")
            except json.JSONDecodeError:
                print(f"Aviso: Arquivo {self.NOME_ARQUIVO} inválido ou vazio. Iniciando lista vazia.")
            except FileNotFoundError:
                pass
        else:
            print("Iniciando nova lista de tarefas (arquivo JSON não encontrado), criando uma nova!")
            with open(self.NOME_ARQUIVO, 'w', encoding='utf-8') as f: #criar o arquivo .json
                print('\n')
                f.close()


    def salvar_tarefa(self):
        """Salva a tarefa e o proximo id da tarefa"""
        dados = {
            'tarefas': self.tarefas,
            'proximo_id': self.proximo_id
        }
        with open(self.NOME_ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
            f.close()


    def adicionar_tarefa(self,tarefa):
        """Adiciona uma nova tarefa com status 'Pendente' e salva."""
        self.tarefas[str(self.proximo_id)] = {
            'tarefa': tarefa,
            'status': 'Pendente'
        }
        print(f'Tarefa {tarefa} adionada com ID: {self.proximo_id}')
        self.proximo_id += 1
        self.salvar_tarefa()

    def listar_tarefas(self):
        if not self.tarefas:
            return 'Nenhuma tarefa adicionada:(, utlize o comando adionar_tarefas para adicionar uma nova tarefa!'
        print("\n--- Lista de Tarefas ---")
        for id_str, tarefa in self.tarefas.items():
            status = tarefa['status']
            cor_status = '\033[92m' if status == 'Concluída' else '\033[93m'
            reset_cor = '\033[0m'
            
            print(f"ID {id_str}: [{cor_status}{status: <10}{reset_cor}] {tarefa['tarefa']}")
        print("------------------------")

    def marcar_concluida(self, id_tarefa_str):
        """marca a tarefa como concluida"""
        if id_tarefa_str in self.tarefas:
            self.tarefas[id_tarefa_str]['status'] = 'Concluída'
            print(f"Tarefa ID {id_tarefa_str} marcada como Concluída.")
            self.salvar_tarefa()
        else:
            print(f"Erro: Tarefa com ID {id_tarefa_str} não encontrada.")

    def remover_tarefa(self, id_tarefa_str):
        """Remove a tarefa da lista de tarefas"""
        if id_tarefa_str in self.tarefas:
            descricao = self.tarefas[id_tarefa_str]['tarefa']
            del self.tarefas[id_tarefa_str]
            print(f"Tarefa ID {id_tarefa_str} ('{descricao}') removida.")
            self.salvar_tarefa()
        else:
            print(f"Erro: Tarefa com ID {id_tarefa_str} não encontrada.")    

