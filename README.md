This project is an implementation of a heart disease diagnosis system using fuzzy expert system
# Inputs of the problem

### Chest pain
- This entry specifies the degree of chest pain. This input is a crisp input and
It has only four values of 1, 2, 3 or 4, and if its value is 1 it indicates "typical angina", if its 
value is 2, it indicates "atypical angina". if the value is 3, it indicates "non-anginal pain" and if the value is 4
It means "asymptomatic".
### Blood pressure
- This input value specifies the blood pressure of the person.
### Cholesterol
- This input value specifies the level of cholesterol of the person.
### Blood sugar
- This input value specifies the blood sugar level of the person.
### ECG
- It is a non-invasive test that can detect abnormalities such as arrhythmia, evidences of coronary artery disease,
left ventricular hypertrophy and bundle branch blocks.
### Maximum heart rate
- This input shows the maximum heart rate of a person during 24 ours.
### Sports activity 
- This input is a crisp input and has only two values: zero or one. If it is zero, that means
Sports activity is not suitable for a person, and if it is one, it means that sports activity is allowed for the person.
### Peak Old
- This input value specifies the level of depression of the person.
### The amount of thallium
- This input specifies the amount of thallium (a chemical element) in a person's body. This input is  also
a crisp value and it can be only three values: 3, 6, and 7. If the amount of thallium is three, it is "normal", if it six
then the amount of thalliym is "Average" and if it is 7, thallium is "high".
### Gender
- This input is also a crisp input and has only two values: zero and one. If it is zero, it means the patient is 
a man, and if it is one, it means that the patient is a woman.
### Age
- This entry specifies the age of the person

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Finally, the output determines whether or not a person is suffering from heart disease, which is explained in more detail below.

# Implementation steps
## First step: Fuzzification
- To solve the problem with the help of fuzzy logic, it is necessary to convert our values from crisp to fuzzy values(imprecise, relative).
This is called Fuzzification. For this purpose, fuzzy sets are defined and according to their membership function, for each value I calculated
the degree of belongingness to its fuzzy set.
- For this purpose, the membership functions of the required sets are in project description. for example here is the membership function for "Age" input:
<img width="702" alt="image" src="https://user-images.githubusercontent.com/72692826/178142542-54897950-3a4f-4899-bad1-bd7b3da31537.png">

note that crisp value also should be taken into account in the implementation phase.

## Second step: Inference
- to solve the problem, it is necessary to check the fuzzy output values obtained from the existing rules(see rules.py).
It is called inference. For example, consider the following rules:

If (age is old ) and (blood pressure is very high) then ( result is sick(s4))

It simply says that if a person is old and has very high blood pressure, his heart disease is type 4.
