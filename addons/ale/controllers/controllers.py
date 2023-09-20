# -*- coding: utf-8 -*-
# from odoo import http


# class Ale(http.Controller):
#     @http.route('/ale/ale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ale/ale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ale.listing', {
#             'root': '/ale/ale',
#             'objects': http.request.env['ale.ale'].search([]),
#         })

#     @http.route('/ale/ale/objects/<model("ale.ale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ale.object', {
#             'object': obj
#         })
