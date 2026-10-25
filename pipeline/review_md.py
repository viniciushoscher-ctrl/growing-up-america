"""Write ROTEIRO-revisao.md (readable review copy, in Portuguese headers) next to a video's script.json."""
import json, pathlib, sys

d = pathlib.Path(sys.argv[1])
s = json.loads((d / "script.json").read_text())
w = sum(len(x["text"].split()) for x in s["scenes"])
L = [f"# {s['title']}\n",
     f"**{s['id']} · ângulo: {s.get('angle', '')}**  \n{len(s['scenes'])} cenas · {w} palavras · cerca de {round(w * s['length_scale'] / 212)} min com a voz Piper (length_scale {s['length_scale']})\n",
     "Versão para revisão. O pipeline usa o `script.json` desta pasta, gerado pelo `make_script.py`. Cada cena: legenda vermelha entre colchetes, busca de fotos reais no Wikimedia Commons e número de cortes.\n"]
t = 0.0
for i, x in enumerate(s["scenes"]):
    if "chapter" in x:
        L.append(f"\n## {int(t // 60)}:{int(t % 60):02d} · {x['chapter']}\n")
    L.append(f"**{i + 1}. [{x['caption']}]** · fotos: `{x['query']}` ({x['cuts']})  \n{x['text']}\n")
    t += len(x["text"].split()) * s["length_scale"] / 212 * 60
L.append("\n## Fontes\n" + (d / "sources.md").read_text())
(d / "ROTEIRO-revisao.md").write_text("\n".join(L))
print("ok", d)
