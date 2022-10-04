from school_schedule.student import Student, compare_students

# testing that adding a class increases class length by 1
def test_adding_one_class_increases_class_length():
    # arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = Student(name, grade, classes)
    # act
    ellis.add_class("Pottery")
    # assert
    assert ellis.classes == ["Painting", "Pottery"]

# test empty list returns empty list
def test_Student_empty_list_return_empty_list():
    name = "Ellis"
    grade = "junior"
    classes = []
    
    ellis = Student(name, grade, classes)

    assert ellis.classes == []

# test that get_num_classes returns length of classes list
def test_get_num_classes_returns_length():
    name = "Ellis"
    grade = "junior"
    classes = ["Painting", "Pottery", "Math"]
    ellis = Student(name, grade, classes)

    results = ellis.get_num_classes()

    assert results == 3
# test add_class adds corrrect class name to the list of classes

def test_add_class_add_correct_class():
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = Student(name, grade, classes)
    # 
    result = ellis.add_class("Art")
    # assert
    assert "Art" in ellis.classes

def test_compare_students_num_classes():
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]
    ellis = Student(name, grade, classes)

    name = "Ella"
    grade = "senior"
    classes = ["Painting", "Math", "Art"]
    ella = Student(name, grade, classes)

    result = compare_students(ellis, ella)

    assert result == ella
