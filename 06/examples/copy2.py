original_list = [1, 2, 3, [4, 5, 6]]
shallow_copy1 = original_list.copy()
shallow_copy2 = original_list[:]  # same as copy()
shallow_copy1[3][0] = 42
shallow_copy2[1] = 35

print(original_list) #[1,2,3,[42,5,6]]
print(shallow_copy1) #[1,2,3,[42,5,6]]
print(shallow_copy2) #[1,35,3,[42,5,6]]
