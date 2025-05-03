from docutils.nodes import title

from odoo import models, fields,api

class Students(models.Model):
    _name = 'students.students'
    _description = 'students.students'
    _rec_name= "name"

    name = fields.Char(string="Name",required=True,)
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
    capacity_track = fields.Integer(string="Capacity", related="track_id.capacity", )
    skills_ids = fields.Many2many(comodel_name="skills.skills", string="Skills", )
    # grade_ids = fields.One2many(comodel_name="student.course.line", inverse_name="student_id", string="Skills", )
    @api.onchange("gender")
    def _on_change_gender(self):
        if self.gender =='m':
            self.salary=10000
        else:
            self.salary=5000
        return {
            'warning': {
                'title' : 'You changed of gender',
                'message' :'will be change salary automation\n'
                           'salary of Male = 10000\n'
                           'salary of Female = 5000' ,
            }
        }


# class Course(models.Model):
#     _name = 'course.course'
#
#     name = fields.Char(string="Name")
#
# class StudentCourseGrades(models.Model):
#     _name = "student.course.line"
#     student_id = fields.Many2one(comodel_name="students.students", string="Student")
#     course_id = fields.Many2one(comodel_name="course.course", string="Course")
#     grade = fields.Selection(string="Grade", selection=[('g', 'Good'), ('vg', 'Very Good')])
