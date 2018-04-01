# Password Strength Calculator

The script evaluates the entered password from 1 to 10:
+ 1 - very weak password, 
+ 10 - very steep.

The password must be 6 to 32 characters long,
and not be included in the list of forbidden passwords specified 
in the file 'blacklist'.  
Download by blacklist by link [https://github.com/B1kt0p/blacklist](https://github.com/B1kt0p/blacklist).     

Black list format:
 ```
11111111
1234567
12345678
7777777
 ```
The script uses one argument:
```bash
-b [--blacklist] - path to blacklist.
```
# Get started:
An example of running a script in Linux, Python 3.5 on other operating systems
 is also:
```bash
$ python3 password_strength.py -b blacklist
Enter the password (from 6 to 32 characters): ***********
Password rating 10 points from 10 points.
```
# Project Goals

The code is written for educational purposes. Training course for web-developers
 - [DEVMAN.org](https://devman.org)
