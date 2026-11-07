# Como gerar a voz em cada plataforma

Todos os valores derivam de `../voice-profile.json`. Ajuste fino: se ficar
grave demais, suba o tom 1 passo; se ficar rápido, reduza a velocidade.

## ElevenLabs — Voice Design
- **Prompt:** use a versão em inglês da seção 2 de `VOZ.md`.
- Gênero: Male · Idade: Middle aged · Sotaque: Brazilian Portuguese.
- Ao gerar narração (modelo multilíngue v2/v3):
  - Stability **0.55** · Similarity **0.75** · Style **0.20** · Speaker boost **on** · Speed **0.95**.
- Alternativa (Instant Voice Clone): gere uma referência alterada com
  `scripts/alterar_referencia.py` a partir de um áudio que você tem direito de usar.

## OpenAI TTS (`gpt-4o-mini-tts`)
- `voice`: **onyx** (alternativa: `ash`) · `speed`: 0.95
- `instructions`:
```
Fale em português brasileiro com sotaque neutro de narrador. Voz masculina
grave e encorpada, timbre escuro e aveludado. Ritmo calmo, pausas curtas e
confiantes, finais de frase descendentes. Tom de contador de histórias
curioso e levemente irônico. Ênfase descendo o tom, nunca gritando.
```

## Microsoft Azure Speech (SSML)
Vozes masculinas pt-BR recomendadas: `pt-BR-AntonioNeural` (padrão),
`pt-BR-JulioNeural`, `pt-BR-ValerioNeural`.
```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="pt-BR">
  <voice name="pt-BR-AntonioNeural">
    <prosody pitch="-10%" rate="-5%" contour="(0%,+0%) (100%,-8%)">
      Você sabia que a expressão <emphasis level="moderate">puxar o saco</emphasis>
      nasceu dentro dos quartéis?
      <break time="800ms"/>
      E a origem é mais curiosa do que parece.
    </prosody>
  </voice>
</speak>
```

## Google Cloud Text-to-Speech
- Voz: `pt-BR-Neural2-B` (ou `pt-BR-Wavenet-B`)
- `audioConfig`: `{"pitch": -4.0, "speakingRate": 0.95, "effectsProfileId": ["headphone-class-device"]}`
- SSML: mesmas regras de `<break>` e `<emphasis>` do exemplo Azure.

## Edge-TTS (grátis, linha de comando)
```bash
pip install edge-tts
edge-tts --voice pt-BR-AntonioNeural --pitch=-12Hz --rate=-5% \
  --file roteiro.txt --write-media narracao.mp3
```

## Modelos abertos (XTTS-v2, F5-TTS, Fish Speech, etc.)
Precisam de um áudio de referência (6–30 s, limpo, sem música). Gere um
alterado com `scripts/alterar_referencia.py` e use os parâmetros:
temperatura ≈0.65, velocidade 0.95, idioma `pt`.
