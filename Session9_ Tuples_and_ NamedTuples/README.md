# Session 9 - Tuples & Named Tuples
## Assignment
#### 1. Use the Faker (Links to an external site.)library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age (add proper doc-strings). - 250 (including 5 test cases) <br>
#### 2. Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250 (including 5 test cases) <br>
#### 3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. - 500  (including 10 test cases)<br>
#### 4. Please write a readme file that can help me understand your code. If you don't write a readme properly, I would not be evaluating that piece of the code. <br>
#### 5. Add the notebook as well to your github where logs can be visible. Your github code must have cleared all the 20 tests that you're writing (these 20 cannot be any of the ones you can already find in the code we shared earlier).<br>
#### 6. Once done, share a public link to your repo where we can find the notebook, python files, readme file, and GitHub Actions executed.<br>

#### Prerequisitis
#### Install Faker library using  !pip install Faker
#### Install pytest using !pip isntall pytest
<br><br>

#### Name : Thamizhannal Paramasivam
#### Email: annalwins@gmail.com
<br>

### Faker Library:
Once Faker library is installed, it can used to get fake profiles of a person's and identities.
An example to get fake profile
```python
from faker import Faker
fake = Faker()
profile = fake.profile()
```

### map()
map() function returns a map object(which is an iterator) of the results after
applying the given function to each item of a given iterable (list, tuple etc.)

e.x
```python
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
```
    
### Counter
Counter: Python Counter is a container that returns count of each element in the list. 
Thus, we simply find the most common element by using most_common() method.
```python
Counter(list)
list1 = ['x','y','z','x','x','x','y', 'z']
Counter({'x': 4, 'y': 2, 'z': 2})

```
## NamedTuple: fake profile data processing

#### create_fake_profile_namedtuple()

**create_fake_profile_namedtuple(num: int)**

Create fake profile from faker library and pack it in a named tuple for data processing
@param: number of profiles needs to be generated from faker library.
@return: return all profiles into a named tuple.

**execute:**
 all_profiles = create_fake_profile_namedtuple(10)

**calc_largest_blood_type_namedtuple(all_profiles: namedtuple):**
computes the largest blodd group type from blood group of a person
@params: all_profiles named tuple
@return: largest blood group type as string

**execute**'
all_profiles = create_fake_profile_namedtuple(10)


**calc_largest_blood_type_namedtuple(all_profiles: namedtuple):**
computes the largest blodd group type from blood group of a person
@params: all_profiles named tuple
@return: largest blood group type as string

**execute:**
calc_largest_blood_type_namedtuple(all_profiles) 

**calc_mean_curr_loc_namedtuple(all_profiles: namedtuple):**
computes mean current location from location value of a person
@params: all_profiles named tuple
@return: x,y axis location as Decimal value  

**execute**
calc_mean_curr_loc_namedtuple(all_profiles)


**calculate_age(birth: datetime):**
 Calculate age from birth year, month and day.
 @param: birth date as datetime
 @return age as int


**oldest_person_age_namedtuple(all_profiles: namedtuple):**
Calculats age from birthdate and calulate olderst age of the person 
@params: all_profiles named tuple
@return: oldest age as int value 
**execute:**
oldest_person_age_namedtuple(all_profiles)

** calc_avg_person_age__namedtuple(all_profiles:namedtuple):**
Calculats age from birthdate and compute average age of a person.
@params: all_profiles named tuple
@return: avg age as int value
**execute**
calc_avg_person_age__namedtuple(all_profiles)  

**comp_elasped_time_namedtuple_process():**
computes total time taken to create a faker profile of 10000 users, find the oldest person age,
largest_blood_type, mean_curr_location and avg_person_age in hh:mm:ss.milliseconds.
```python
start_time = datetime.now()
num_of_profiles = 10000
  
profiles_dict = create_fake_profile_namedtuple (num_of_profiles)
oldest_person_age_namedtuple (profiles_dict)
calc_largest_blood_type_namedtuple(profiles_dict)
calc_mean_curr_loc_namedtuple(profiles_dict) 
calc_avg_person_age__namedtuple(profiles_dict)

end_time = datetime.now()
elasped_time = end_time - start_time
print(f'NamedTuples of {num_of_profiles} faker profiles tooks hh:mm:ss.ms {elasped_time} for processing! ')
 
```

### OUTPUT: NamedTuples of 10000 faker profiles tooks hh:mm:ss.ms 0:00:13.575570 for processing! 

