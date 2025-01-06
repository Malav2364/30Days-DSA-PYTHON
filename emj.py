# lst = [2,5,7,9,12,34,56]

# mn = min(lst)
# mx = max(lst)
# print(f'Minimum value is :{mn} and Maximum value is :{mx}')

srr = [4,5,6,8,2,1]
for i in range(len(srr)):
    for j in range(i + 1, len(srr)):
        if srr[i] > srr[j]:
            srr[i, srr[j]] = srr[j], srr[i]

print(f'Sorted array is: {srr}')