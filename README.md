# Eventos CET_RIO

Este script recupera dados sobre eventos em andamento na API do CET-RIO (Comando de Operações Especiais da Prefeitura do Rio de Janeiro) e os armazena em um arquivo CSV. Ele também atualiza periodicamente os dados a cada 20 minutos.

# Instalação

Para executar este script, você precisa ter o Python 3 instalado em seu sistema. Além disso, você precisará instalar as dependências necessárias usando o seguinte comando:

```pip install requests ```
```pip install pandas ```
```pip install schedule ```

# Uso
Clone este repositório ou baixe o arquivo dados_rio.bat/dados_rio.py

Abra o terminal ou prompt de comando e navegue até o diretório do projeto.
Execute o script usando o seguinte comando:

```python dados_rio.py```

##

O script começará a buscar dados na API do CET-RIO e os armazenará no arquivo eventos_rio.csv. Ele também atualizará periodicamente os dados a cada 20 minutos, até que você interrompa o programa, abaixo um fluxograma seguindo a lógica de execução do código.

<img src="https://github.com/lyipef/etl_cet-rio/assets/120730541/cfe008cb-4455-47b3-89b0-d4559587180c" width = "60%" height="40%">

###
| Nome | Link de acesso | 
|------|-----------------|
| Fluxograma | [Lucidchart](https://lucid.app/lucidchart/91abc393-7e0b-46df-9c00-dc4fa4304f9a/edit?viewport_loc=203%2C-49%2C3721%2C1595%2C0_0&invitationId=inv_7635ce4f-86b6-4486-9389-a2c614181de2) |

# Registro de Eventos

O script registra quaisquer erros encontrados durante a execução no arquivo error.log. Você pode verificar este arquivo para solucionar quaisquer problemas.


# Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato comigo.

<div>
      <a href="https://www.linkedin.com/in/filipe-jos%C3%A9-9652891b1/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
      <a href="mailto:josefilipe602@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>

##