## Dictionary: fake_profile data processing
Use the Faker (Links to an external site.)library to get 10000 random profiles.
Using dictionary, calculate the largest blood type, mean-current_location, oldest_person_age, and average age (add proper doc-strings). <br>

**create_fake_profile_dict(num_of_profiles: int):**
Create fake profile from faker library and pack it in a namedtuples for data processing
@param: number of profiles needs to be generated from faker library.
@return: return all profiles into a dict.

**execute:**
profiles_dict = create_fake_profile_dict(5)

**oldest_person_age_dict(profiles_dict: dict):**
Calculats age from birthdate of the profiles and calulate olderst age of the person 
@params: profiles as dictionary
@return: oldest age as int value
**execute:**
oldest_person_age_dict(profiles_dict)

**calc_largest_blood_type_dict(profiles_dict: dict):**
computes the largest blood group type from blood group of a person's profile dictionary
@params: profiles as dictionary
@return: largest blood group type as string
**execute:**
calc_largest_blood_type_dict(profiles_dict)

**calc_mean_curr_loc_dict(profprofiles_dictiles: dict):**
computes mean current location from location value of a person stored in dictionary
@params: profiles as dictionary
@return: x,y axis location as Decimal value
**execute:**
calc_mean_curr_loc_dict(profiles_dict)  

**oldest_person_age_dict(profiles_dict: dict):**
Calculats age from birthdate and calulate olderst age of the person from profiles dictionary
@params: profiles as dictionary
@return: oldest age as int value    
**execute:**
oldest_person_age_dict(profiles_dict)


**avg_person_age_dict(profiles_dict: dict):**
Calculats age from birthdate and compute average age of a person from profiles dictionary
@params: profiles as dictionary 
@return: avg age as int value
**execute:**
avg_person_age_dict(profiles_dict)

**comp_elasped_time_dict_process():**
Computes elasped time to create 10k faker profiles in dict and compute oldest_person_age, 
calc_largest_blood_type,calc_mean_curr_loc and avg_person_age. <br>

```python
  start_time = datetime.now()
  num_of_profiles = 10000
  profiles_dict = create_fake_profile_dict(num_of_profiles)
  oldest_person_age_dict(profiles_dict)
  calc_largest_blood_type_dict(profiles_dict)
  calc_mean_curr_loc_dict(profiles_dict) 
  avg_person_age_dict(profiles_dict)
  end_time = datetime.now()
  elasped_time = end_time - start_time
  print(f'Dictionay of {num_of_profiles} faker profiles tooks hh:mm:ss.ms {elasped_time} for processing! ')
```
### OUTPUT: Dictionary of 10000 faker profiles tooks hh:mm:ss.ms 0:00:15.324825 for processing! 

### Named Tuples Faster than Dictionary
#### NamedTuples of 10000 faker profiles took  0:00:13.575570 hh:mm:ss.ms for processing!
#### Dictionary of 10000 faker profiles took 0:00:15.493149 hh:mm:ss.ms for processing!
#### NamedTuple faster than Dictionary for large scale data processing"



## Stock Exchange
Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple.  <br>


Create a named tuples to hold Global variables for stack exchange

```python
Company = namedtuple('Company', 'name, symbol, open, high, low, close')
all_companies = namedtuple('all_companies', ['Company'])
random_weight = namedtuple('random_weight','weight')

```

**init_stock_exchange(num_of_stocks : int):**
This function creates a named tuples to hold the Company that consist of name, symbol, open, high, low, close
It initialized weight of each stocks randomly. From random weight a normalized weigh is being computed 
that represents % of weight of each stock in exchange.
@param: num_of_stocks present in the exchange as int value
@return: all_stocks that initialize with Company and normalized weight for num_of_stocks

Convert Random weight into normalized weights to assign price to stocks
Normalized weight represents % of weigh a stock holds in exchange value

Assumption: Stocks can't go higher than +20% in a day
Assumption: Stock can't go lower than -20% in a day
Assumption: close is high, then mark high=close
Assumption: Open price can he highest price of the stock in a day 
    
**execute:**
init_stock_exchange(5)

**output:**
(all_companies(Company=Company(name='Weber, Schmidt and Harris', symbol='WEBE', open=2175.0, high=2475.1, low=1939.88, close=2035.83)),
 (6.976744186046512,
  28.77906976744186,
  2.0348837209302326,
  28.197674418604652,
  25.0,
  9.011627906976745))
  
