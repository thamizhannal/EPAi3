## **Session7 Assignemt:**
**Objective of this assignment is to experiment and apply Global and Local Scopes, Nonlocal scopes, Closures, and Closure Applications in real time programming.**

### **Question1:   Q1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters.** 



doc_str_validator:  closure that validates given fun has > 50 length of doc string, if yes returns True otherwise False.

 it accepts function as parameter.

add_nums: This is a sample method for that doc string gets validated.

**Execute:** 

Run below commands to execute it

fn = doc_str_validator(add_nums)
fn()

**Results:**

```
add_nums function does have doc string with > 50 charecters.
True
```

### **Question2:  # Q2. Write a closure that gives you the next Fibonacci number** 

fib(): method that generates Fibonacci series

get_next_fib_number():  
    summary: method that generates next number in Fibonacci  series
    once sum of prev_num and curr_num is computed, curr_num & next_num values are swapped with prev_num & curr_num.
    variables:
    prev_num initialized with value 0
    curr_num initialized with vale 1
    next_num stores sum of prev_num and curr_num

fib_closure(n):
  summary: Wrapper method for fib()
  parameter: n is value in int that represent number of term in Fibonacci series.

**Execute:** Run below commands to execute it

fib_closure(10)

**Result:** 55

### **Question3. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts** 

add() : method to add two numbers

mult():method to mult two numbers

div(): method to divide numbers 

functional_counter():  wrapper function that counts number of times function called and  returns inner function as return value

inner():  method increment counter dict every time fun called also update global dict fun_counters. it accepts function as parameter(add/mult/div) and returns function value as return type

**Execute:**

fn = functional_counter()

fn(add,3,3)

fn(add,3,3)

fn(add,3,3)

fn(mult,3,3)

fn(mult,3,3)

fn(div,9,3)

fn(div,4,2)

print(fun_counters)



**Results:**

{'add': 3, 'mult': 2, 'div': 2}



### **Question4. Modify above such that now we can pass in different dictionary variables to update different dictionaries**



functional_counter(custom_dict):  wrapper function that counts number of times function called. it accepts  dict as parameter

returns inner function as return value.

inner(): method increment custom_dict every time fun called also update global dict fun_counters.

**Execute:**

custom_dict = dict()

fn = functional_counter(custom_dict)

fn(add,3,3)

fn(add,3,3)



fn(div,4,2)

print(custom_dict)



**Results:**

{'add': 2, 'div': 1}
