h_atual=int(input("Digite a hora: "))
m_atual=int(input("Digite o minuto: "))
s_atual=int(input("Digite o segundo: "))
zero_h = h_atual*3600
zero_m = m_atual*60
zero_s = s_atual*1
total_segundos = zero_h+zero_m+zero_s
print("O total de segundos é: ", total_segundos)
