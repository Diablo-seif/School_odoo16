from odoo import models, fields

class Students(models.Model):
    _name = 'students.students'
    _description = 'students.students'
    _rec_name= "name"

    name = fields.Char(string="Name")
    gender = fields.Selection(string="Gender", selection=[('m', 'Male'), ('f', 'Female'), ])
    age = fields.Integer(string="Age")
    img = fields.Binary(string="Img")
    accepted = fields.Boolean(string="Work inside company")
    salary = fields.Integer(string="Salary")
    add = fields.Text(string= "Address")
    des = fields.Text(string= "Description")
    birth_date = fields.Date(string="Birth")
    login_time = fields.Datetime(string="Login Time" )
    track_id = fields.Many2one(comodel_name="track.track", string="Track", required=False, )
    skills_id = fields.Many2many(comodel_name="skills.skills", relation="", column1="", column2="", string="Skills", )
