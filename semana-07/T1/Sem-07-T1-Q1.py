def idade(d_at, m_at, a_at, d_ns, m_ns, a_ns):
    dia = abs(d_at - d_ns)
    mes = abs(m_at - m_ns)
    ano = a_at - a_ns
    return f'{ano} {mes} {dia}'

def main():
    dia_at = int(input().strip())
    mes_at = int(input().strip())
    ano_at = int(input().strip())
    dia_ns = int(input().strip())
    mes_ns = int(input().strip())
    ano_ns = int(input().strip())
    id = idade(dia_at, mes_at, ano_at, dia_ns, mes_ns, ano_ns)
    print(id)

if __name__ == '__main__':
    main()
