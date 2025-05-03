from odoo import models, fields

class Skills(models.Model):
    _name = 'skills.skills'
    _description = 'Skills'

    name = fields.Char(string="Name", required=True)
    students_id = fields.Many2many(comodel_name="students.students", string="Students", )
