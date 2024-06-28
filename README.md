# Store Api
APIRest to sell products. With this api you can register and query products, update stock, and make orders to sell products, also you have a panel Admin to manage your catalog, orders and product stock.
You can check if some product has enough stock when you query products or in a log.

### Start project
* On docker-compose.yaml level run next command: **docker compose up -d**
* In a new terminal run next command: **docker exec -i postgresql bash -c "psql -U sl -d mydb -f docker-entrypoint-initdb.d/dump.sql"**
* Now in a new terminal run: 
  * **docker exec -w /app/store/ -it store /bin/bash**
  * later inside the container **python manage.py createsuperuser** and follow the instructions
  * Now you can access to the Admin panel at http://localhost:8008/admin


### Run directly
* > docker compose up -d
* > docker exec -i postgresql bash -c "psql -U sl -d mydb -f docker-entrypoint-initdb.d/dump.sql"
* > docker exec -w /app/store/ -it store /bin/bash
* > python manage.py createsuperuser

Now you are ready to consume the api with postman and django admin. To run tests in app you can run:

* > pytest


### API Docs
The docs are in postman, you can import the collection with follow link: https://api.postman.com/collections/4702306-6b40f3fd-e85d-4910-a8a8-6ca13a6d4eb2?access_key=PMAT-01J1E0NHCG9V14D0V4VN39CD4B

Docs online: https://docs.google.com/document/d/1MXJ1tFsOsxn43KoswmaSSk1AoG-0qTM83Y18jUTH79w/edit?usp=sharing
For more information, contact me at steve.ludwig.jesus@gmail.com.