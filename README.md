!!!!INICIAR CONTENEDOR CON ODOO 16 POSTGRES 15!!!!!
docker-compose up -d

!!!!COMANDO PARA INICIALIZAR DB!!!!
docker-compose run --rm odoo odoo -d TS-MMV -i base --stop-after-init


Entrar en http://localhost:8069/web/database/manager Establecer MASTER PASSWORD 

!!!!COMANDO PARA REESTABLECER LA CONTRASEÑA!!!!
"env['res.users'].search([('login', '=', 'admin')]).write({'password': 'admin'}); env.cr.commit()" | docker-compose exec -T odoo odoo shell -d TS-MMV --db_host=db --db_user=odoo --db_password=odoo