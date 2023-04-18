'''
Description:

Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...


Calculate the sum of the numbers in the nth row of this
triangle (starting at index 1)


e.g.: (Input --> Output)
1 -->  1
2 --> 3 + 5 = 8


The solution was obtained by realizing what each row has
in common, which turns out to be that the row number is
the cube root of the row's sum.

e.g.:
1 is the product of 111 = 1
8 is the product of 222 = 8
27 is the product of 333 = 27
The sum of any row of odd numbers is just the row number cubed.

'''

def row_sum_odd_numbers(n):
    return pow(n, 3)