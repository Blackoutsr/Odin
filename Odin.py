from random import choice
from time import sleep
p = ['andremerli74@gmail.com', 'daisyess@gmail.com', 'Edu.itaperuna@gmail.com', 'prof.janderfisica@gmail.com', 'jonathan.cassian@gmail.com']                    
t = [123123, 123456789, 1111111, 'amor123', 'nanatsunotaizai', 987654321, 'nobru123', 'abc123', 'ilovaaeyou123', 'jogador123', 'gamer123']
print('''\033[1;32m
  ___  ____ ___ _   _
 / _ \|  _ \_ _| \ | |
| | | | | | | ||  \| |
| |_| | |_| | || |\  |
 \___/|____/___|_| \_|
\033[m''')
sleep(5)
print('\033[1;33mAtenção: essa ferramenta foi criada com o objetivo de ajudar pessoas a recuperar suas contas do Free fire, caso contrário não me responsabilizo\033[m')
sleep(5)
seguranca = str(input('\033[1;36mVocê concorda com os termos? [S/N]: \033[m').strip().upper()[0]
if seguranca == 'N':
    sleep(3)
    print('\033[1;31mEncerrando ferramenta!. Você não pode usar essa ferramenta com má fé\033[m')
    sleep(5)
    quit()
id = input('\033[1;32mID: \033[m')
if id == id[0:9]:
    sleep(5)
    print('\033[1;32mID válido [√]\033[m')
    sleep(5)
    print('\033[1;32mIniciando recuperação...\033[m')
    sleep(5)
    print('\033[1;35m=\033[m'*55)
    for s in range(0, 50):
        sleep(5)
        print('\033[1;32mProcurando senha dentro da wordlist integrada em mim...\033[m')
print('\033[1;32GGmail: {}\033[m'.format(choice(p)))
print('\033[1;32SSenha: {}\033[m'.format(choice(t)))
