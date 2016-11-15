# Parallel

Parallel is a library that enables you to leverage the distributed computing power of [AWS Lambda](https://aws.amazon.com/lambda/) from Python.

# *NOT ACTUALLY FUNCTIONAL CODE (YET...)*

## Example

To illustrate how Parallel works, let's looks at a simple example. For this example, we're going to write a script that steps through a large number of arrays, and adds the values in the array. Because the set of arrays is so large, it would be helpful to perform these summation in parallel to speed up the time it takes to calculate the summations.

To start with, let's install Parallel:
```
$ pip install parallel
```

Now we'll create two files, one to hold our main program (`example.py`), and one to hold the methods we'd like to run in parallel on AWS Lambda (`add.py`).

```
# add.py

def add_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

```
# example.py

import parallel
import random

numbers = []
for num in range(0,1000000):
    numbers.append(random.sample(range(1, 100), 10))

results = []
for arr in numbers:
    with parallel():
        results.append(add_this_array(arr))

print results
```

Now we need to let Parallel know which files and methods are available to be run in parallel. We do this in the `parallel.yml` file:

```
# parallel.yml

add_this_array:
  file: add
  method: add_array
  threads: 30
```
The key `add_this_array` is the name of the method we'll calling from our `example.py` code. The key `file` is the file that contains our code. The key `method` is the name of our method in that file.  The key `threads` let's us set the number of concurrent jobs we'd like to run in parallel.

Now let's run our code locally:
```
$ parallel example.py
```
You should see something like:
```
[409, 424, 543, 571, 671, 606, 534, 623, 510, 575, ...]
```

Now let's leverage AWS Lambda to run our program in parallel.  First we need to deploy our code to AWS:

```
$ parallel deploy
```

Now let's run our code leveraging AWS:
```
$ parallel --remote example.py
```
Once again, you should see something like:
```
[409, 424, 543, 571, 671, 606, 534, 623, 510, 575, ...]
```
