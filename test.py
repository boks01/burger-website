import time


# full_order = []
# # with open("order_list.txt", "a") as order_list:
# #     order_list.write("nasi\n")
# with open("order_list.txt", "r") as order_list:
#     p = order_list.read()
#     full_order = p.split()
# how_len = len(full_order)
# print(how_len)
hasil = ['nasi', "babi", "kambing", "sapi"]
for i in range(0, len(hasil)):
    print(hasil[i])
    time.sleep(0.5)