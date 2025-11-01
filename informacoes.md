# Colocando a API no ar !!
    > no Terminal:  uvicorn main:app --reload

# Criação de rota no API 

    endpoint -> caminho/link 

    Rest APIs
    get -> leitura/pegar
    POst -> enviar/criar 
    Put/Patch -> edição
    Delete -> Deletar

# criando rota 

    * Passo 1:  usar o "roteador" e informar o caminho e tipo de requisição 
                @order_router.get("/lista")

    * Passo 2: associar a uma função ao decorador

# Migração 

Processo:  Sempre que realizar uma alteração no BD 
    1. `alembic revision --autogenerate -m "oque foi alterado? " `
    2. ` alembic upgrade head` executa a migração 


# Aula 04 - Criar conta de usuário, Schemas e criptografia 

#### Criptografia: Utilizando o bycript 

    Formas de informações exceções ao usuário:
        biblioteca: HTTPException (utilizar o raise e não o return)
    ```python
            raise HTTPException(status_code=400, detail="E-mailç do usuário já cadastrado")
    ```

#### schemas: Pydantic
- Criado quando uma função esta recebendo vários paramentros. Então é recomendavel a criação de schemas, fazendo com que a função receba todos os paramentros somente em um objeto. 
- Padroniza a forma como as informações são enviadas por meio de objeto.
- Tipagem de dados (não é obrigado no Python mas o Fast API recomenda).
- Força o python a tipar os dados.
- Objetivo: sitema mais velocidade e integridade de todas as trocas de informações/requisições


# Aula 5 - Pedidos e Login