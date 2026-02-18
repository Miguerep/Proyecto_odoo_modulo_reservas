
!!!!COMANDO PARA INICIALIZAR DB!!!!

docker-compose run --rm odoo odoo -d TS-MMV -i base --stop-after-init

DESPUES DE EJECUTAR ESTE COMANDO

Entrar en http://localhost:8069/web/database/manager
Establecer MASTER PASSWORD
"env['res.users'].search([('login', '=', 'admin')]).write({'password': 'admin'}); env.cr.commit()" | docker-compose exec -T odoo odoo shell -d TS-MMV --db_host=db --db_user=odoo --db_password=odoo