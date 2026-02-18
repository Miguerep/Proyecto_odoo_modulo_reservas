
!!!!COMANDO PARA INICIALIZAR DB!!!!

docker-compose run --rm odoo odoo -d TS-MMV -i base --stop-after-init

DESPUES DE EJECUTAR ESTE COMANDO

Entrar en http://localhost:8069/web/database/manager
Establecer MASTER PASSWORD
