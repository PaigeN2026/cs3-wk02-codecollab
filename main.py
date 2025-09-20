def main():
  age = 17
  gpa = 3.75
  name = "Luna"
  is_passed = True
  subjects = [
      "AP Calculus", "Rhetoric and Media",
      "Post-AP Computer Science"
  ] # LIST []

  # Lists
  print(f"{name}'s subjects: {subjects}")
  subjects.append("AP Physics") #added 
  print(f"{name}'s subjects after adding one: {subjects}")

  # List Comprehension
  grades = ['A' for subject in subjects]
  print(f"{name}'s grades: {grades}")

  # Loops & Conditionals
  def grades_in_subjects():
    print(f"{name}'s grades in subjects:")
    for subject, grade in zip(subjects, grades):
      if grade == "A":
        print(f"   {subject}: Excellent!")
      else:
        print(f"   {subject}: Keep it up!")

  grades_in_subjects()
  print("fkjs")
  # Functions
  def calculate_year_of_birth(current_year, age):
    return current_year - age

  year_of_birth = calculate_year_of_birth(2025, age)
  print(f"{name}'s year of birth is: {year_of_birth}")

  # User Input
  new_subject = input("Enter a new subject to add to the list: ")
  subjects.append(new_subject)
  grades.append('B')
  print(f"{name}'s updated subjects and grades: {list(zip(subjects, grades))}")
  
I commented out line 36, and on line 37 I changed new_subject to input("Enter a new subject: "). When I ran the code there wasn’t an error message, so I can assume I don’t need to save info as a variable to take user input.

  print(" ")
  
  def student_profile():
    print("-- Student Profile --")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"GPA: {gpa}")
    print(f"Subjects: {subjects}")
    print(f"Grades: {grades}")
    grades_in_subjects()

  student_profile()
# Explain this below???
if __name__ == "__main__":
  main()
