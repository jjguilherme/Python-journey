def obter_media():
    media = float(input("Digite a media: "))
    return media


def calc_media(media1, media2, media3, media4):
    med_bi = (media1 + media2 + media3 + media4) / 4
    return med_bi


media1 = obter_media()
media2 = obter_media()
media3 = obter_media()
media4 = obter_media()

calcula = calc_media(media1, media2, media3, media4)

print(calcula)
