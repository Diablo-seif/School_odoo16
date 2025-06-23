from odoo import models, fields,api

class Students(models.Model):
    _name = 'students.students'
    _description = 'students.students'
    _rec_name= "name"

    name = fields.Char(string="Name",default="Eng.",)
    code = fields.Integer(string="ID", required=True,default=0000 )
    gender = fields.Selection(string="Gender", selection=[('m', 'Male'), ('f', 'Female'), ])
    age = fields.Integer(string="Age")
    img = fields.Binary(string="Img")
    accepted = fields.Boolean(string="Work inside company")
    salary = fields.Integer(string="Salary")
    add = fields.Text(string= "Address")
    des = fields.Text(string= "Description")
    birth_date = fields.Date(string="Birth")
    track_id = fields.Many2one(comodel_name="track.track", string="Track", required=False, )
    capacity_track = fields.Integer(string="Capacity of track", related="track_id.capacity", )
    skills_ids = fields.Many2many(comodel_name="skills.skills", string="Skills", )
    login_time = fields.Datetime(string="Login Time" )
    #               ( 'invisible') == hidden      /      ('readonly') != must_write      /     ('required') == must_write
    grade_id = fields.One2many(comodel_name="students.course.line", inverse_name="student_id", string="Grade")
    state = fields.Selection(string="State", selection=[('a', 'Applied'),('f', 'First Interview'),
                                                        ('s', 'Second Interview'),('p', 'Passed'),
                                                        ('r', 'Rejected'),], required=False, default="a")


    def change_state(self):
            if self.state == "a":
                self.state = "f"
            elif self.state == "f":
                self.state = "s"
            elif self.state in ["p","r"]:
                self.state = "a"

    def set_state_passed(self):
                self.state = "p"
    def set_state_rejected(self):
                self.state = "r"
    class StudentCourse(models.Model):
        _name = 'students.course'
        _description = 'students.course'

        name = fields.Char(string="Name", required=True, )

    class StudentCourseGrades(models.Model):
        _name = 'students.course.line'
        _description = 'students.course.line'

        student_id = fields.Many2one(comodel_name="students.students")
        course_id = fields.Many2one(comodel_name="students.course")
        grade = fields.Selection(string="Grade", selection=[('g', 'Good'), ('vg', 'Very Good'), ])



    @api.onchange('gender')
    def onchange_gender(self):
        if not self.gender : # if not choice
            self.salary = 10000
            return {}

        elif self.gender == 'm' :
            self.salary = 10000
            return {
                "warning": {
                    'title': 'Gender Changed to Male ',
                    'message': 'salary to be 10000 '
                },
            }
        elif self.gender == 'f' :
            self.salary = 5000
            return {
                "warning": {
                    'title': 'Gender Changed to Female',
                    'message': 'salary to be 5000 '
                },
            }
        else :
            return {}






class Course(models.Model):
    _name = 'course.course'

    name = fields.Char(string="Name")

class StudentCourseGrades(models.Model):
    _name = "student.course.line"
    student_id = fields.Many2one(comodel_name="students.students", string="Student")
    course_id = fields.Many2one(comodel_name="course.course", string="Course")
    grade = fields.Selection(string="Grade", selection=[('g', 'Good'), ('vg', 'Very Good')])
    
