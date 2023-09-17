from time import sleep
import pyotp
import qrcode

chave_mestra = "K4XO47QRE75L4KTTPM775SOY4ESGSMIN"

codigo = pyotp.TOTP(chave_mestra)


codigo_usuario = input("Digite seu codigo de autenticação. ")

#escaneie o Qr_code para adicionar o codigo
print(codigo.verify(codigo_usuario))

link = pyotp.TOTP(chave_mestra).provisioning_uri(name="Rafael", issuer_name="teste de autenticação")

meu_qrcode = qrcode.make(link)
meu_qrcode.save("meu_QRcode.png")
