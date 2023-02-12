import re
from scraper import Scrapper
import json

if __name__ == "__main__":
    scraper = Scrapper()

    datas = scraper.get_data()
    index = 1

    # Result JSON Data
    result = json.dumps(datas)
    print(result)

    # Count JSON Data
    item = json.loads(result)
    print("\n Data Count : ", len(item))

    for data in datas:
        harga_awal = str(data['harga'])
        split = re.split(r'Rp', harga_awal)
        splits = str(split[1])
        hasil = splits.replace(".", "")
        rate = str(data['jumlah_terjual'])

    jumlah = hasil + hasil

    average = int(jumlah) / len(item)

    if int(hasil) >= int(average):
        print("\n Layak beli")
    else:
        print("\n Biasa Saja")

    # print("\n Average : ",
    #       int(jumlah) / len(item)
    #       )

    # split = np.char.replace(split[1], data, '')
    # print(split[1])
    # print("\n Rata - rata : " +
    #       list(map(float, split[1])) +
    #       list(map(float, split[1])) / len(item)
    #       )

    #
    # for data in datas:
    #     print(
    #         index,
    #         data['id'],
    #         data['nama'],
    #         data['harga'],
    #         # data['deskripsi'],
    #         data['penjual'],
    #         data['rating'],
    #         data['jumlah_terjual']
    #     )

    #     index += 1
