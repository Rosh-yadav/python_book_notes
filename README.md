# python_book_notes

## LISTS in Python

1. List = collection of items
   Example: a = ['a', 'b', 'c']

2. Index starts from 0
   a[0] → first item

3. Negative index:
   a[-1] → last item

4. Modify:
   a[0] = 'new'

5. Add:
   append() → end
   insert(index, value)

6. Remove:
   del → delete
   pop() → remove + use
   remove() → by value

7. Lists are dynamic (can change anytime)


### Organizing Lists

1. sort() → permanent sorting
2. sorted() → temporary sorting
3. reverse() → reverse order
4. len() → number of items

Index Error:
  - Happens when index is out of range
  - Index starts from 0

For Loop:
- Used to loop through list
- Syntax:
     for item in list:
         print(item)

- Used to avoid repetition



  ############
  ###  FOR LOOP:
- for item in list:
    do something

- runs for every item

INDENTATION:
- indent = inside loop
- no indent = outside loop

RANGE:
- range(start, end)
- end not included

LIST:
- list(range())

LIST COMPREHENSION:
- [value for value in range()]

FUNCTIONS:
- min(), max(), sum()

SLICING:
- list[start:end]
- [:] → full copy

COPY LIST:
- new = old[:]
