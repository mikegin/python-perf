import time
from hwcounter import Timer
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from tests.string_comparison import test_compare_int, test_compare_string, test_compare_string_long, test_compare_float
from tests.shapes import test_shape_monomorphic, test_shape_polymorphic, test_shape_megamorphic
from tests.functional_methods import test_functional_numbers, test_imperative_numbers
from tests.indirection import test_class_access_getattr, test_class_access_getitem, test_map_access, test_direct_access
from tests.sequental_random_access import test_sequential_access, test_random_access
from tests.cache_access import test_l1, test_l2, test_l3, test_ram
from tests.large_obj import test_large_obj_direct, test_large_obj_indirect
from tests.eval_dynamic_key import test_with_eval, test_without_eval
from tests.string_mutation_concatenation import test_string_mutation, test_string_concatenation
from tests.specialized import test_not_specialized, test_specialized
from tests.comprehensions import test_comprehensions, test_regular_loops
from tests.float_int_arthimetic import test_float_arithmetic, test_int_arithmetic
from tests.data_structures import test_list, test_set
from tests.numpy import test_regular_float_sum, test_numpy_float_sum, test_builtin_float_sum
from tests.numpy_with_array_type import test_regular_float_sum_with_array, test_numpy_float_sum_with_array, test_builtin_float_sum_with_array
from tests.unrolling import test_sum_list_unrolled_0, test_sum_list_unrolled_2, test_sum_list_unrolled_4, test_sum_list_unrolled_8, test_sum_list_unrolled_16
from tests.unrolling_cython import test_cython_sum_list_unrolled_0, test_cython_sum_list_unrolled_2, test_cython_sum_list_unrolled_4, test_cython_sum_list_unrolled_8, test_cython_sum_list_unrolled_16


tests = [
    # test_compare_int, test_compare_string, test_compare_string_long, test_compare_float
    
    # test_shape_monomorphic, test_shape_polymorphic, test_shape_megamorphic,
    
    # test_functional_numbers, test_imperative_numbers,
    
    # test_class_access_getattr, test_class_access_getitem, test_map_access, test_direct_access,
    
    # test_sequential_access, test_random_access,
    
    # test_l1, test_l2, test_l3, test_ram,
    
    # test_large_obj_indirect, test_large_obj_direct
    
    # test_with_eval, test_without_eval,
    
    # test_string_mutation, test_string_concatenation,
    
    # test_not_specialized, test_specialized,

    # test_list, test_set,
    
    # test_regular_loops, test_comprehensions,
    
    # test_float_arithmetic, test_int_arithmetic,
    
    # test_regular_float_sum, test_numpy_float_sum, test_builtin_float_sum,
    
    # test_regular_float_sum_with_array, test_numpy_float_sum_with_array, test_builtin_float_sum_with_array,
    
    # test_sum_list_unrolled_0, test_sum_list_unrolled_2, test_sum_list_unrolled_4, test_sum_list_unrolled_8, test_sum_list_unrolled_16,
    
    test_cython_sum_list_unrolled_0, test_cython_sum_list_unrolled_2, test_cython_sum_list_unrolled_4, test_cython_sum_list_unrolled_8, test_cython_sum_list_unrolled_16
    
]

with Timer() as t:
    time.sleep(1)

cycles_per_second = t.cycles

print("Running tests...")

sizes = [10 ** i for i in range(1, 7)] # 10, 100, 1000... 1 million
runs = 30

cycles_per_test = []
for i in range(len(sizes)):
    size_dimension = []
    cycles_per_test.append(size_dimension)
    for j in range(len(tests)):
        test_dimension = []
        size_dimension.append(test_dimension)
        
total_cycles_per_test = []
for i in range(len(sizes)):
    total_cycles_per_test.append([0] * len(tests))



for s, size in enumerate(sizes):
    
    print(f"\n\nSize: {size}")
    
    for i in range(0, runs):
        
        print(f"\nRun {str(i)}:")
        
        for t, test in enumerate(tests):
            
            with Timer() as timer:
                test(size)
            
            cycles = timer.cycles
            
            print(f'{test.__name__}: cycles = {cycles}, time taken = {cycles / cycles_per_second * 1000} ms')
            
            cycles_per_test[s][t].append(cycles)
            total_cycles_per_test[s][t] += cycles


# Perform statistical tests
print("\nStatistical Significance")
for s, size in enumerate(sizes):
    print("\nSize", size)
    for i in range(0, len(tests) - 1):
        for j in range(i + 1, len(tests)):
            test1_cycles = cycles_per_test[s][i]
            test2_cycles = cycles_per_test[s][j]
            print(f"{tests[i].__name__} cycles=", test1_cycles)
            print(f"{tests[j].__name__} cycles=", test2_cycles)
            t_stat, p_value = stats.ttest_ind(test1_cycles, test2_cycles, equal_var=False)
            print(f"t-statistic: {t_stat}, p-value: {p_value}")

            if p_value < 0.05:
                print("There is a statistically significant difference between the two tests.")
            else:
                print("No statistically significant difference was found between the two tests.")
            
            print() # new line
    



print("\nSize, " + ', '.join([test.__name__ for test in tests]))
avg_cycles = []
time_taken_ms = []

for s, size in enumerate(sizes):
    avg_cycles_row = []
    time_taken_row = []
    
    for idx, test in enumerate(tests):
        
        avg_cycle = total_cycles_per_test[s][idx] / runs
        
        time_taken = avg_cycle / cycles_per_second * 1000
        
        avg_cycles_row.append(avg_cycle)
        time_taken_row.append(time_taken)
        
    print(f'{size}, ' + ', '.join(map(lambda x: str(x), time_taken_row)))
    
    avg_cycles.append(avg_cycles_row)
    time_taken_ms.append(time_taken_row)




## Bar Graphs ##

# Number of sizes
# n_sizes = len(sizes)

# # Create a subplot for each size
# fig, axs = plt.subplots(n_sizes, 1, figsize=(10, 2 * n_sizes))

# for idx, size in enumerate(sizes):
#     axs[idx].bar(range(len(tests)), time_taken_ms[idx], tick_label=[test.__name__ for test in tests])
    
#     axs[idx].set_ylim(0, max(time_taken_ms[idx]))
#     axs[idx].set_ylabel('Time (ms)')
#     axs[idx].set_title(f'Size: {size}')
#     axs[idx].grid(True, axis='y', ls="--")

# plt.tight_layout()
# plt.show()




## Line Graph ##

# Plotting the data with discrete points for each test and size
plt.figure(figsize=(12, 6))

# Plot each test with markers and annotate each point with the exact time
for idx, test in enumerate(tests):
    times = [row[idx] for row in time_taken_ms]
    plt.plot(sizes, times, marker='o', label=test.__name__)
    for i, time in enumerate(times):
        plt.annotate(f'{time:.3f}', (sizes[i], time), textcoords="offset points", xytext=(0,8), ha='center', rotation=45)

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Size')
plt.ylabel('Time Taken (ms)')
plt.legend()
plt.show()