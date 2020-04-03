import random
f = 10
while f>0:
    co = True
    pt = False
    if co:
        print('Fase: COME OUT')
        print('Apostas disponiveis: Pass Line Bet, Field, Any Craps, Twelve.')
        print('Se quiser encerrar o jogo, digite \'quit\'')
        aposta_do_jogador = input('Qual é a sua aposta? ')
        if aposta_do_jogador == 'quit':
            co = False
            pt = False
            print('Você terminou o jogo com {0} fichas'.format(f))
            break
        if aposta_do_jogador == 'Pass Line Bet':
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            sd = d1 + d2
            print('Você possui {0} fichas'.format(f))
            fichas_apostadas = int(input('Quantas fichas você vai apostar? '))
            f = f - fichas_apostadas
            if sd == (7 or 11):
                fichas_apostadas = fichas_apostadas * 2
                f = f + fichas_apostadas
                print('Os dados deram {0} e {1}, somando um total de {2}. Você venceu a aposta!'.format(d1, d2, d1 + d2))
                print('Você recebeu {0} fichas nessa aposta. Seu total agora é {1}'.format(fichas_apostadas, f))
                co = False
                pt = True
            if sd == (2 or 3 or 12):
                fichas_apostadas = fichas_apostadas * 0
                print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1,d2,sd))
                print('Seu total de fichas é: {0}'.format(f))
                co = False
                pt = True
            else:
                co = False
                pt = True
                if pt:
                    print('Fase: POINT')
                    print('Apostas disponiveis: Field, Any Craps, Twelve.')
                    print('Se quiser encerrar o jogo, digite \'quit\'')
                    aposta_do_jogador = input('Qual é a sua aposta? ')
                    if aposta_do_jogador == 'Pass Line Bet':
                        print('Aposta indisponível')
                    if aposta_do_jogador == 'quit':
                        pt = False
                        co = False
                        print('Você terminou o jogo com {0} fichas'.format(f))
                        break
                    if aposta_do_jogador == 'Field':
                        d1 = random.randint(1, 6)
                        d2 = random.randint(1, 6)
                        sd = d1 + d2
                        if 5 or 6 or 7 or 8:
                            fichas_apostadas = fichas_apostadas * 0
                            print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1, d2,sd))
                            print('Seu total de fichas é {0}'.format(f))
                            co = True
                            pt = False
                        elif sd == 3 or 4 or 9 or 10 or 11:
                            fichas_apostadas = fichas_apostadas * 2
                            f = f + fichas_apostadas
                            print('Os dados deram {0} e {1}, somando um total de {2}. Você ganhou a aposta!'.format(d1,d2,sd))
                            print('Você recebeu {0} fichas nessa aposta. Seu total agora é {1}'.format(fichas_apostadas,f))
                            co = True
                            pt = False
                        elif sd == 2:
                            fichas_apostadas = fichas_apostadas * 3
                            f = f + fichas_apostadas
                            print('Os dados deram {0} e {1}, somando um total de {2}. Você ganhou a aposta!'.format(d1,d2,sd))
                            print('Você recebeu {0} fichas nessa aposta. Seu total agora é {1}'.format(fichas_apostadas,f))
                            co = True
                            pt = False
                    if aposta_do_jogador == 'Any Craps':
                        d1 = random.randint(1, 6)
                        d2 = random.randint(1, 6)
                        sd = d1 + d2
                        print('FICHAS: {0}'.format(f))
                        fichas_apostadas = int(input('Quantas fichas você vai apostar? '))
                        f = f - fichas_apostadas
                        if sd == 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11:
                            fichas_apostadas = fichas_apostadas * 0
                            print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1, d2,sd))
                            print('Seu total de fichas é {0}'.format(f))
                            co = False
                            pt = True
                        else:
                            fichas_apostadas = fichas_apostadas * 12
                            print(
                                'Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1, d2,sd))
                            print('Seu total de fichas é {0}'.format(f))
                            co = False
                            pt = True
                    if aposta_do_jogador == 'Twelve':
                        d1 = random.randint(1, 6)
                        d2 = random.randint(1, 6)
                        sd = d1 + d2
                        if sd == 12:
                            fichas_apostadas = fichas_apostadas * 30
                            f = f + fichas_apostadas
                            print('Ambos os dados deram 6, somando um total de 12. Parabéns! Você venceu a aposta!')
                            print('Você recebeu {0} fichas nessa aposta. Seu total agora é {1}'.format(fichas_apostadas,f))
                            co = True
                            pt = False
                        else:
                            fichas_apostadas = fichas_apostadas * 0
                            print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1, d2,sd))
                            print('Seu total de fichas é {0}'.format(f))
        if aposta_do_jogador == 'Field':
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            sd = d1 + d2
            print('FICHAS: {0}'.format(f))
            fichas_apostadas = int(input('Quantas fichas você vai apostar? '))
            f = f - fichas_apostadas
            if 5 or 6 or 7 or 8:
                fichas_apostadas = fichas_apostadas * 0
                print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1,d2,sd))
                print('Seu total de fichas é {0}'.format(f))
                co = False
                pt = True
            elif sd == 3 or 4 or 9 or 10 or 11:
                fichas_apostadas = fichas_apostadas * 2
                f = f + fichas_apostadas
                print('Os dados deram {0} e {1}, somando um total de {2}. Você ganhou a aposta!'.format(d1,d2,sd))
                print('Você recebeu {0} fichas nessa aposta. Seu total agora é {1}'.format(fichas_apostadas,f))
                co = False
                pt = True
            elif sd == 2:
                fichas_apostadas = fichas_apostadas * 3
                f = f + fichas_apostadas
                print('Os dados deram {0} e {1}, somando um total de {2}. Você ganhou a aposta!'.format(d1,d2,sd))
                print('Você recebeu {0} fichas nessa aposta. Seu total agora é {1}'.format(fichas_apostadas, f))
                co = False
                pt = True
        if aposta_do_jogador == 'Any Craps':
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            sd = d1 + d2
            print('FICHAS: {0}'.format(f))
            fichas_apostadas = int(input('Quantas fichas você vai apostar? '))
            f = f - fichas_apostadas
            if sd == 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11:
                fichas_apostadas = fichas_apostadas * 0
                print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1,d2,sd))
                print('Seu total de fichas é {0}'.format(f))
                co = False
                pt = True
            else:
                fichas_apostadas = fichas_apostadas * 12
                print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1,d2,sd))
                print('Seu total de fichas é {0}'.format(f))
                co = False
                pt = True
        if aposta_do_jogador == 'Twelve':
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            sd = d1 + d2
            print('FICHAS:{0}'.format(f))
            fichas_apostadas = int(input('Quantas fichas você vai apostar? '))
            f = f - fichas_apostadas
            if sd == 12:
                fichas_apostadas = fichas_apostadas * 30
                f = f + fichas_apostadas
                print('Ambos os dados deram 6, somando um total de 12. Parabéns! Você venceu a aposta!')
                print('Você recebeu {0} fichas nessa aposta. Seu total agora é {1}'.format(fichas_apostadas,f))
                co = False
                pt = True
    if pt:
        print('Fase: POINT')
        print('Apostas disponiveis: Field, Any Craps, Twelve.')
        print('Se quiser encerrar o jogo, digite \'quit\'')
        aposta_do_jogador = input('Qual é a sua aposta? ')
        if aposta_do_jogador == 'Pass Line Bet':
            print('Aposta indisponível')
        if aposta_do_jogador == 'quit':
            pt = False
            co = False
            print('Você terminou o jogo com {0} fichas'.format(f))
            break
        if aposta_do_jogador == 'Field':
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            sd = d1 + d2
            print('Você possui {0} fichas'.format(f))
            fichas_apostadas = int(input('Quantas fichas você vai apostar? '))
            f = f - fichas_apostadas
            if 5 or 6 or 7 or 8:
                fichas_apostadas = fichas_apostadas * 0
                print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1,d2,sd))
                print('Seu total de fichas é {0}'.format(f))
                co = True
                pt = False
            elif sd == 3 or 4 or 9 or 10 or 11:
                fichas_apostadas = fichas_apostadas * 2
                f = f + fichas_apostadas
                print('Os dados deram {0} e {1}, somando um total de {2}. Você ganhou a aposta!'.format(d1,d2,sd))
                print('Você recebeu {0} fichas nessa aposta. Seu total agora é {1}'.format(fichas_apostadas,f))
                co = True
                pt = False
            elif sd == 2:
                fichas_apostadas = fichas_apostadas * 3
                f = f + fichas_apostadas
                print('Os dados deram {0} e {1}, somando um total de {2}. Você ganhou a aposta!'.format(d1,d2,sd))
                print('Você recebeu {0} fichas nessa aposta. Seu total agora é {1}'.format(fichas_apostadas, f))
                co = True
                pt = False
            if aposta_do_jogador == 'Any Craps':
                d1 = random.randint(1, 6)
                d2 = random.randint(1, 6)
                sd = d1 + d2
                print('FICHAS: {0}'.format(f))
                fichas_apostadas = int(input('Quantas fichas você vai apostar? '))
                f = f - fichas_apostadas
                if sd == 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11:
                    fichas_apostadas = fichas_apostadas * 0
                    print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1, d2, sd))
                    print('Seu total de fichas é {0}'.format(f))
                    co = False
                    pt = True
                else:
                    fichas_apostadas = fichas_apostadas * 12
                    print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1, d2, sd))
                    print('Seu total de fichas é {0}'.format(f))
                    co = False
                    pt = True
            elif sd == 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11:
                fichas_apostadas = fichas_apostadas * 0
                print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1,d2,sd))
                print('Seu total de fichas é {0}'.format(f))
                co = True
                pt = False
        if aposta_do_jogador == 'Twelve':
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            sd = d1 + d2
            print('FICHAS:{0}'.format(f))
            fichas_apostadas = int(input('Quantas fichas você vai apostar? '))
            f = f - fichas_apostadas
            if sd == 12:
                fichas_apostadas = fichas_apostadas * 30
                f = f + fichas_apostadas
                print('Ambos os dados deram 6, somando um total de 12. Parabéns! Você venceu a aposta!')
                print('Você recebeu {0} fichas nessa aposta. Seu total agora é {1}'.format(fichas_apostadas,f))
                co = True
                pt = False
            else:
                fichas_apostadas = fichas_apostadas * 0
                print('Os dados deram {0} e {1}, somando um total de {2}. Você perdeu a aposta'.format(d1,d2,sd))
                print('Seu total de fichas é {0}'.format(f))
        if f<0:
            print('Suas fichas acabaram. Fim de jogo!')
            break