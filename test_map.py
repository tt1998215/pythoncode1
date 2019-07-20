# def normalize(name):
#     for ch in name:
#         s1=name[:1].upper()
#     for ch in name:
#         s2=name[1:].lower()
#     return s1+s2
# L=['sJKjf','hDJdjhf','HHkjdfk']
# s=list(map(normalize,L))
# print(s)
import tensorflow as tf
sess = tf.Session()
a = tf.constant(1)
b = tf.constant(2)
print(sess.run(a+b))