def base(x):
  def plus(y):
    return x + y
  return plus

plus = base(10)
print(plus(10))
print(plus(30))

def add_num():
  def plus(y):
    return i + y
  return plus

i = 10
plus = add_num()
print(plus(10))
i = 100
print(plus(30))


# # """

# # pip install pep8
# # pip install flake8
# # pip install pylint


# # """

# # import roboter.controller.conversation

# # class MainError(Exception):
# #     pass

# # def main():
# #         roboter.controller.conversation.talk_about_restaurant()
# #         raise MainError('Error')
    

# # x = [(i, x, y) for i in (1, 2, 3) for x in (1, 2, 3) for y in (1, 2, 3)]

# # d = {'key1': 'value1', 'key2': 'value2'}
# # if 'key1' in d:
# #     print('test')

# # if 'key1' in d.keys():
# #     print('test')

# # for k, v in ranking.items():
# #     print(k, v)

# # if __name__ == '__main__':
# #     main()

# def t():
#   # num = []
#   for i in range(10):
#     yield i

# for i in t():
#   print(i)

# def other_func(f):
#   print(f(10))

# def test_func(x):
#   return x * 2
# def test_func2(x):
#   return x * 5
# other_func(test_func)
# other_func(test_func2)

# other_func(lambda x: x * 2)
# other_func(lambda x: x * 5)

# y = 'test_func'
# x = i if y else 2
# print(x)
