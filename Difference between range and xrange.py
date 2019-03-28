#range([start,] stop[, step])，根据start与stop指定的范围以及step设定的步长，生成一个序列。
>>> range(5) 
[0, 1, 2, 3, 4] 
>>> range(1,5) 
[1, 2, 3, 4] 
>>> range(0,6,2)
[0, 2, 4]

#xrange 用法与 range 完全相同，所不同的是生成的不是一个list对象，而是一个生成器。
>>> xrange(5)
xrange(5)
>>> list(xrange(5))
[0, 1, 2, 3, 4]
>>> xrange(1,5)
xrange(1, 5)
>>> list(xrange(1,5))
[1, 2, 3, 4]
>>> xrange(0,6,2)
xrange(0, 6, 2)
>>> list(xrange(0,6,2))
[0, 2, 4]

#要生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要一上来就开辟一块很大的内存空间。

#xrange 和 range 这两个基本上都是在循环的时候用。
a = range(0,100) 
print type(a) 
print a 
print a[0], a[1] 
#虽然输出的结果一样，但是range输出的是list对象

<type 'list'>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
0 1
#而xrange则不会直接生成一个list，而是每次调用返回其中的一个值：
a = xrange(0,100) 
print type(a) 
print a 
print a[0], a[1]

#输出结果：
<type 'xrange'>
xrange(100)
0 1


