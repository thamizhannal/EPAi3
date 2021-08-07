# **Session 13 - Generators and Iteration tools I**

## Goal 1

Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc.

**DataSet:** The NYC Department of Finance collects data on every parking ticket issued in NYC

**Column Names:**

['SummonsNumber', 'PlateID', 'RegistrationState', 'PlateType', 'IssueDate', 'ViolationCode', 'VehicleBodyType', 'VehicleMake', 'ViolationDescription']

Initalize simple lazy iterator using yield method

```python

def read_csv_file(file_name):
    with open(file_name) as f:
        next(f)
        yield from f
```

parse row is the method that parses every row and associated column name with value

```python
def parse_row(row):
    
    fields = row.strip('\n').split(',')
    parsed_data = (func(field) 
                   for func, field in zip(column_parsers, fields))
    return parsed_data
```

Lazy generator: This generates parsed row in lazy method using yield keyword.

```python
# create generator
def parse_rows_gen():
    for row in read_csv_file(file_name):
        yield zip(column_header,parse_row(row))
```



```python
OUTPUT:
    [('SummonsNumber', 4006478550), ('PlateID', 'VAD7274'), ('RegistrationState', 'VA'), ('PlateType', 'PAS'), ('IssueDate', datetime.date(2016, 10, 5)), ('ViolationCode', 5), ('VehicleBodyType', '4D'), ('VehicleMake', 'BMW'), ('ViolationDescription', 'BUS LANE VIOLATION')]
[('SummonsNumber', 4006462396), ('PlateID', '22834JK'), ('RegistrationState', 'NY'), ('PlateType', 'COM'), ('IssueDate', datetime.date(2016, 9, 30)), ('ViolationCode', 5), ('VehicleBodyType', 'VAN'), ('VehicleMake', 'CHEVR'), ('ViolationDescription', 'BUS LANE VIOLATION')]
[('SummonsNumber', 4007117810), ('PlateID', '21791MG'), ('RegistrationState', 'NY'), ('PlateType', 'COM'), ('IssueDate', datetime.date(2017, 4, 10)), ('ViolationCode', 5), ('VehicleBodyType', 'VAN'), ('VehicleMake', 'DODGE'), ('ViolationDescription', 'BUS LANE VIOLATION')]
```



## Goal 2

Calculate the number of violations by car make.

Note: Try to use lazy evaluation as much as possible - it may not always be possible though! That's OK, as long as it's kept to a minimum.

Parse each row and extract violation values and count and print it.

```python
violations_counts= {}
for rows in parsed_rows:
    data = list(next(parsed_rows))[7]
    if data[1] in violations_counts:        
        violations_counts[data[1]] += 1
    else:
        violations_counts[data[1]] = 1
```

```python
OUTPUT: 
 {'ACURA': 7,
 'AM/T': 1,
 'AUDI': 7,
 'BMW': 15,
 'BUICK': 3,
 'CADIL': 4,
 'CHEVR': 40,
 'CHRYS': 7,
 'DODGE': 21,
 'FIR': 1,
 'FORD': 51,
 'FRUEH': 21,
 'GMC': 18,
 'HIN': 5,
 'HINO': 1,
 'HONDA': 51,
 'HYUND': 18,
 'INFIN': 6,
 'INTER': 11,
 'ISUZU': 4,
 'JAGUA': 3,
 'JEEP': 11,
 'KENWO': 3,
 'KIA': 3,
 'LEXUS': 13,
 'LINCO': 6,
 'MAZDA': 2,
 'ME/BE': 18,
 'MERCU': 3,
 'MI/F': 1,
 'MINI': 1,
 'MITSU': 4,
 'NISSA': 34,
 'NS/OT': 9,
 None: 1,
 'OLDSM': 1,
 'PETER': 1,
 'PLYMO': 1,
 'PORSC': 1,
 'ROVER': 2,
 'SAAB': 1,
 'SATUR': 2,
 'SCION': 1,
 'SMART': 2,
 'SPRI': 1,
 'STAR': 1,
 'SUBAR': 10,
 'TOYOT': 53,
 'UD': 1,
 'UPS': 1,
 'VOLKS': 4,
 'VOLVO': 6,
 'WORKH': 1,
 'YAMAH': 1}
```

