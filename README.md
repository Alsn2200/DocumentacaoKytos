          Documentacão Kytos
   
 1. Instalação das dependencias para o kytos, mininet, mongodb  
 
 2. Comandos para a inicialização do kytos:     
          sudo ./docker/scripts/add-etc-hosts.sh   
          export MONGO_USERNAME=mymongouser   
          export MONGO_PASSWORD=mymongopass    
          docker-compose up -d    
          kytosd -f --database mongodb    
          
 3. Inserção de Topologias no Kytos:    
          Na pasta PycharmProjects/bin utilize       
          sudo python2.7 topologia.py   
          
 4. Deletar o banco de dados da Topologia:    
         Num novo terminal insira:   
         sudo docker exec -it mongo1 mongo rs0:PRIMARY>   
         use napps     
         db.dropDatabase();   
         
 5. Alterar Longitude e latidute de switches:
 
 
 6. Criar conexão entre os hosts da topologia: 
         6.1 Dentro do terminal do mininet execute:   
         net     
         6.2 Para uma conexão entre h1 e h2 faça:    
         h1 ping h2
 Porém conexões diretas dedicam uma unica conexão pra cada host, e isso para a aplicação se torna maléfico.
 7. Criar conexão via VLAN: 
          7.1 No terminal do mininet insira:   
          
