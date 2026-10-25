# Regra de título do canal

O título é a parte mais importante do vídeo. Esta regra vem de dados reais, coletados pelo workflow `titles` em 25/10/2026:
- **Nosso nicho:** 305 vídeos longos de nostalgia de 150 canais (`research/titles/latest.md`).
- **Outros nichos:** 217 vídeos longos de 150 canais, entre os mais vistos do mês (`research/titles/other.md`).

**Como medimos:** a nota de outlier é a view do vídeo dividida pela mediana de views dos últimos 30 vídeos do mesmo canal. A mediana do nicho é **11,5x**. Uma nota alta indica que o título puxou o vídeo para muito além do normal daquele canal.

## 1. O que funciona no nicho de nostalgia

| Mecânica | Nota (mediana) | Exemplo real |
|---|---|---|
| **Psicologia de quem viveu a época** | **cerca de 480x** (4 vídeos) | *Psychology of People Who Grew Up in the 1970s*: 1,4M de views, 688x · *If You Grew Up In The 1970s, You Probably Possess These Rare Traits*: 1,2M |
| **Promessa emocional** ("It will make you cry") | **cerca de 100x** | *Growing Up in the 1950s... It will make you cry*: 845 mil, 845x |
| **Cozinha e casa** | **25x** | *11 Old Kitchen Features That Have Vanished Over Time*: 1,3M · *A Step Saving Kitchen, 1949*: 3,9M |
| **"Ilegal hoje" ou choque** | **24x** | *You Won't Believe the ILLEGAL Things People Did in the 1970s*: 1,2M |
| **Ano específico** (1955 em vez de "1950s") | **23x**, contra 10x da década | *What Everyday Life Really Looked Like in the 1950s*: 5,8M |
| **"Só quem viveu lembra"** ou "as crianças de hoje não entendem" | **20x** | *20 Things From The 1960s, Kids Today Will Never Understand!*: 919 mil |
| **Esquecido, sumiu, nunca mais** | **14x** | *100 Things From 1950s America That Are FORGOTTEN Today*: 1,24M num canal de 15 mil inscritos |
| Número na frente ("25 Forgotten Meals…") | 11x | *25 Forgotten Meals Every Family In 1950s Ate Weekly*: 880 mil |
| **"Growing Up in…" sozinho** | **3,6x (fraco)** | Funciona só quando vem com uma promessa extra |

## 2. O que funciona em outros nichos agora, adaptado para o nosso

| Mecânica de outro nicho | Exemplo real (este mês) | Versão para o nosso canal |
|---|---|---|
| **What Happened to X?** | *What Happened to Zombie Catchers?*: 928 mil num canal de 2,3 mil inscritos | *What Happened to the Milkman?* · *What Happened to the American Drive-In?* |
| **The Rise and Fall of X** | *The Turkey Leg Hut: The Rise & Fall of a Houston Empire*: 1,07M em 8,4 mil inscritos | *The Rise and Fall of Woolworth's* · *The Rise and Fall of the Sears Catalog* |
| **The TRUTH About X (It's Not What You Think)** | *The TRUTH About Biphasic Sleep As You Get Older*: 895 mil, público mais velho | *The TRUTH About Life in 1955 (It's Not What You Remember)* |
| **O que você NUNCA viu, contado por quem estava lá** | *What Happens to Your Body Inside a Sealed Casket*: 1,2M em 4,8 mil inscritos | *What Every 1950s Housewife Knew That Nobody Tells You Now* |
| **Lacrado ou intocado há décadas** | *Breathtaking WW1 battlefield… untouched since the war*: 9,1M | *Inside an American Home Untouched Since 1962* |
| **Then and Now** | *60+ Most Beautiful Actresses of 1970s and 1980s: Then and Now*: 831 mil em 12 mil inscritos | *1950s Main Street, Then and Now* |
| **Derrubar mitos** | *Debunking the biggest myths history made you believe*: 2,3M | *7 Myths About the 1950s Everyone Still Believes* |
| **Por que ficou tão caro** | *Why Smartphones Got So Expensive: The Hidden Tax Nobody Talks About*: 1,8M | *Why a House Cost $11,000 in 1955 (And What Really Changed)* |

## 3. A regra (checklist para todo título)

1. **Fale com "você" e com a idade ou o ano da pessoa.** Ano exato vale mais que década: *1957* vence *the 1950s*.
2. **Prometa uma perda ou uma descoberta.** Use palavras como forgotten, vanished, gone forever, nobody remembers, really looked like, the truth, what happened to.
3. **Coloque uma emoção ou um choque**, de preferência um só: it will make you cry, you won't believe, illegal today.
4. **Escreva no máximo uma palavra em MAIÚSCULAS**, a palavra-chave: FORGOTTEN, TRUTH, ILLEGAL.
5. **Use entre 55 e 70 caracteres.** Prefira afirmação a pergunta, exceto no "What Happened to…?".
6. **Nunca use "Growing Up in [ANO]" sozinho.** Sempre acrescente uma promessa (o mundo que sumiu, a emoção, a jornada).
7. **Não copie títulos.** Os moldes não têm dono; os títulos têm.
8. **Teste A/B:** todo vídeo sai com um título reserva usando outra mecânica da tabela.

## 4. Trends e datas para aproveitar

- **Halloween (31/10):** *What Halloween Was Really Like in 1958 America*
- **Thanksgiving (26/11/2026):** *Thanksgiving 1955: The Dinner Every American Family Remembers*
- **Natal:** *Christmas in 1962 America: The Things That Vanished Forever*. É a data mais forte do ano para lembranças de família.
- **Mecânicas em alta este mês:** "What happened to…", "Rise and fall", "The truth about".

## 5. Títulos do dia 1, revisados

| Horário | Antes | Agora | Reserva para teste A/B |
|---|---|---|---|
| 9h | Growing Up in 1955 America: From Your First Bicycle to Your First Car | **Growing Up in 1955 America: The World That Vanished Forever** | If You Were 7 Years Old in 1955, This Was Your World |
| 14h | If You Turned 18 in 1957, This Is What Adulthood Really Looked Like | **mantido** (ano exato + "you" + "really looked like") | If You Turned 18 in 1957, You Grew Up Faster Than Anyone Today |
| 19h | What Every American Kitchen Had in 1962 (That Nobody Remembers Now) | **mantido** (cozinha + ano + "nobody remembers") | 25 Things Every 1962 Kitchen Had That Vanished Forever |

**Limites desta pesquisa:** a busca do YouTube favorece vídeos antigos e grandes, e não temos a data de cada vídeo, só o total de views. Vamos rodar o workflow `titles` toda semana e ajustar a regra com os nossos próprios números (CTR e retenção).
