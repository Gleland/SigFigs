This inspiration came from when I was in grad school, trying to finish my god awful data and error analysis assignments. Basically, how can you trust the computer (or programming language) to conserve whatver significant figure you have during a calculation? Here are the rules regarding sig figs, which can be found at [Wikipedia](https://en.wikipedia.org/wiki/Significant_figures) with more detail, but any Google search will yield the same results.



 - All non-zero digits are significant (843 is 3 sig figs)
 - Zeroes that are in between two non-zero digits are significant (404, 808, etc. have 3 sig figs)
 - Leading zeroes are not significant (0.001 has 1 sig fig.)
 - Trailing zeroes are not significant *unless* a decimal is in front of them (1200 has 2 sig figs, 2.00 has 3, 100 has 1, and 100. has 3).
 
 Included in this repository are `sigfigs.py`, which has the code to count the number of significant figures in a number, and `test.py `, which will allow the user to run a test to confirm whether the code works in its method.
