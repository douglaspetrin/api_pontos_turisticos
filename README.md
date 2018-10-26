# api_pontos_turisticos
API Rest desenvolvida com Django Rest Framework para estudos e testes.
<br><br>

 `Python 3.6.6 - Django=>2.1.2 - djangorestframework==3.9.0`  
   
## Workflow  

![API Workflow](http://assets.douglaspetrin.com/API%20Pontos%20Tur%C3%ADsticos%20-%20Workflow.png)  



## Clone o projeto

`$ git clone https://github.com/douglaspetrin/api_pontos_turisticos.git`
  

`cd api_pontos_turisticos`


## Criar e ativar ambiente virtual

`virtualenv venv`   

### Linux/Mac  
`source .venv/bin/activate`
  

  
### Windows  
`cd venv/scripts`  

`activate`  


## Instalar dependências

`pip install -r requirements.txt`

## Migrar e criar super usuario

`python manage.py migrate`   

`python manage.py createsuperuser`  


## Rodar projeto

`python manage.py runserver`  


## Digite no seu navegador

http://localhost:8000/
