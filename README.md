# password-analysis
Jupyter notebook which sums up my analysis of passwords using a database (https://github.com/duyetdev/bruteforce-database) of 61682 passwords, made visualizations to assess which types of passwords are harder to brute-force through.

## steps
I first analysed the relationships between entropy, different character types, and how they impact password strength:
(https://github.com/Yatin-Kapur/password-analysis/blob/master/password%20analysis.ipynb)

I then wrote a script to make individual passwords better:
(https://github.com/Yatin-Kapur/password-analysis/blob/master/passtronger.py)

Lastly, I compared the 'old' strength of the 61682 passwords to the 'new' strength, the 'new' strength being the strength determined after running the password improving script on the passwords:
(https://github.com/Yatin-Kapur/password-analysis/blob/master/improved%20passwords%20and%20comparison.ipynb)
