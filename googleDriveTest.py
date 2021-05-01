import requests

GOOGLE_SHEET_ID = '17gF7RNOpDnllSEBVj7JJaSzaOSRicojU9JpKyVnLfxA'
GOOGLE_SHEET_PAGE_IDS = {'Grain+Bran':265995474,
                         'Corn+Rice':1122722752,
                         'Sugar':2109322920}

for page_name,page_id in GOOGLE_SHEET_PAGE_IDS.items():
    csv_url=f"https://docs.google.com/spreadsheet/ccc?key={GOOGLE_SHEET_ID}&gid={page_id}&output=csv"
    response = requests.get(csv_url)
    assert response.status_code == 200, 'Wrong status code'
    with open(f"cereal_{page_id}.csv", "w") as f:
        f.write(response.text)

#https://doc-04-7o-sheets.googleusercontent.com/export/3vjgu2dt0cfl5ot89nhhod63rg/77kd15f50plej04v5fsfgaolpc/1619873480000/103633697030264563844/115439790302271250414/17gF7RNOpDnllSEBVj7JJaSzaOSRicojU9JpKyVnLfxA?format=csv&id=17gF7RNOpDnllSEBVj7JJaSzaOSRicojU9JpKyVnLfxA&gid=265995474&dat=AMvwolZ5O4xCmNhFC4ZTSNUupmyInE4lmAjW6_5MXqg4vblZf-WKKspeUer-OJUC6-MypycH5WpRzOAB0yoqqETvC2Itp-iSbnn0tQtYxG2DqtLiudPesmA9kuJ6SCQ8ABlne_annBzv_FVIGJp1QGffWzuRp_94LqWXpLynWhb8BiYxEHsSM8iyFB-jJOcBEAC4HWogVdhjy2C8jmUC6ptDsqSd5wlk41ynHjYEqLTcQ2L0lXCeyxFmWoNPaQPo_0HqzAL0vhPX1JqT6GDAVSOfe_ePU3G4wMXvaQTv0ek6eAJOxjHLZN2QVqL2wNBOEjh7yWpDj92H5trIgFL2dEl465_TKji-SwV4ZHZFZWMn4IyoKtvzoJbvR_Snwbbh0O06Xdpr7fFL3Y3wNXPLCbt1nI75zl5gF1pBroQ7cBgXeAvUlajdSLfM46sLUVcoRGoux_K50QcNjg2zUU63-eH1DrLQKauMkYUTW3cka9yYher0V842So4Q-PDs_Cs76DDNu2FgE4zDchn9LOzC60Bb322I6QaMR0OVe901n3p39Jb8t-it67gD_8toe5zwyXXecDDSQMYY9A5caJeMuPIiTjqiosd9shI-MkpT-w76PVjPpy5mjxmwT_DnPOTtbaGTRc2JkpPUTiaG_ZjGiuultXwiHWwu_qXQ07Pqetg9Mur-nRyV1jiGY6khak_7xcSceiHUkjIPkSd7zvNwDHBOT7iJ9c0