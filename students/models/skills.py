from odoo import models, fields

class Skills(models.Model):
    _name = 'skills.skills'
    _description = 'Skills'

    name = fields.Char(string="Name", required=True)
    students = fields.Many2many(comodel_name="students.students", relation="", column1="", column2="", string="Students", )
