# factorial2k

## The factorial 2k design

The factorial 2k design is a special case of the general factorial design.
These designs are usually referred to as screening designs.
The 2k designs are a major set of building blocks for many experimental designs.
It´s very widely used in industrial experimentation.

The 2k refers to designs with k factors where each factor has just two levels. These designs are created to explore a large number of factors, with each factor having the minimal number of levels, just two. By screening we  refer to the process of screening a large number of factors that might be important in your experiment, with the goal of selecting those important for the response that you're measuring.
The number k of factors can get quite large.
In this context we need to decide which factors are important.

In 2k designs, the levels are referred as high and low, +1 and -1, to denote the high and the low level of each factor.
In most cases the levels are quantitative, although they don't have to be. Sometimes they are qualitative, such as gender, or two types of variety, brand or process. In these cases the +1 and -1 are simply used as labels.
Interpretation of data can proceed largely by common sense, elementary
arithmetic, and graphics.
For quantitative factors, we can’t explore a wide region of factor space, but
determine promising directions


## Our module by example

To use our module, just import the module.
You must create a list of the variables, as shown below

```python
    factors = ['a', 'b']
```

To enter data, you should create a matrix with n lines. Each line correspond to a combination of the factors. Each line contains a list of values. The first values correspond to the contrast. One for each factor. As our example has 2 factors, our matrix must have 4 lines. Each line has three entries. The first element corresponds to 'a', the second to 'b', and the third contains a list with all values of y - we show 3 repetitions below.

```python
    example = [[-1, -1, [28, 25, 27]],
               [+1, -1, [36, 32, 32]],
               [-1, +1, [18, 19, 23]],
               [+1, +1, [31, 30, 29]],
               ]
```
To perform the design, call the factorial2k() method. It returns a python dictionary with all the results of the analysis.

```python
    result = factorial2k(factors, example)
```

Calling print_result_factorial() prints a format result on the screen.

```python
    print_result_factorial(result)
```

# Bibliografy

DOUGLAS C. MONTGOMERY. Design and Analysis of Experiments. Eighth Edition. Hoboken: John Wiley & Sons, 2013. Chapter 6 - The 2k Factorial Design.

Angela Dean, Daniel Voss and Danel Draguljić - Design and Analysis of Experiments. Second Edition. Dayton : Springer International Publishing, 2017. Chapter 7 - Several Crossed Treatment Factors.
