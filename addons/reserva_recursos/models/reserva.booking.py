from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ReservaBooking(models.Model):
    _name = 'reserva.booking'
    _description = 'Reserva de recurso'

    name = fields.Char(string="Código de reserva")

    recurso_id = fields.Many2one('reserva.recurso', string="Recurso")

    usuario_id = fields.Many2one('res.users', string="Usuario")

    fecha_inicio = fields.Datetime(string="Fecha inicio")

    fecha_fin = fields.Datetime(string="Fecha fin")

    motivo = fields.Text(string="Motivo")

    estado = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmada'),
        ('done', 'Finalizada'),
        ('cancelled', 'Cancelada')
    ], string="Estado")
    
    _sql_constraints = [
        (
            'check_fechas',
            'CHECK(fecha_fin > fecha_inicio)',
            'La fecha de fin debe ser mayor a la fecha de inicio'
        )
    ]
    
    @api.constrains('fecha_inicio', 'fecha_fin', 'recurso_id')
    def check_availability(self):
        for record in self:
            domain = [
                ('recurso_id', '=', record.recurso_id.id),
                ('id', '!=', record.id),  
                ('estado', 'not in', ['cancelled', 'done']),
                ('fecha_inicio', '<=', record.fecha_fin),
                ('fecha_fin', '>=', record.fecha_inicio)
            ]
            solapadas = self.search(domain)
            if solapadas:
                raise ValidationError(
                    ("Solapamiento! %s reservado %s → %s") % (
                        record .recurso_id.name,
                        solapadas[0].fecha_inicio,
                        solapadas[0].fecha_fin
                    )
                )

    # TRANSICIONES ESTADO (Dev3) - Llamar desde botones XML
    def action_confirmar(self):
        self.check_availability()
        self.estado = 'confirmed'

        template = self.env.ref('reserva_recursos.email_template_reserva')
        if self.usuario_id.email:
            template.send_mail(self.id, force_send=True)

        return True

    def action_finalizar(self):
        self.estado = 'done'
        return True

    def action_cancelar(self):
        self.estado = 'cancelled'
        return True

    # Auto código secuencial
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('reserva.booking') or 'New'
        return super().create(vals)