# -*- coding: utf-8 -*-
# from odoo import http


# class ReservaRecursos(http.Controller):
#     @http.route('/reserva_recursos/reserva_recursos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reserva_recursos/reserva_recursos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reserva_recursos.listing', {
#             'root': '/reserva_recursos/reserva_recursos',
#             'objects': http.request.env['reserva_recursos.reserva_recursos'].search([]),
#         })

#     @http.route('/reserva_recursos/reserva_recursos/objects/<model("reserva_recursos.reserva_recursos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reserva_recursos.object', {
#             'object': obj
#         })
