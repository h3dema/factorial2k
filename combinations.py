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
import itertools


def generate_combinations(items):
    """
    
    :param items: the list of items to combine (without repetition)
    :return: a list of tuples. each tuple contains the index for each item that is in the combination  
    """
    assert isinstance(items, list) and (len(items) > 0), "items should be a list with elements"
    n = len(items)
    stuff = range(n)
    comb = []
    for L in range(1, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            comb.append(subset)
    return comb


def transform_combinations(items, combinations, as_string=False):
    tcomb = []
    for comb in combinations:
        this_comb = []
        for item in comb:
            this_comb.append(items[item])
        if as_string:
            this_comb = "".join(this_comb)
        tcomb.append(this_comb)
    return tcomb

if __name__ == "__main__":
    items = list(range(3))
    combinations = generate_combinations(items)
    print items, ' n# comb=', len(combinations), ':', combinations

    items = ['a', 'b', 'c']
    combinations = generate_combinations(items)
    print items, ' n# comb=', len(combinations), ':', combinations
    tcomb = transform_combinations(items, combinations)
    print tcomb
    tcomb = transform_combinations(items, combinations, as_string=True)
    print tcomb