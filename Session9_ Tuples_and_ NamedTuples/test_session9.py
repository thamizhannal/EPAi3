# -*- coding: utf-8 -*-
from session9 import *

from datetime import datetime
import pytest
from io import StringIO
import sys
import time
import inspect
import os
import re

import session9
import random

README_CONTENT_CHECK_FOR = [
    "namedtuple",
    "dict",
    "tuple",
    "random",
    "ge",
    "sum",
    "list",
    "map",
    "lambda",
    "Company"
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            print("README.md Missing words:{}".format(c))
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        print()
        assert len(re.findall('([A-Z])', function[0])) <= 1, "You have used Capital letter(s) in your function names"


def test_create_fake_profile_namedtuple():
    global input1
    random.seed(10)

    input1 = session9.create_fake_profile_namedtuple(9999)
    # Here one additionl entry used initializaiton
    assert 10000 == len(input1),"you should have to create 10000 entries"


def test_create_fake_profile_dict():
    global input2
    random.seed(10)

    input2 = session9.create_fake_profile_dict(10000)
    assert 10000 == len(input2),"you have to create 10000 profiles "

def test_oldest_person_time_check():
    assert session9.oldest_person_age_namedtuple(input1)[0] <= \
           session9.oldest_person_age_dict(input2)[0],\
        "Named tuple faster tha Dict for oldest person check"

def test_average_age_time_check():
    assert session9.calc_avg_person_age_namedtuple(input1)[0] <= \
           session9.avg_person_age_dict(input2)[0], "Named tuple faster tha Dict for avg_age_check"

def test_calc_largest_blood_type_time_check():
    assert session9.calc_largest_blood_type_namedtuple(input1)[0] <= \
           session9.calc_largest_blood_type_dict(input2)[0],\
        "Named tuple faster tha Dict for calc_largest_blood_type_namedtuple"

def test_calc_mean_curr_loc_time_check():
    assert session9.calc_mean_curr_loc_namedtuple(input1)[0] <=\
           session9.calc_mean_curr_loc_dict(input2)[0], \
        "Named tuple faster tha Dict for mean currl loc"

# Stock exchange
def test_init_stock_exchange():
    global input3
    num_of_stocks = 100
    x,y = session9.init_stock_exchange(num_of_stocks)
    input3 = session9.run_stock_exchange(x,y,num_of_stocks)
    assert num_of_stocks == len(input3),"you need to create 100 entries"