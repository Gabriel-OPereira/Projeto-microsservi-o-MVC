# Base de dados simulada
atividades = [
    {
        'id_atividade': 1,
        'id_disciplina': 1,
        'enunciado': 'Crie um app todo em Flask',
        'respostas': [
            {'id_aluno': 1, 'resposta': 'todo.py', 'nota': 9},
            {'id_aluno': 2, 'resposta': 'todo.zip.rar'},
            {'id_aluno': 4, 'resposta': 'todo.zip', 'nota': 10}
        ]
    },
    {
        'id_atividade': 2,
        'id_disciplina': 1,
        'enunciado': 'Crie um servidor que envia email em Flask',
        'respostas': [
            {'id_aluno': 4, 'resposta': 'email.zip', 'nota': 10}
        ]
    }
]

# Exceção customizada para indicar que a atividade não foi encontrada
class AtividadeNotFound(Exception):
    pass

def listar_atividades():
    """
    Lista todas as atividades.
    """
    return atividades

def obter_atividade(id_atividade):
    """
    Retorna uma atividade pelo ID.
    Lança AtividadeNotFound se não encontrada.
    """
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            return atividade
    raise AtividadeNotFound

def criar_atividade(id_disciplina, enunciado, respostas=None):
    """
    Cria uma nova atividade.
    """
    nova_atividade = {
        'id_atividade': max([a['id_atividade'] for a in atividades]) + 1 if atividades else 1,
        'id_disciplina': id_disciplina,
        'enunciado': enunciado,
        'respostas': respostas or []
    }
    atividades.append(nova_atividade)
    return nova_atividade

def atualizar_atividade(id_atividade, id_disciplina=None, enunciado=None, respostas=None):
    """
    Atualiza os campos de uma atividade existente.
    """
    atividade = obter_atividade(id_atividade)  # Busca a atividade
    atividade['id_disciplina'] = id_disciplina or atividade['id_disciplina']
    atividade['enunciado'] = enunciado or atividade['enunciado']
    atividade['respostas'] = respostas or atividade['respostas']
    return atividade

def excluir_atividade(id_atividade):
    """
    Remove uma atividade existente pelo ID.
    """
    atividade = obter_atividade(id_atividade)  # Busca a atividade
    atividades.remove(atividade)
