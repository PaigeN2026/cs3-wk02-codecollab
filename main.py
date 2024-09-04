def main():
  age = 17
  gpa = 3.75
  name = "Luna"
  is_passed = True
  subjects = [
      "AP Calculus", "Rhetoric and Media",
      "Post-AP Computer Science"
  ]

  # Lists
  print(f"{name}'s subjects: {subjects}")
  subjects.append("AP Physics")
  print(f"{name}'s subjects after adding one: {subjects}")

  # List Comprehension
  grades = ['A' for subject in subjects]
  print(f"{name}'s grades: {grades}")

  # Loops & Conditionals
  print(f"{name}'s grades in subjects:")
  for subject, grade in zip(subjects, grades):
    if grade == "A":
      print(f"{subject}: Excellent!")
    else:
      print(f"{subject}: Keep it up!")

  # Functions
  def calculate_year_of_birth(current_year, age):
    return current_year - age

  year_of_birth = calculate_year_of_birth(2023, age)
  print(f"{name}'s year of birth is: {year_of_birth}")

  # User Input
  new_subject = input("Enter a new subject to add to the list: ")
  subjects.append(new_subject)
  grades.append('B')
  print(f"{name}'s updated subjects and grades: {list(zip(subjects, grades))}")


# Explain this below???
if __name__ == "__main__":
  main()
