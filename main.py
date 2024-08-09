import time
from hwcounter import Timer

from tests.cache_access import test_l1, test_l2, test_l3
from tests.direct_indirect_class_access import test_class_access_getattr, test_class_access_getitem, test_map_access, test_direct_access
from tests.enum_string_int import test_enum_int, test_enum_string, test_enum_string_long
from tests.eval_dynamic_key import test_with_eval, test_without_eval
from tests.float_int_arthimetic import test_float_arithmetic, test_int_arithmetic
from tests.functional_imperative import test_functional_numbers, test_imperative_numbers
from tests.large_obj import test_large_obj_direct, test_large_obj_indirect
from tests.sequental_random_access import test_sequential_access, test_random_access
from tests.shapes import test_shape_monomorphic, test_shape_polymorphic, test_shape_megamorphic
from tests.specialized import test_not_specialized, test_specialized
from tests.string_mutation_concatenation import test_string_mutation, test_string_concatenation


with Timer() as t:
    time.sleep(1)

cycles_per_second = t.cycles

# test_enum_string, test_enum_int, test_shape_monomorphic, test_shape_polymorphic, test_shape_megamorphic, functional_numbers, imperative_numbers, test_class_access, test_map_access, test_direct_access
for test in [test_specialized, test_not_specialized]:
    run_count = 10
    # avg = 0
    avg_cycles = 0
    for i in range(0, run_count):
        # t = time.perf_counter_ns()
        # test()
        # tt = time.perf_counter_ns() - t
        # avg += tt
        
        with Timer() as t:
            test()
        avg_cycles += t.cycles
    # avg /= run_count
    # print(f"{test.__name__} avg ms:", avg / 1000 / 1000)
    avg_cycles /= run_count
    print(f'{test.__name__}: avg cycles = {avg_cycles}, time taken = {avg_cycles / cycles_per_second * 1000} ms')

    