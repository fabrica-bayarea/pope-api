### API do portal de pesquisas
Essa esta sendo desenvolvida com o intuito de listar os serviços na qual determinadas organizações prestam


### Desenvolvimento
## Instalação no linux
```
  virtualenv -p python3 venv
  source venv/bin/activate
  pip install -r requirements.txt
  export FLASK_APP=run.py && export FLASK_DEBUG=1 && flask run
```



### Implantação
Para realizar o deploy da aplicação que age em conjunto
com o frontend é bom que você tenha docker para poder auxiliar nesse processo:

## Faça o build da imagem

```
docker build -t pope-api .
```

## Variaveis de ambiente
Copie o arquivo `env.list` para  `.env` e preencha as variaveis com os valores corretos

```
cp env.list .env
```
## Rodando o container
```
docker run -d -p 5000:5000 --env-file .env pope-api
```

PS: em breve melhoro o README