**run_stock_exchange(all_stocks: namedtuple, normalized_weights: namedtuple, num_of_stocks:int):**
@param: all_stocks named tuple is initialized with Company class
@param: normalized_weight is percentage of weight each stock holds in stock exchange
@param: num_of_stocks is int represents number of stocks in exchange
@return list of companies as named tuple thaat consist of stocks name, symbol, open, high, low and close prices      

**execute:**
all_stocks, normalized_weights = init_stock_exchange(100)
run_stock_exchange( all_stocks, normalized_weights, 100)  

#### **OUPUT:** ####

 Company(name='Weaver and Sons', symbol='WEAV', open=85.14, high=99.85, low=78.42, close=69.23),<br> Company(name='Holloway-Becker', symbol='HOLL', open=19.03, high=20.51, low=18.93, close=19.51),<br> Company(name='Harris, Rivera and Moody', symbol='HARR', open=31.93, high=36.22, low=27.51, close=25.81),<br> Company(name='Bishop Ltd', symbol='BISH', open=66.05, high=76.4, low=54.36, close=62.33),<br> Company(name='Compton, Graves and Brewer', symbol='COMP', open=48.94, high=56.79, low=40.16, close=53.55),<br> Company(name='Rodriguez-Perez', symbol='RODR', open=18.2, high=20.18, low=18.09, close=19.23),<br> Company(name='Williams and Sons', symbol='WILL', open=23.06, high=25.52, low=22.95, close=20.51),<br> Company(name='Durham Group', symbol='DURH', open=168.57, high=191.35, low=159.71, close=136.45),<br> Company(name='Williams, Davis and Fields', symbol='WILL', open=12.97, high=15.19, low=10.46, close=12.76),<br> Company(name='Barry, Sanders and Odom', symbol='BARR', open=99.08, high=106.72, low=86.76, close=90.25),<br> Company(name='Miller, Wilson and Murphy', symbol='MILL', open=72.51, high=85.06, low=65.43, close=58.97),<br> Company(name='Scott LLC', symbol='SCOT', open=110.11, high=123.63, low=102.01, close=111.36),<br> Company(name='Davis Group', symbol='DAVI', open=7.02, high=8.28, low=6.85, close=8.28),<br> Company(name='Lee-Mills', symbol='LEE-', open=21.85, high=24.87, low=17.61, close=23.8),<br> Company(name='Duran-Floyd', symbol='DURA', open=58.74, high=61.23, low=49.44, close=50.54),<br> Company(name='Mendoza-Moon', symbol='MEND', open=7.77, high=9.24, low=6.79, close=7.82),<br> Company(name='Lang-Simmons', symbol='LANG', open=64.56, high=69.16, low=53.61, close=54.53),<br> Company(name='Diaz Group', symbol='DIAZ', open=1.44, high=1.72, low=1.31, close=1.51),<br> Company(name='Scott, Mckee and Hobbs', symbol='SCOT', open=76.62, high=78.48, low=74.27, close=68.33),<br> Company(name='Perry Ltd', symbol='PERR', open=111.99, high=120.12, low=100.94, close=110.33),<br> Company(name='Young-Williams', symbol='YOUN', open=8.19, high=9.31, low=8.15, close=7.64),<br> Company(name='Matthews, Boyer and Garrett', symbol='MATT', open=10.43, high=11.67, low=10.26, close=11.67),<br> Company(name='Taylor-Gray', symbol='TAYL', open=56.78, high=59.76, low=53.5, close=59.76),<br> Company(name='Collins LLC', symbol='COLL', open=7.61, high=8.83, low=6.49, close=6.91),<br> Company(name='Ali-Johnson', symbol='ALI-', open=88.12, high=100.77, low=72.56, close=100.77),<br> Company(name='Wagner, Anderson and Carpenter', symbol='WAGN', open=85.03, high=90.8, low=71.08, close=72.41),<br> Company(name='Rubio-Lewis', symbol='RUBI', open=18.34, high=20.65, low=16.96, close=20.36),<br> Company(name='Gutierrez Inc', symbol='GUTI', open=112.17, high=133.51, low=106.52, close=132.01),<br> Company(name='Shaw, Conway and Keller', symbol='SHAW', open=62.54, high=70.49, low=57.05, close=54.82),<br> Company(name='Daniel-Lopez', symbol='DANI', open=93.47, high=111.62, low=90.48, close=111.62),<br> Company(name='Mclaughlin, Boyle and Ramirez', symbol='MCLA', open=3.62, high=4.27, low=3.12, close=3.83),<br> Company(name='Jackson Inc', symbol='JACK', open=12.13, high=12.83, low=11.64, close=11.99),<br> Company(name='Garcia, Evans and Parker', symbol='GARC', open=70.02, high=77.71, low=60.9, close=77.71),<br> Company(name='Flores, Martin and Wright', symbol='FLOR', open=0.92, high=0.97, low=0.76, close=0.9),<br> Company(name='Barker, Hughes and Barrett', symbol='BARK', open=103.02, high=115.32, low=94.06, close=111.91),<br> Company(name='Taylor-Yoder', symbol='TAYL', open=77.42, high=86.87, low=73.74, close=86.87),<br> Company(name='Martinez-Evans', symbol='MART', open=13.07, high=14.49, low=11.26, close=14.49),<br> Company(name='Smith, Faulkner and Wood', symbol='SMIT', open=18.09, high=20.45, low=17.53, close=18.74),<br> Company(name='Adkins, Miller and Turner', symbol='ADKI', open=47.53, high=55.63, low=46.94, close=42.94),<br> Company(name='Hamilton-Ayala', symbol='HAMI', open=9.22, high=10.26, low=9.02, close=10.26),<br> Company(name='Chan, Barber and White', symbol='CHAN', open=32.81, high=37.89, low=29.09, close=28.39),<br> Company(name='Meyers, Thompson and Warren', symbol='MEYE', open=48.24, high=48.53, low=41.94, close=38.8),<br> Company(name='Johnson-Marshall', symbol='JOHN', open=16.14, high=18.27, low=15.85, close=15.12),<br> Company(name='Curry, Olson and Landry', symbol='CURR', open=69.17, high=81.49, low=60.4, close=61.94),<br> Company(name='Martin, Farmer and Johnson', symbol='MART', open=11.12, high=12.9, low=9.29, close=12.9),<br> Company(name='Scott, Lynch and Clay', symbol='SCOT', open=12.24, high=14.49, low=11.63, close=13.39),<br> Company(name='Roberts, Clark and Smith', symbol='ROBE', open=5.76, high=6.86, low=5.71, close=5.55),<br> Company(name='Watson and Sons', symbol='WATS', open=40.69, high=45.89, low=35.82, close=34.66),<br> Company(name='Rhodes-Schmidt', symbol='RHOD', open=16.37, high=16.64, low=14.75, close=15.4),<br> Company(name='Daniels, Scott and Nelson', symbol='DANI', open=3.62, high=4.11, low=3.43, close=3.26),<br> Company(name='Lara-Scott', symbol='LARA', open=22.84, high=25.86, low=20.72, close=23.93),<br> Company(name='Morrison and Sons', symbol='MORR', open=113.5, high=134.96, low=95.65, close=132.2),<br> Company(name='Pierce and Sons', symbol='PIER', open=0.99, high=1.18, low=0.86, close=0.93),<br> Company(name='Gamble, Garrett and Reynolds', symbol='GAMB', open=4.11, high=4.56, low=3.35, close=3.71),<br> Company(name='Campbell Ltd', symbol='CAMP', open=36.72, high=40.37, low=35.22, close=39.91),<br> Company(name='Weaver, Hall and Bailey', symbol='WEAV', open=89.39, high=102.05, low=82.83, close=91.37),<br> Company(name='Wolf Group', symbol='WOLF', open=155.02, high=179.35, low=142.94, close=151.72),<br> Company(name='Daniel, Ward and Hall', symbol='DANI', open=14.83, high=16.2, low=14.5, close=16.2),<br> Company(name='Ruiz, Leon and Wagner', symbol='RUIZ', open=19.24, high=20.47, low=16.55, close=17.53),<br> Company(name='Johnson-Smith', symbol='JOHN', open=75.2, high=79.74, low=70.53, close=70.89),<br> Company(name='Davis, Mahoney and Russell', symbol='DAVI', open=120.89, high=142.68, low=119.76, close=113.19),<br> Company(name='Taylor-Garza', symbol='TAYL', open=46.13, high=47.12, low=41.44, close=37.66),<br> Company(name='Douglas LLC', symbol='DOUG', open=52.78, high=53.75, low=49.8, close=52.92),<br> Company(name='Walker LLC', symbol='WALK', open=68.93, high=72.75, low=57.93, close=60.34),<br> Company(name='Durham PLC', symbol='DURH', open=23.15, high=24.47, low=19.05, close=19.41),<br> Company(name='Gray-Clark', symbol='GRAY', open=145.23, high=165.16, low=135.31, close=130.3),<br> Company(name='Guerra Ltd', symbol='GUER', open=9.38, high=10.45, low=7.54, close=7.68),<br> Company(name='Edwards Group', symbol='EDWA', open=38.6, high=41.27, low=34.12, close=38.86),<br> Company(name='Lopez-Alexander', symbol='LOPE', open=3.05, high=3.65, low=2.98, close=2.83),<br> Company(name='Lambert-Gillespie', symbol='LAMB', open=23.06, high=27.59, low=21.6, close=21.94),<br> Company(name='Horne, Mathis and Marshall', symbol='HORN', open=32.28, high=36.53, low=30.4, close=36.53),<br> Company(name='Jones, Herrera and Hernandez', symbol='JONE', open=14.37, high=15.75, low=12.3, close=15.75),<br> Company(name='Sanders Ltd', symbol='SAND', open=160.07, high=183.01, low=155.57, close=147.07),<br> Company(name='Lee and Sons', symbol='LEE ', open=131.25, high=137.75, low=123.86, close=106.4),<br> Company(name='Garcia, Robinson and Weaver', symbol='GARC', open=70.5, high=83.72, low=67.6, close=80.11),<br> Company(name='Pierce LLC', symbol='PIER', open=25.61, high=25.96, low=25.35, close=21.85),<br> Company(name='Holt, Evans and Reid', symbol='HOLT', open=5.11, high=5.62, low=4.2, close=5.62),<br> Company(name='Rodriguez-Bennett', symbol='RODR', open=25.86, high=28.07, low=25.49, close=24.48),<br> Company(name='Williams LLC', symbol='WILL', open=140.21, high=155.47, low=120.13, close=125.94),<br> Company(name='Saunders, Glover and Anderson', symbol='SAUN', open=79.46, high=79.84, low=70.62, close=65.04),<br> Company(name='Dyer-Baldwin', symbol='DYER', open=10.06, high=10.95, low=8.13, close=10.95),<br> Company(name='White Inc', symbol='WHIT', open=89.39, high=102.48, low=71.91, close=73.12),<br> Company(name='Ramirez Ltd', symbol='RAMI', open=38.06, high=42.79, low=31.21, close=33.28),<br> Company(name='White-Johnson', symbol='WHIT', open=137.07, high=163.6, low=125.92, close=163.6),<br> Company(name='Herring, Wright and Little', symbol='HERR', open=138.7, high=151.35, low=115.73, close=134.63),<br> Company(name='Hale Ltd', symbol='HALE', open=63.3, high=73.64, low=59.16, close=51.1),<br> Company(name='Rice-Carlson', symbol='RICE', open=82.72, high=96.75, low=74.58, close=81.91),<br> Company(name='Cohen, Sanders and Long', symbol='COHE', open=62.58, high=66.31, low=57.36, close=64.96),<br> Company(name='Walker Ltd', symbol='WALK', open=54.49, high=57.84, low=46.69, close=46.88),<br> Company(name='Pruitt-Clark', symbol='PRUI', open=34.05, high=36.19, low=31.99, close=36.19),<br> Company(name='Sweeney Group', symbol='SWEE', open=53.07, high=55.93, low=44.81, close=47.89),<br> Company(name='Jennings, Decker and Smith', symbol='JENN', open=9.15, high=9.97, low=7.35, close=9.97),<br> Company(name='Lynch-Vang', symbol='LYNC', open=17.17, high=20.01, low=15.13, close=17.07),<br> Company(name='Gallagher, Hernandez and Moore', symbol='GALL', open=17.03, high=19.81, low=16.04, close=19.56),<br> Company(name='Jacobs-Spence', symbol='JACO', open=123.38, high=133.81, low=106.7, close=129.26),<br> Company(name='Moody-Mcintyre', symbol='MOOD', open=24.18, high=28.57, low=22.28, close=27.26),<br> Company(name='Wood Ltd', symbol='WOOD', open=71.94, high=75.01, low=58.06, close=75.01),<br> Company(name='Fletcher, Patel and Young', symbol='FLET', open=66.41, high=76.72, low=56.39, close=66.42),<br> Company(name='Thompson, Williams and Patton', symbol='THOM', open=71.51, high=76.93, low=60.87, close=76.93),<br> Company(name='Schwartz-Choi', symbol='SCHW', open=17.52, high=19.24, low=14.59, close=18.27))<br> #####
 
