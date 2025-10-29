## Colocando a API no ar !!
    > no Terminal:  uvicorn main:app --reload

## Criação de rota no API 

    endpoint -> caminho/link 

    Rest APIs
    get -> leitura/pegar
    POst -> enviar/criar 
    Put/Patch -> edição
    Delete -> Deletar

## criando rota 

    * Passo 1:  usar o "roteador" e informar o caminho e tipo de requisição 
                @order_router.get("/lista")

    * Passo 2: associar a uma função ao decorador

## Migração 

Processo:  Sempre que realizar uma alteração no BD 
    1. `alembic revision --autogenerate -m "oque foi alterado? " `
    2. ` alembic upgrade head` executa a migração 