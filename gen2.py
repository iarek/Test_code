def simple_gen_function():
  yield 1
  yield 2
  yield 3

for value in simple_gen_function():
  print(value)


new_gen = simple_gen_function()

next(new_gen)
print(next(new_gen))
next(new_gen)
