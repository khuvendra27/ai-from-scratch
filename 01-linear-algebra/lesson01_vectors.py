import math

import numpy as np
import math as m
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


# calculating cosine similarity between vectors
def cosine_similarity(v1,v2):
     dot = np.dot(v1,v2)
     n1 = np.linalg.norm(v1)
     n2 = np.linalg.norm(v2)

     return dot / (n1 * n2)

print("cosine similarity function calling for cat and dog",cosine_similarity(cat,dog))
print("cosine similarity function calling for cat and car",cosine_similarity(cat,car))

# calculating the length of a vector
def vector_length(v):
    length_squared  = 0
    for i in range(len(v)):
        length_squared  += v[i] ** 2
    return math.sqrt(length_squared )

print("vector length function calling",vector_length(cat))
