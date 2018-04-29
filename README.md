# Significant Figures Calculator

This inspiration came from when I was in grad school, trying to finish my error analysis assignments. Basically, how can you trust the computer (or programming language) to conserve whatver significant figure you have during a calculation?

 Included in this repository are `sigfigs.py`, which has the code to count the number of significant figures in a number, and `test.py `, which will allow the user to run a test to confirm whether the code works in its method.
 
NOTE: When using this code, the number of interest must be entered as sfCount('0.0670') and not sfCount(0.670), otherwise python will strip the traling zero and result in an incorrect answer. Any thoughts or suggestion on how to avoid this please send me an email at _gleland@protonmail.com_, I would very much welcome any feedback!


## Rules for Determining Significant Figures

Here are the rules regarding sig figs, which can be found at [Wikipedia](https://en.wikipedia.org/wiki/Significant_figures) with more detail, but any Google search will yield the same results.

 - All non-zero digits are significant (843 has 3 sig figs)
 - Zeroes that are in between two non-zero digits are significant (404 and 808 both have 3 sig figs)
 - Leading zeroes are not significant (0.001 has 1 sig fig.)
 - Trailing zeroes are not significant *unless* a decimal is in front of them (1200 has 2 sig figs, 2.00 has 3, 100 has 1, and 100. has 3).
 
 
 
## Test script 
 
 Running `test.py` should yield these results:
 
|Input| Sig Figs|Input |Sig Figs|
|---|---|---|---|
|100.0  | 4| 0.00203  | 3|
|-100.0 | 4| 1203450  | 6|
|1000   | 1| 5420     | 3|
|01000. | 4| -0.006700| 4|
|01000.0| 5| 0.06540  | 4|
|0.002  | 1| 009009.  | 4|
|0.0020 | 2| 90090.   | 5|




## Using the code

Include this in your code to use sigfigs.py. Make sure the file is in the same directory as your code.

`import sigfigs as sf`

To use the code and count sig figs, just use `sf.sfCount('0.670')` or whatever number desired. Make sure to enclose the number in quotes, or the result may be incorrect.

Additionally, this code can be used to perform operations and adhere to the rules of preserving sigfigs. After importing the file into your code just add `sf.sfMult()` for multiplying, `sf.sfDiv()` for dividing, `sf.sfAdd()` for adding, and `sf.sfSub()` for dividing.

To count sig figs, use `sf.sfCount()`, or to round sig figs, use `sf.sfRound()`.
