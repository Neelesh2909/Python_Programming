# import time
#
# my_list = [i for i in range(3000)]
#
# total = 3000
#
#
# def total_sum_case_1(given_list, total_sum):
#     start_time = time.process_time() * 1000
#     for i in range(len(given_list)):
#         for j in range(i+1, len(given_list)):
#             if given_list[i] + given_list[j] == total_sum:
#                 end_time = time.process_time() * 1000
#                 total_time_taken = end_time - start_time
#                 return i, j, total_time_taken
#
#     end_time = time.process_time() * 1000
#     total_time_taken = end_time - start_time
#     return -1, -1, total_time_taken
#
#
# index_1, index_2, time_taken = total_sum_case_1(my_list, total)
#
# print(f'{index_1}, {index_2}, {time_taken}')
#
#
# def total_sum_case_2(given_list, total_sum):
#     start_time = time.process_time() * 1000
#     given_list.sort()
#     first_index = 0
#     last_index = len(given_list) - 1
#     while first_index != last_index:
#         if given_list[first_index] + given_list[last_index] == total_sum:
#             end_time = time.process_time() * 1000
#             total_time_taken = end_time - start_time
#             return first_index, last_index, total_time_taken
#
#         elif given_list[first_index] + given_list[last_index] > total_sum:
#             last_index -= 1
#         elif given_list[first_index] + given_list[last_index] < total_sum:
#             first_index += 1
#     end_time = time.process_time() * 1000
#     total_time_taken = end_time - start_time
#     return -1, -1, total_time_taken
#
# ind_1, ind_2, total_time_taken = total_sum_case_2(my_list, total)
# print(f'ind_1 {ind_1}, ind_2: {ind_2}, time {total_time_taken}')


