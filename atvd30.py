# crie uma função que calcule a media de 3 notas, em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7.

def calcular_media(n1, n2, n3):
    media = (n1+n2+n3)/3  
    
    return media
    
def verificar_media(media):
    if media >= 7:
        return "Aprovado"
    else: 
        return "Reprovado"

n1, n2, n3 = map(float, input("digite a nota 1, 2 e 3: ").split())   

resulMedia = calcular_media(n1, n2, n3)
print(f"{resulMedia:.1f}")
resulFinal = verificar_media(resulMedia)
print(resulFinal)
    

    

