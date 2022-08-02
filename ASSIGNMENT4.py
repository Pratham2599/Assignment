{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c9e8728d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4, 'hello', 8, 10]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)\n",
    "ANS:-\n",
    "# solution by changing the value in index 3\n",
    "spam = [2, 4, 6, 8, 10]\n",
    "spam[2] = 'hello'\n",
    "spam"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9575ffa6",
   "metadata": {},
   "outputs": [],
   "source": [
    "1. What exactly is []?\n",
    "ANS :- [] is a empty list, which is a list value that contains no items."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "74ca587b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'d'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.\n",
    "\n",
    "3. What is the value of spam[int(int('3' * 2) / 11)]?\n",
    "ANS :-\n",
    "spam = ['a', 'b','c','d']\n",
    "spam[int(int('3' * 2) / 11)] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5cfd8c8b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'d'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "4. What is the value of spam[-1]?\n",
    "ANS :-\n",
    "spam = ['a', 'b','c','d']\n",
    "spam[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "785a8907",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5. What is the value of spam[:2]?\n",
    "ANS :-\n",
    "spam[:2] # c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "770b4df4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.\n",
    "\n",
    "6. What is the value of bacon.index('cat')?\n",
    "ANS :-\n",
    "bacon = [3.14, 'cat', 11, 'cat', True]\n",
    "bacon.index('cat')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0cebff6c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3.14, 'cat', 11, 'cat', True, 99]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "7. How does bacon.append(99) change the look of the list value in bacon?\n",
    "ANS :-\n",
    "bacon = [3.14, 'cat', 11, 'cat', True]\n",
    "bacon.append(99)\n",
    "bacon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c1dcfdf9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3.14, 11, 'cat', True]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "8. How does bacon.remove('cat') change the look of the list in bacon?\n",
    "ANS :-\n",
    "bacon = [3.14, 'cat', 11, 'cat', True]\n",
    "bacon.remove('cat')\n",
    "bacon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4ba13dc2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 4, 2, 5]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "9. What are the list concatenation and list replication operators?\n",
    "ANS :-\n",
    "# list concatination\n",
    "l1 = [1,4]\n",
    "l2 = [2,5]\n",
    "l1+l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7ab3bdd1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[7, 4, 7, 4, 7, 4]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l1 = [7,4]\n",
    "\n",
    "# list replication\n",
    "l1*3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6dd7995c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3.14, 'cat', 11, 'cat', True, 99]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10. What is difference between the list methods append() and insert()?\n",
    "ANS :-\n",
    "# append adds the item at the end of the list\n",
    "bacon = [3.14, 'cat', 11, 'cat', True]\n",
    "bacon.append(99) \n",
    "bacon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "234d4537",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4, 'hello', 6, 8, 10]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# solution by inserting value in 3rd index\n",
    "spam = [2, 4, 6, 8, 10]\n",
    "spam.insert(2,'hello')\n",
    "spam"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "6794cb26",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3.14, 11, 'cat', True]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "11. What are the two methods for removing items from a list?\n",
    "ANS :-\n",
    "# Solution by using remove method\n",
    "bacon = [3.14, 'cat', 11, 'cat', True]\n",
    "bacon.remove('cat')\n",
    "bacon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "58171d5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3.14, 'cat', 11, 'cat']"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#solution by using pop method\n",
    "bacon = [3.14, 'cat', 11, 'cat', True]\n",
    "bacon.pop()\n",
    "bacon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80e765bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "12. Describe how list values and string values are identical.\n",
    "ANS :-Lists and Strings in Python is that both are sequences.\n",
    "      1.Lists are mutable but Strings are immutable.\n",
    "      2.Both lists and strings can be passed to len()\n",
    "      3.Have indexes and slices\n",
    "      4.Can be used in for loops\n",
    "      5.Can be concatenated or replicated\n",
    "      6.Can be used with the in and not in operators"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f1ef370c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(12,)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "13. What's the difference between tuples and lists?\n",
    "ANS :-\n",
    "    Lists : are mutable - they can have values added, removed, or changed. lists use the square brackets, [ and ]\n",
    "    Tuples : are immutable; they cannot be changed at all. Tuples are written using parentheses, ( and )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "842baed3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(42,)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "14. How do you type a tuple value that only contains the integer 42?\n",
    "ANS :-\n",
    "tuple = (42,)\n",
    "tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ac81cbd4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "15. How do you get a list value's tuple form?\n",
    "ANS :-\n",
    "l1 = [2,3]\n",
    "l = tuple(l1)\n",
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6d29ee50",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 5]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "How do you get a tuple value's list form?\n",
    "ANS :-\n",
    "t1 = (3,5)\n",
    "t = list(t1)\n",
    "t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12f0b0bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "16. Variables that \"contain\" list values are not necessarily lists themselves. Instead, what do they contain?\n",
    "ANS :- They contain references to list values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e8b92cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "17. How do you distinguish between copy.copy() and copy.deepcopy()?\n",
    "ANS :- copy() create reference to original object. If you change copied object - you change the original object.\n",
    "       deepcopy() creates new object and does real copying of original object to new one."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
