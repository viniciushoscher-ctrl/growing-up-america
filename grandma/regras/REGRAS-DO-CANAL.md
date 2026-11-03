# Regras do canal Grandma Ruth Remembers

Tiradas do guia de canais faceless que o Vinicius mandou em 3/11/2026, já adaptadas ao canal: dicas de Natal, receitas de Natal e receitas do dia a dia, 6 vídeos por dia, voz en_US-lessac-high, thumbs no Gemini, upload pela API.

Objetivo de tudo aqui: subir **CTR** (gente que clica), **AVD** (tempo assistido) e **RPM** (dinheiro por mil views). É isso que leva aos US$ 20 milhões até dez/2029.

Cada roteiro novo passa pelo checador antes de ir para o render:

```
python3 -I /mnt/project-files/billionaires-histories/regras/check_roteiro.py videos/grandmaNN/script.json
```

Ele sai com ERRO quando falta algo obrigatório (título, gancho, CTA no meio, loops, final) e com aviso quando é recomendado.

---

## 1. Escolha do tema (antes de escrever)

1. **Google Trends EUA** continua sendo a fonte principal (regra do Vinicius). Registrar em `trends/AAAA-MM-DD.md`.
2. **Outliers:** priorizar temas onde um vídeo de canal pequeno tem muito mais views que inscritos. Isso indica demanda sem dono.
3. **Comentários dos concorrentes (novo):** 1 vez por semana, ler os comentários dos 5 vídeos mais vistos dos canais de vovó, receitas antigas e Natal. Procurar "please make a video about", "can you do", "my grandma used to make". Guardar os pedidos em `regras/pedidos-do-publico.md` e usar como fila de temas.
4. **Comentários do nosso canal:** a pergunta do final de cada vídeo vira tema. Se 3 pessoas citam o mesmo prato, ele entra na fila.
5. **Títulos dos concorrentes:** colar a lista de títulos e pedir "sugira ideias novas a partir disso". Nunca copiar o título: manter o formato e trocar o ângulo.
6. **SCAMPER** em cada tema do Trends, para achar o ângulo que ninguém fez:
   - **Substituir:** fudge de chocolate → fudge de manteiga de amendoim da Ruth.
   - **Combinar:** biscoito de Natal + presente caseiro = "cookies em pote para dar de presente".
   - **Adaptar:** receita de 1955 adaptada para air fryer ou panela elétrica.
   - **Modificar:** versão para 2 pessoas, versão de US$ 10, versão em 15 minutos.
   - **Outro uso:** sobra do peru vira sopa; potes de vidro viram enfeite.
   - **Eliminar:** "sem forno", "sem batedeira", "só 3 ingredientes".
   - **Inverter:** "o que NÃO fazer", "o erro que estraga", "por que o seu fica duro".
7. **Ideias de canais infantis:** desafios, "qual você escolhe", contagem regressiva e antes/depois funcionam para o público adulto também (ex.: "Rate my grandkids' gingerbread houses").

## 2. Título

- **45 a 70 caracteres.** Acima de 70 corta no celular. O checador recusa.
- **Palavra-chave no começo:** "Christmas Fudge…", "Pinto Beans…", "Christmas Tree Mistakes…".
- **Padrão do canal:** número ou dor/erro + uma palavra em MAIÚSCULAS. Moldes que já usamos e continuam valendo:
  - `The [prato] EVERYONE's Grandma Made (Why Yours [dor em MAIÚSCULAS])`
  - `[7/9/11] Christmas [tema] Mistakes That Make It Look CHEAP`
  - `[prato] That NEVER [problema] (Grandma's [3/5] Secrets)`
- **Números ímpares** (3, 5, 7, 9, 11) nas listas: parecem mais precisos.
- **Dor + solução:** dizer o problema que a pessoa tem (seco, duro, sem graça, barato) e prometer o conserto.
- **Urgência sazonal** quando couber: "Before Christmas", "This Year", "Before Thanksgiving".
- **"You/Your"** deixa pessoal: "Why YOUR Tree Looks Cheap".
- Não prometer o que o vídeo não entrega. Clique enganado derruba a AVD e a confiança do canal.
- Se o título passar de 70, cortar o parêntese primeiro.

## 3. Thumbnail

Continua valendo a referência de Natal (Ruth realista, suéter vermelho, cenário de Natal, apontando, X vermelho, ✓ verde, setas e círculos). O guia acrescenta:

- **3 a 5 palavras** no texto da thumb, nunca mais.
- **Título e thumb dizem a mesma coisa, sem repetir:** o título faz a pergunta, a thumb mostra a resposta ou o problema (ex.: título "Why Your Fudge Turns GRAINY", thumb com fudge granulado com X e fudge liso com ✓).
- **Emoção no rosto da Ruth:** surpresa, desaprovação ou "olha isso". Rosto neutro clica menos.
- **Contraste forte:** objeto bem iluminado em fundo mais escuro ou desfocado; texto branco/amarelo com contorno preto.
- **Teste no tamanho do celular:** reduzir para 320×180 e ver se ainda se entende em 1 segundo.
- **Mesmo estilo em todas** (marca reconhecível na página inicial).

## 4. Roteiro (o checklist)

