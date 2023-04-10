import PySimpleGUI as kpn

def string_ke_biner(string):
    biner = ""
    for char in string:
        biner += format(ord(char), '08b')
    return biner

def string_ke_decimal(string):
    decimal = ""
    for char in string:
        decimal += str(ord(char))
    return decimal

def string_ke_octal(string):
    octal = ""
    for char in string:
        octal += format(ord(char), '03o')
    return octal

def string_ke_hexadecimal(string):
    hexadecimal = ""
    for char in string:
        hexadecimal += format(ord(char), '02X')
    return hexadecimal

layout = [
    [kpn.Text("Masukkan string yang ingin anda konversikan : ",font=("poppins", 16), background_color='#DEB887', text_color='#800000')],
    [kpn.Text("Hasil: ",background_color='#DEB887', font=("Helvetica", 12), text_color='#800000'), kpn.Text("",background_color='white', font=("Helvetica", 12), text_color='#228B22', key="output")],
    [kpn.InputText(key="input", size=(70,1)), kpn.Button("Hapus", font=("Helvetica"), button_color='#800000', key="hapus")], 
    [kpn.Text("Pilih yang ingin di konversi: ",font=("poppins", 12, "bold"), background_color='#DEB887', text_color='#800000')],
    [kpn.Radio("Biner", "konversi", key="biner", background_color='#DEB887', text_color='#800000' )],
    [kpn.Radio("Desimal", "konversi", key="decimal", background_color='#DEB887', text_color='#800000')],
    [kpn.Radio("Oktal", "konversi", key="octal", background_color='#DEB887', text_color='#800000')],
    [kpn.Radio("Hexadesimal", "konversi", key="hexadecimal", background_color='#DEB887', text_color='#800000')],
    [kpn.Radio("ASCII", "konversi", key="ascii", background_color='#DEB887', text_color='#800000')],
    [kpn.Button("Konversi", font=("Helvetica"), button_color='#800000', size=(25, 1)),kpn.Button("Keluar", font=("Helvetica"), button_color='#800000', size=(25, 1))],
]

window = kpn.Window('Converter', layout, background_color='#DEB887')

while True:
    event, values = window.read()
    if event == kpn.WIN_CLOSED or event == "Keluar":
        break
    if event == "Konversi":
        string = values["input"]
        if not string: # jika input kosong
            hasil = "" # hasil diisi dengan string kosong
        elif values["biner"]:
            hasil = string_ke_biner(string)
        elif values["decimal"]:
            hasil = string_ke_decimal(string)
        elif values["octal"]:
            hasil = string_ke_octal(string)
        elif values["hexadecimal"]:
            hasil = string_ke_hexadecimal(string)
        elif values["ascii"]:
            hasil = ' '.join(str(ord(char)) for char in string)
        window["output"].update(hasil)
    if event == "hapus":
        window["input"].update("")

window.close()