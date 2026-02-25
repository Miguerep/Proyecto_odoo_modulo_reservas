from odoo import models, fields


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