A voz fala cerca de **146 palavras por minuto**. 30 s ≈ 73 palavras.

| Momento | O que precisa ter | Obrigatório |
|---|---|---|
| 0–30 s (bloco 1, até 75 palavras) | **Gancho:** uma frase forte, fato surpreendente ou memória com emoção. Nada de "hello, welcome back". | sim |
| 30–60 s (bloco 2) | **Promessa:** o que a pessoa vai levar ("tonight I'm giving you…, every step, and the 4 reasons…"). **Curiosity gap:** citar o erro principal e não dizer qual é ("and mistake number three is the one that ruins most…, I'll get to it"). | sim |
| A cada 2–3 min | **Loop aberto / mini cliffhanger:** "in a minute I'll tell you…", "the biggest mistake is coming up", "but first…". Pelo menos 1 a cada 3 min. | sim |
| Entre 15% e 60% | **CTA no meio, logo depois de uma dica boa:** "If this just saved your fudge, tap the like button, it helps Grandma more than you know." Curto e natural. | sim |
| Meio | **Revelação aos poucos:** em listas, guardar o melhor item para o fim e avisar isso no começo. | sim |
| Meio | **Recapitulação** de onde estamos ("so far: fresh beans, the soak, the simmer… now the part everyone gets wrong"). | recomendado |
| Meio | **Pergunta ao espectador** no meio ("do you add sugar? tell me below"). | recomendado |
| Fim | **Payoff:** entregar tudo que foi prometido no início. Resumo em uma lista. | sim |
| Últimos 2 blocos | **Pergunta para os comentários** + **levar ao próximo vídeo/playlist:** "Grandma's fudge is in the next video right on your screen" / "the whole Christmas playlist is right there". | sim |

Outros pontos do roteiro:
- **Emoção:** cada vídeo tem pelo menos uma memória da Ruth com sentimento (família, saudade, humor). É o que diferencia de um canal de receita comum.
- **Ritmo:** misturar frases longas com frases curtas de impacto. Cortar enrolação.
- **Capítulos:** 1 a cada 2 ou 3 minutos (viram as seções no YouTube).
- **Legendas vermelhas:** até 5 palavras.
- **Confiança:** receita certa, medidas certas, nada de mito apresentado como fato.
- **Melhorar uma coisa a cada vídeo** (regra final do guia).

## 5. Edição (pipeline)

Não buscar perfeição: o jogo é volume com qualidade constante. O que o render precisa garantir:
- **Pattern interrupt a cada ~60 s:** a Ruth falando (SadTalker), troca de capítulo com cartão, zoom ou mudança de clipe. Nunca a mesma imagem parada por mais de 8–10 s.
- **B-roll em movimento** (clipes Prelinger e fotos com movimento), cortes de 3 a 8 por bloco.
- **Texto na tela** nas medidas e nos erros (a legenda vermelha), setas ou destaque no ingrediente-chave.
- **Som:** voz limpa, música baixa por baixo, um efeito curto na virada de capítulo.
- **Cor:** quente e consistente (cozinha antiga, luz de Natal).
- **Tela final** com o próximo vídeo e a playlist, nos últimos 20 s.

## 6. Upload

- Título e descrição com a palavra-chave nas primeiras linhas; capítulos com tempo na descrição.
- Sempre numa playlist (Natal ou Grandma Ruth's Kitchen). Playlist é o que encadeia a maratona.
- Tela final e card apontando para o vídeo citado no roteiro.
- Marcar "AI was used" e dizer que a Ruth é personagem (já é regra).
- Fixar um comentário com a pergunta do vídeo.

## 7. Análise (toda segunda-feira)

1. **Impressões primeiro**, depois CTR e AVD (regra do vídeo 1 de conhecimento).
2. **CTR abaixo de 4% com impressões boas após 48 h:** trocar thumb; se em mais 48 h não subir, trocar o título. Trocar embalagem é mais barato que fazer vídeo novo.
3. **AVD:** olhar o gráfico de retenção dos 3 vídeos piores. Onde cai, ver o que o roteiro diz ali (enrolação, dica fraca, imagem repetida) e virar regra nova neste arquivo.
4. **Formato vencedor:** comparar dicas de Natal × receitas de Natal × receitas do dia a dia em views por vídeo e RPM. O que ganhar recebe mais dos 6 slots do dia.
5. Registrar tudo em `regras/analise-AAAA-MM-DD.md`.

## 8. RPM e renda além do AdSense

- Receitas e casa/decoração têm anunciantes fortes no 4º trimestre (Natal). Vídeos de 10 a 14 min já permitem anúncios no meio; manter acima de 8 min.
- **Afiliados (próximo passo, depende do Vinicius):** Amazon Associates para utensílios citados (forma de ferro, pote de feijão, cortador de biscoito, enfeites). Link na descrição.
- **Depois de crescer:** livro de receitas da Ruth (PDF), comunidade, membros do canal.

## 9. Conta e algoritmo

- Sem truques: o que sobe o canal é gente assistindo até o fim e voltando.
- Regularidade: 6 vídeos por dia, em horários fixos.
- Nada que fira as diretrizes (confiança do canal).

---

O que ficou de fora do guia, a pedido do Vinicius: contratar freelancers e comprar canais prontos.
