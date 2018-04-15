# Python script for calculating the spread risk solvency capital charge ("SCR") under Solvency II (along the standard formula)

This script calculates the spread risk SCR percentage and spread risk MV capital charge an insurer needs to maintain for a portfolio of both bonds and loans (other than residential mortgages) and covered bonds (along the standard formula of Solvency II).

A sample bond portfolio file (in CSV) is attached to this repository. A print screen of this portfolio file and its corresponding SCR charges (per this script) are shown below.

Please note - this script requires the following packages / modules in order to function properly:

- [Python 3.5.1](https://www.python.org/downloads/release/python-351/)
- [Numpy](http://www.numpy.org/)
- [Pandas](https://pandas.pydata.org/)

#### Sample bond portfolio

```
     Name  Rating_class  Coupon  MV_EUR  Modified_duration  Covered_bond  \
0  Bond A             0     1.5     433                200             0   
1  Bond B             1     2.1     132                 20             0   
2  Bond C             2     3.1      98                  9             0   
3  Bond D             3     4.1     231                 10             1   
4  Bond E             4     8.1     532                 25             0   
5  Bond F             5     3.1      36                 16             0   
6  Bond G             6     5.4     245                  5             1   
7  Bond H             7    15.0     145                 25             0   

   Non_EEA_sovereign_issue_in_dom_curr  Issue_from_entity_not_meeting_MCR  
0                                    0                                  0   
1                                    0                                  0   
2                                    0                                  0   
3                                    0                                  0   
4                                    0                                  0   
5                                    0                                  0   
6                                    0                                  0   
7                                    0                                  0
```

#### Resulting SCR charges for the sample bond portfolio file

```
   Name  Rating_class  Coupon  MV_EUR  Modified_duration  Covered_bond  \
0  Bond A             0     1.5     433                176             0
1  Bond B             1     2.1     132                 20             0
2  Bond C             2     3.1      98                  9             0
3  Bond D             3     4.1     231                 10             1
4  Bond E             4     8.1     532                 25             0
5  Bond F             5     3.1      36                 16             0
6  Bond G             6     5.4     245                  5             1
7  Bond H             7    15.0     145                 25             0

   Non_EEA_sovereign_issue_in_dom_curr  Issue_from_entity_not_meeting_MCR  \
0                                    0                                  0
1                                    0                                  0
2                                    0                                  0
3                                    0                                  0
4                                    0                                  0
5                                    0                                  0
6                                    0                                  0
7                                    0                                  0

   SCR_percentage  SCR_instrument
0           0.902         390.566
1           0.134          17.688
2           0.098           9.604
3           0.200          46.200
4           0.491         261.212
5           0.615          22.140
6           0.375          91.875
7           0.380          55.100
```
