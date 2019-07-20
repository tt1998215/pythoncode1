import tensorflow as tf
try:
    tf.contrib.eager.enable_eager_execution()
except ValueError:
    pass
tensor=tf.constant("hello,world")
tensor_value=tensor.numpy()
print (tensor_value)