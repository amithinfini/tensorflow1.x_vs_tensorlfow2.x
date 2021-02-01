import tensorflow as tf

# Define the matrices
a = tf.constant([2,5,7])
b = tf.constant([1,3,8])
c = tf.constant([7,9,0])

# Compute the calculations
x = tf.add(a,b)
y = tf.multiply(x,c)

# print the output
print(x)
print(y)