import base64

encoded_string = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT="

# Decode the Base64 string
decoded_bytes = base64.b64decode(encoded_string)

# decoded_bytes.decode('utf-8')
decoded_string = decoded_bytes.decode('utf-8')

print(decoded_string)

# Freedom Flotilla,Resistancu,Liberation,Frue PalustineGaza%easefire,Protest,UORWA