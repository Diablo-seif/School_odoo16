from odoo import models, fields

class Track(models.Model):
    _name = 'track.track'
    _description = 'Track'

    name = fields.Char(string="Name", required=True)
    is_open = fields.Boolean(string="Is open", default=True)
    capacity = fields.Integer(string="Capacity", required=False, default=20)
    Student_id = fields.One2many(comodel_name="students.students", inverse_name="track_id", string="Members", required=False, )

