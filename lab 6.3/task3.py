def age_classification(age):
    if age > 60 and age <= 100:
        return "senior"
    elif age > 13 and age < 20:
        return "teenager"
    elif age > 20 and age < 60:
        return "adult"
    else:
        return "child"

age = int(input("Enter age: "))
print(age_classification(age))