                            
 **Para abrir o Pycharm: entre no diretorio pelo terminal e utilize:** 
           
           
           cd bin
           ./pycharm.sh      
   
 1. Instalação das dependencias para o kytos, mininet, mongodb  
 
 2. Comandos para a inicialização do kytos:
 3. 
 4. 
          sudo ./docker/scripts/add-etc-hosts.sh
    
    
          export MONGO_USERNAME=mymongouser
    
    
          export MONGO_PASSWORD=mymongopass
    
    
          docker-compose up -d
    
    
          kytosd -f --database mongodb
    

          export MONGO_DBNAME=napps

    
          export MONGO_HOST_SEEDS=mongo1:27017,mongo2:27018,mongo3:27019

    
    2.1 Comando para entrar como root: Sudo su

    
    2.2 Comando para listar os ambientes virtuais: docker ps
    
          
 6. Inserção de Topologias no Kytos:

 7. 
          Na pasta PycharmProjects/bin utilize       
          sudo python2.7 topologia.py
    

9. Deletar o banco de dados da Topologia:    
         Num novo terminal insira:

   
         sudo docker exec -it mongo1 mongo
   
         use napps
   
         db.dropDatabase();
   

11. Alterar Longitude e latidute de switches:
 
 
12. Criar conexão entre os hosts da topologia:

13. 
    	6.1 Dentro do terminal do mininet execute:   
         	net

         	6.2 Para uma conexão entre h1 e h2 faça:    
         	h1 ping h2
 Porém conexões diretas dedicam uma unica conexão pra cada host, e isso para a aplicação se torna maléfico.

 
 14. Criar conexão via VLAN: 
          7.1 No terminal do mininet insira:

     
          h1 ip addr flush dev h1-eth0.100
       
          h1 ip addr add 192.168.100.1/24 dev h1-eth0.100
     
          h2 ip addr flush dev h2-eth0.100
     
          h2 ip addr add 192.168.100.2/24 dev h2-eth0.100
     
          h1 ping 192.168.100.2

     
          
          7.2 Geralmente as VLANS são configuradas entre 100 e 286.
15. Criar vlan:


16. Para executar tests do diretorio kytos-end-to-end-tests:


         1. Acesse o diretorio
    	kytos-end-to-end-tests

    
         2. verifique qual documento está executando atualmente:
             2.1 cat docker-compose.yml

    
         3. após isso, se for necessario alterar faça:
             3.1 gedit docker-compose.yml
             3.2 altere a linha 16 com o test desejado para execução
             3.3 Salvar arquivo

    
         4. Execute o codigo:
             4.1 docker-compose up -d

   ```python
      produto = Produto.get.all()
      print(produto)
   ```
   

    
         5. Verifique os logs do teste:
             5.1 docker logs kytos-end-to-end-tests_kytos_1

      
    
          
