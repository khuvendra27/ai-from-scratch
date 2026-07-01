import numpy as np

cat = np.array([0.5,0.2])
dog = np.array([0.4,0.1])
car = np.array([3,2])

print(cat)
print(dog)
print(car)


# vector additions

cat_dog = cat +dog

print("performing vector addition",cat_dog)

# vector multiplication

big_cat = 2*cat

print("vector multiplication",big_cat)

# magnitude length

cat_length = np.linalg.norm(cat)

print("cat_length",cat_length)

# dot product

dot = np.dot(cat,dog)

print("dot",dot)

def dot_product(v1,v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]

    return result

print("dot product function calling",dot_product(cat,dog))
