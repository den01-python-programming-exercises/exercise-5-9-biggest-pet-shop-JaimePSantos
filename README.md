[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3537884&assignment_repo_type=AssignmentRepo)
# Exercise 5.9 Biggest pet shop

Two classes, `Person` and `Pet`, are included in the exercise template. Each person has one pet. Modify the `__str__` method of the `Person` class so that the string it returns tells the pet's name and breed in addition to the person's own name.

```python
lucy = Pet("Lucy", "golden retriever")
leo = Person("Leo", lucy)

print(leo)
```

```plaintext
Leo, has a friend called Lucy (golden retriever)
```
