# America That We Love

Canal "America That We Love" (o repositório mantém o nome antigo, growing-up-america): canal faceless em inglês no YouTube: documentários calmos e nostálgicos sobre a vida americana de 1950 a 1985, para o público 55+ dos EUA. O narrador fala direto com o espectador ("you"), usa fotos reais de arquivo e fatos com fonte.

A produção segue o mesmo modelo do canal Pickup Reality (repositório `american-trucks`, guia `agendamento/GUIA-REPLICAR-CANAL.md`). O Claude escreve o roteiro e o GitHub Actions baixa as fotos, narra, edita, corta os Shorts e agenda tudo no YouTube.

## Os 3 ângulos do canal (3 vídeos por dia)

| Horário (Nova York) | Ângulo | Molde de título | Exemplo |
|---|---|---|---|
| 9h | Jornada de um ano | Growing Up in [ANO] America: [promessa de perda ou emoção] | Growing Up in 1955 America: The World That Vanished Forever |
| 14h | Marco de idade ou fase da vida | If You Turned 18 in [ANO], This Is What Adulthood Really Looked Like | If You Turned 18 in 1957, This Is What Adulthood Really Looked Like |
| 19h | Tema do dia a dia | What Every American [X] Had in [ANO] (That Nobody Remembers Now) | What Every American Kitchen Had in 1962 (That Nobody Remembers Now) |

O uploader converte os horários de Nova York para UTC sozinho, inclusive na troca do horário de verão. No horário de Brasília, isso dá 10h, 15h e 20h até 31/10/2026 e 11h, 16h e 21h a partir de 1/11/2026.

## Títulos

O título é a parte mais importante. A regra, feita com dados de outliers do nicho e de outros nichos, está em **[TITULOS.md](TITULOS.md)**. Leia antes de criar qualquer título. A pesquisa é atualizada pelo workflow `titles` (`set` = `nostalgia` ou `other`).

## Padrão de cada vídeo

- **Duração:** 30 a 40 minutos, ou seja, de 4.400 a 5.800 palavras com a voz em `length_scale` 1.45.
- **Voz:** Piper `en_US-ryan-high`, grátis e rodando no próprio runner.
- **Imagens:** só fotos reais do Wikimedia Commons (CC ou domínio público, JPEG de pelo menos 2000 px, em paisagem). Nada de imagem gerada por IA.
- **Edição:** zoom lento em cada foto, tag marrom-sépia no canto com a legenda da cena e legendas queimadas por último, para nunca saírem de sincronia.
- **Estrutura:** abertura em cena ("close your eyes, it's September 1955…"), capítulos com um gancho em cada um, fatos com fonte, fechamento emocional e pergunta nos comentários ("What year did you turn 10?").
- **Shorts:** 5 por vídeo longo, cortados automaticamente.

## Estrutura do repositório

| Caminho | O que é |
|---|---|
| `videos/videoNN/make_script.py` | O roteiro em blocos. Rodar `python3 make_script.py` gera os arquivos abaixo e mostra a duração estimada. |
| `videos/videoNN/script.json` | O vídeo como dados: cenas com `text`, `query` (busca de fotos), `caption` e `cuts`. É o que o render usa. |
| `videos/videoNN/sources.md` | As fontes dos fatos do vídeo. |
| `videos/videoNN/ROTEIRO-revisao.md` | Versão para ler e revisar, com os tempos de cada capítulo. |
| `pipeline/` | `fetch_media.py` (fotos), `build.py` (narração, edição e legendas), `shorts.py`, `yt_upload.py`, `scriptkit.py` e `review_md.py`. |
| `.github/workflows/` | `photocheck` (testa as buscas de fotos sem baixar nada), `render`, `shorts`, `pacotes` (uma Release por vídeo), `thumbs` e `youtube` (agendamento diário). |
| `agendamento/` | `calendar.json` (o que sai em cada dia), `meta/` (título, descrição e tags), `thumbs/`, `creditos/` e `youtube-state.json`. |
| `docs/` | Página do app, política de privacidade e termos (GitHub Pages), exigidos pelo Google para a API. |

## Status

| Vídeo | Título | Cenas | Duração estimada | Situação |
|---|---|---|---|---|
| video01 | Growing Up in 1955 America: The World That Vanished Forever | 96 | cerca de 33 min | roteiro pronto |
| video02 | If You Turned 18 in 1957, This Is What Adulthood Really Looked Like | 83 | cerca de 31 min | roteiro pronto |
| video03 | What Every American Kitchen Had in 1962 (That Nobody Remembers Now) | 81 | cerca de 30 min | roteiro pronto |

## Próximos passos

1. Rodar o **photocheck** com `video01 video02 video03` e corrigir as buscas que trouxerem fotos erradas.
2. Rodar o **render** do `video01` e revisar o preview e os frames na branch `deliveries-video01`. Esse é o teste de qualidade antes de produzir em lote.
3. Criar o canal no YouTube, verificar o telefone e a conta no Studio e criar um projeto no Google Cloud com OAuth próprio (passo a passo no guia do american-trucks, seção 5).
4. Cadastrar os secrets `YT_CLIENT_ID`, `YT_CLIENT_SECRET` e `YT_REFRESH_TOKEN` e rodar o workflow **youtube** no modo `check`.
5. Ativar o GitHub Pages (Settings > Pages > branch `main`, pasta `/docs`) e pedir a auditoria da API.
6. Preencher `agendamento/calendar.json` e deixar o agendamento diário publicar.

## Como rodar um workflow

GitHub > aba **Actions** > escolha o workflow > **Run workflow** > preencha o campo (por exemplo, `video01`).

Nunca cole o valor de um secret no chat, em issue ou em commit.
