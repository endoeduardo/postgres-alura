# POSTGRES-ALURA
Repositório de estudos de PostgresSQL com os cursos da Alura.

## Instruções para rodar
- Necessita de ter o docker instalado.
- Executar o seguinte comando

```powershell
docker compose up
```

## Criando um servidor
Colocar o hostname 0.0.0.0 ou localhost não vai funcionar se você estiver rodando tudo no docker-compose.

Para criar um servidor na hora de configurar as conexões é necessário colocar o hostname como o nome do serviço criado no docker-compose.yaml, nesse caso foi `postgres`.

As demais variáveis, colocar as que foram setadas no `docker-compose.yaml` ou trocar no arquivo para variáveis de sua preferência.

![Como configurar o hostname/address](/readme_images/register_server_screenshot.png)