# Aşamalar:
#     1. aşama: Tüm dizi elemanlarını tek tek kontrol ederek en küçüğünü bulmaya çalışırız.
#         n elemanı tek tek kontrol edeceğimiz için bu adım O(n) zaman alır.
#         Bu örnekte, 6 elemanın her birini kontrol ederiz ve en küçüğü olan 2'yi buluruz.
#     2. aşama: 2'yi başa koyduktan sonra, geriye kalan elemanlar (n-1) içinde en küçüğü bulmaya çalışırız.
#         (n-1) elemanı kontrol etmek için (n-1) zaman alır.
#         Bir sonraki en küçük eleman olan 6'yı buluruz ve 2'nin yanına yerleştiririz.
#     3. aşama: 2-6 şeklinde olan dizimizin geri kalan elemanlarını (n-2) kontrol ederiz ve bir sonraki en küçük olanı buluruz, burada 16'yı buluruz.
#         16'yı bulmak için (n-2) zaman alır.
#         16'yı 2 ve 6'nın yanına yerleştiririz.
#     4. aşama: 2-6-16'dan sonra kalan elemanlara (n-3) tek tek bakarız.
#         (n-3) elemana tek tek baktıktan sonra bir sonraki en küçük elemanı, 18'i buluruz.
#     5. aşama: 2-6-16-18'den sonra kalan elemanları (n-4) inceleriz ve geriye kalan en küçük elemanı, 22'yi buluruz.
#     6. aşama: 2-6-16-18-22'den sonra geriye bir eleman kalır ve bunu en sona yerleştiririz.

#      1. Adım: [22, 27, 16, 2, 18, 6]
#      2. Adım: [2, 22, 27, 16, 18, 6]
#      3. Adım: [2, 6, 22, 27, 16, 18]
#      4. Adım: [2, 6, 16, 22, 27, 18]
#      5. Adım: [2, 6, 16, 18, 22, 27]
#      6. Adım: [2, 6, 16, 18, 22, 27]

# Big-O Gösterimi:
#     n eleman vardır ve (n-1), (n-2), (n-3), (n-4) ... 1'e kadar devam ederiz.
#     Big-O gösterimini bulmak için bu formülü kullanırız: (n * (n-1)) / 2
#     Bu da (n^2 - n) / 2'ye eşittir.
#     Big-O gösterimini bulmak için, zamana en yüksek katkısı olan n^2'yi alırız, diğer terimlerin katkısı göz ardı edilir.
#     Böylece:
#         Insertion Sorting Big-O gösterimi: O(n^2) olur.

# Time Complexity: 
#     Average case: Aradığımız sayının(18) ortada olduğu için, bu durumda averga case olur.


# [7,3,5,8,2,9,4,15,6] 
#     1.Adım:
#         Tüm elemanları tara
#         Dizinin en küçük elemanını bul:2
#         Yerleştir: [2,7,3,5,8,9,4,15,6] 
        
#     2.Adım:
#         Yerleştirilenler dışında kalan elemanları tara
#         Dizinin en küçük ikinci elemanını bul:3
#         Yerleştir: [2,3,7,5,8,9,4,15,6] 
        
#     3.Adım:
#         Yerleştirilenler dışında kalan elemanları tara
#         Dizinin en küçük üçüncü elemanını bul:4
#         Yerleştir: [2,3,4,7,5,8,9,15,6] 
        
#     3.Adım:
#         Yerleştirilenler dışında kalan elemanları tara
#         Dizinin en küçük dördüncü elemanını bul:5
#         Yerleştir: [2,3,4,5,7,8,9,15,6] 


arr =[22,27,16,2,18,6] 

# n = int(input("Number of elements: "))
# for i in range(n):
#     element = int(input("Enter element {}: ".format(i+1)))
#     arr.append(element)

for j in range (len(arr)):
    min=arr[j];
    index=j
    for i in range(j+1,len(arr)):
        if (arr[i]<min):
            min=arr[i]
            index=i
    arr.pop(index)
    arr.insert(j, min) 
    print(str(j + 1) + ". step ==> " + str(arr))


