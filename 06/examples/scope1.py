global_ = 42


def f():
    local_ = 43
    print('local_:', local_)
    print('global_:', global_)


print('global_:', global_)
print('local_:', local_)  # NameError
