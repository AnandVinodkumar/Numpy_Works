"""
Weather     Temperature     Play  
Sunny           Hot          No  
Sunny           Mild         No
Overcast        Cool         Yes
Rainy           Mild         Yes
Rainy           Cool         Yes  
Sunny           Cool         No


        Prior Probability
_________________________________
Find Prior Probability P(Play=Yes) = 3/5
Find Prior Probability P(Play=No)  = 2/5

        Likelihood
_________________________________
P(Weather=Rainy | Play=Yes) = 2/3
P(Temperature=Hot | Play=Yes) = 0/3
P(Weather=Rainy | Play=No) = 0/2
P(Temperature=Hot | Play=No) = 2/2


weather = rainy, temperature = hot, >>> input_features

P(yes|x) = P(x|yes) * P(yes) / P(x) 
        = 1 * 0 * 2.5 / P(x) 
        = 0

P(no|x) = P(x|no) * P(no) / P(x) 
        = 0 * 0.67 * 3.5 / P(x) 
        = 0
"""
