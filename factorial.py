#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 * factorial2k, Copyright (c) 2016-2017, Henrique Moura (h3dema)
 * All rights reserved.
 *
 * If you have questions about your rights to use or distribute this
 * software, please contact h3dema@outlook.com.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 * 4. Neither the name of author nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE H3DEMA AND CONTRIBUTORS
 * ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
 * TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE FOUNDATION OR CONTRIBUTORS
 * BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
"""
"""
  factorial2k returns the matrix for a 2k factorial analisys


"""
import numpy as np
from scipy.misc import comb
from combinations import generate_combinations


def num_combinations(n):
    """
    calculates the number of possible combinations of n factors
    using C(n,1) + C(n, 2) + ... + C(n,n)
    :param n: number of factors to fully combine
    :return: number of possible combinations
    """
    assert n > 0, "n must be greater than zero."
    total = 0
    for i in range(n):
        total += comb(n, i, exact=True)
    return total

def binary(v, size):
    value = bin(v)[2:]
    return '0' * (size - len(value)) + value


def decimal_value_to_factor_value_list(i, size):
    values = list(binary(i,size))
    values = [2*int(i)-1 for i in values]
    return values

def factorial2k(number_of_factors):
    """
    Create a 2-Level full-factorial design
    :param number_of_factors: The number of factors (k) in the 2k factorial design
    :return matrix: a 2d-array with coded levels -1 and 1 for the factors
    """
    assert number_of_factors > 0, "Should be one or more factors"
    matrix = []
    for i in range(2**number_of_factors):
        values = decimal_value_to_factor_value_list(i, size=number_of_factors)
        matrix.append(values)

    return np.array(matrix)


def contrasts_factorial2k(number_of_factors):
    """
    Create a 2-Level full-factorial design
    :param number_of_factors: The number of factors (k) in the 2k factorial design
    :return matrix: a 2d-array with coded levels -1 and 1 for the factors and full combination
    """
    assert number_of_factors > 0, "Should be one or more factors"
    n = num_combinations(number_of_factors)

    items = list(range(number_of_factors))
    combinations = generate_combinations(items)

    matrix = []
    for i in range(2**number_of_factors):
        values = decimal_value_to_factor_value_list(i, size=number_of_factors)
        entry = []
        for comb in combinations:
            value = 1
            for idx in comb:
                value *= values[idx]
            entry.append(value)
        matrix.append(entry)

    return np.array(matrix), combinations

def index(v):
    p = 0
    for i in v:
        p = (p + (i + 1) / 2 ) * 2
    p /= 2
    return p

def generate_model(matrix):
    # step 1) same number of y's?
    correct_number_of_y = True
    num_y = len(matrix[0][-1])

    number_of_factors = len(matrix[0])-1

    for i in range(1,len(matrix)):
        if num_y != len(matrix[i][-1]):
            correct_number_of_y = False
            break
    assert correct_number_of_y, "Each value should have the same number of y measures"

    # step 2) system of equations
    x, combinations = contrasts_factorial2k(number_of_factors)
    c = np.ones(2**number_of_factors)
    x = np.insert(x, 0, c, axis=1) # insert column c


    ym = np.zeros(2**number_of_factors)
    for l in matrix:
        p = index(l[0:-1])
        ym[p] = np.mean(l[-1])
    b, r, rank, s = np.linalg.lstsq(x, ym)

    r = [ [0] * num_y for i in range(2**number_of_factors) ]
    for l in matrix:
        p = index(l[0:-1])
        residual = l[-1] - ym[p]
        r[p] = residual

    return b, r

if __name__ == "__main__":

    factors = ['a', 'b']

    example = [[-1, -1, [28, 25, 27]],
               [+1, -1, [36, 32, 32]],
               [-1, +1, [18, 19, 23]],
               [+1, +1, [31, 30, 29]],
               ]

    number_of_factors = len(factors)
    contrasts, combinations = contrasts_factorial2k(number_of_factors=number_of_factors)
    i = 0
    for entry in contrasts:
        print binary(i,number_of_factors), '\t', entry
        i += 1

    b, r = generate_model(example)
    print "Coeficients: ", b
    print "Residuals  : ", r

