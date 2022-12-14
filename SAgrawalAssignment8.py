class University:

  def __init__(self, university_name, location, undergraduate_students, graduate_students):
    self.university_name = university_name
    self.location = location
    self.undergraduate_students = undergraduate_students
    self.graduate_students = graduate_students

  def print_university_size(self):
    print("University Size: " + str(self.undergraduate_students + self.graduate_students))

  def is_undergraduate_greater(self):
    if (self.undergraduate_students > self.graduate_students):
      print("There are more undergraduate students than graduate students")
    else:
      print("There are more graduate students than undergraduate students")

SPU = University("Saint Peter's University", "Jersey City", 2600, 800)
SPU.print_university_size()
SPU.is_undergraduate_greater()

class College(University):
  
  def is_college_object(self):
    print("College object created")

SPU = College("Saint Peter's University", "Jersey City", 2600, 800)
SPU.print_university_size()
SPU.is_undergraduate_greater()
SPU.is_college_object()
