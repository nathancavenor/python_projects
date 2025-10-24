import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, op = None, value = None, left = None, right = None):
        self.op = op
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.op is None:
            return str(self.value)
        return f"({self.left}{self.op}{self.right})"

    def eval(self):
        try:
            if self.op is None:
                return self.value
            
            left_val = self.left.eval()
            right_val = self.right.eval()

            if self.op == "+":
                return left_val + right_val
            elif self.op == "-":
                return left_val - right_val
            elif self.op == "*":
                return left_val * right_val
            elif self.op == "/":
                if right_val == 0:
                    return np.nan
                return left_val / right_val

        except ZeroDivisionError:
            return np.nan

def generate_trees(nums):
    if len(nums)== 1:
        yield Node(value=nums[0])
        return
    
    for i in range(1, len(nums)):
        left_nums = nums[:i]
        right_nums = nums[i:]

        for left in generate_trees(left_nums):
            for right in generate_trees(right_nums):
                for op in ["+", "-", "*", "/"]:
                    yield Node(op, None, left, right)

nums = [7, 7, 3, 6, 1, 10]

answers = []
for tree in generate_trees(nums):
    val = tree.eval()
    answers.append(val)
    print(tree, "=", val)

target = 798
count = sum(1 for v in answers if np.isclose(v, target))
print(f"{count} results are approximately equal to {target}")

plt.hist(answers, bins=30, edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution of Expression Results")
plt.show()

