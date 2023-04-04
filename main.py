import requests
i = 0
while i <17:
    link = 'https://store.steampowered.com/wishlist/id/dark_kuzya1/wishlistdata/?p=' + str(i)
    r = requests.get(link)
    with open('text.cvs', 'w', encoding='UTF-8') as text:
        text.write(r.text)
    with open('text.cvs', 'r', encoding='UTF-8') as text:
        for line in text:
            stringWithAppId = line
    array = stringWithAppId.split('"name":"')
    newArray = []
    for item in array:
        newArray.append(item.split('","capsule"'))
    resultArray = []
    for item in newArray:
        resultArray.append(item[0])
    resultArray = resultArray[1:]
    with open('wishlist_result.txt', '+a', encoding='UTF-8') as res:
        for item in resultArray:
            res.write(item + ' \n')
    i += 1
