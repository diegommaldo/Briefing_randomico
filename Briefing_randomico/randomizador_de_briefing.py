### Randomizador de Briefings para exercícios ###
### por Diego Maldonado

import random

### Suportes & Temas -----------

# colocar aqui opcoes de suporte
suporte = {'Revista' : 1, 'Site' : 2, 'Livro' : 3, 'Jornal' : 4}

# colocar aqui opcoes de tema
tema = {'moda' : 1, 'automobilismo' : 2, 'beleza' : 4, 'gastronomia' : 5, 'universo masculino' : 6, 'universo feminino' : 7, 'universo infantil' : 8, 'esportes' : 9, 'design' : 10, 'quadrinhos' : 11, 'musica rock' : 12, 'musica gospel' : 13, 'musica brasileira' : 14, 'musica jazz' : 15, 'saude' : 16, 'universo teen feminino' : 17, 'universo teen masculino' : 18, 'universo gay masculino' : 19, 'erotismo' : 20, 'cultura mexicana' : 21, 'cultura tailandesa' : 22, 'cultura alema' : 23, 'computacao grafica' : 24, 'casos policiais' : 25, 'cultura baiana' : 26, 'cultura carioca' : 27, 'cultura paulistana' : 28, 'design grafico' : 29, 'design de produto' : 30, 'decoracao' : 31, 'arquitetura' : 32, 'propaganda' : 33, 'mercado financeiro' : 34, 'setor imobiliario' : 35, 'cinema' : 36, 'tecnologia' : 37, 'games' : 38, 'cerveja' : 39, 'vinhos' : 40, 'turismo' : 41, 'artes plasticas' : 42, 'advocacia' : 43, 'animacao' : 44, 'universo gay feminino' : 45, 'universo transsexual' : 46, 'fotografia' : 47, 'oncologia' : 48, 'humor' : 49, 'o Brasil' : 50, 'a Italia' : 51, 'futebol' : 52, 'a Islandia' : 53, 'o Egito' : 54, 'esportes radicais' : 55, 'aves' : 56, 'repteis' : 57, 'mamiferos' : 58, 'cavalos' : 59, 'o nordeste brasileiro' : 60, 'seu bairro' : 61, 'igreja catolica' : 62, 'igreja evangelica' : 63, 'religiao judaica' : 64, 'religiao muculmana' : 65, 'curiosidades cientificas' : 66, 'casamento' : 67}

briefing = random.choice(suporte.keys()) + ' sobre ' + random.choice(tema.keys())

print briefing