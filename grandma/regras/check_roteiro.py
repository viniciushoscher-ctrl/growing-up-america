"""Checa um script.json da Grandma Ruth contra REGRAS-DO-CANAL.md (título, gancho, CTAs, loops, final).
Uso: python3 check_roteiro.py videos/grandma31/script.json [...]   -> sai com código 1 se houver ERRO."""
import json, re, sys

WPM = 212 / 1.45  # palavras por minuto na voz lessac com length_scale 1.45 (~146)
LOOPS = r"in a minute|in a moment|later|at the end|i'll tell you|i'll show you|stay with me|but first|before i|wait until you|the one that|number one|the biggest|the worst|coming up|don't skip|you'll see why"
LIKE = r"\b(tap|hit|press|click|give)\b[^.]{0,40}\b(like|thumbs)|\bsubscribe\b|\bsubscribed\b"
NEXT = r"next video|playlist|tomorrow|next one|on your screen|right after this|watch next|link"
RECAP = r"so far|so remember|so one more time|so the (one|two|three|four|five|six|seven|eight|nine|ten)|let's recap|that's (one|two|three)"


def check(path):
    d = json.load(open(path)); sc = d["scenes"]; erros, avisos = [], []
    t = d["title"]
    if not 45 <= len(t) <= 70: erros.append(f"título com {len(t)} caracteres (quero 45 a 70): {t}")
    if not re.search(r"\b[A-Z]{3,}\b", t): erros.append("título sem palavra em MAIÚSCULAS")
    if not re.search(r"\d|never|mistake|why|wrong|stop|avoid|cheap|dry|hard|bland|soggy|tough|gummy", t, re.I):
        avisos.append("título sem número nem dor/erro")
    words = [len(s["text"].split()) for s in sc]; total = sum(words)
    mins = total / WPM
    if words[0] > 75: erros.append(f"gancho com {words[0]} palavras (>30 s); corte para no máximo 75")
    intro = " ".join(s["text"] for s in sc[:2]).lower()
    if not re.search(r"today|tonight|i'm going to|i'll show|i'll give|i'm giving|every step|here's|you'll", intro):
        avisos.append("os 2 primeiros blocos não dizem o que a pessoa vai ganhar (promessa)")
    alltext = [s["text"].lower() for s in sc]
    nloops = sum(len(re.findall(LOOPS, x)) for x in alltext)
    if nloops < max(3, int(mins / 3)): erros.append(f"só {nloops} loops abertos; quero 1 a cada 3 min (~{max(3,int(mins/3))})")
    acc, mid = 0, False
    for w, x in zip(words, alltext):
        if 0.15 <= acc / total <= 0.6 and re.search(LIKE, x): mid = True
        acc += w
    if not mid: erros.append("falta CTA de like/inscrição no meio (entre 15% e 60% do vídeo)")
    if not any(re.search(RECAP, x) for x in alltext[len(sc)//3:]): avisos.append("sem recapitulação no meio/fim")
    end = " ".join(alltext[-2:])
    if "comment" not in end or "?" not in end: erros.append("final sem pergunta para os comentários")
    if not re.search(NEXT, end): erros.append("final não leva ao próximo vídeo/playlist")
    longcap = [s["caption"] for s in sc if len(s["caption"].split()) > 5]
    if longcap: avisos.append(f"legendas com mais de 5 palavras: {longcap[:3]}")
    nch = sum(1 for s in sc if s.get("chapter"))
    if nch < mins / 2.5: avisos.append(f"só {nch} capítulos para {mins:.0f} min (quero 1 a cada 2-3 min)")
    print(f"{'FALHOU' if erros else 'OK'}  {d['id']}  {mins:.1f} min  {t}")
    for e in erros: print("   ERRO:", e)
    for a in avisos: print("   aviso:", a)
    return not erros


if __name__ == "__main__":
    ok = all([check(p) for p in sys.argv[1:]])
    sys.exit(0 if ok else 1)
