list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

ans = {}
for i in list1:
    if i in list2:
        ans[i] = list1.index(i) + list2.index(i)
if len(ans) == 1:
    print(ans.keys())
key_list = list(ans.keys())
value_list = list(ans.values())
ind = []
for i in range(len(value_list)):
    if value_list[i] == min(value_list):
        ind.append(key_list[i])

print(ind)

