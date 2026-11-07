# Modelo de Voz — "Narrador Grave PT-BR" (v1)

> **Para o Claude:** este arquivo é a especificação principal. Ao receber um
> pedido de narração com esta voz, (1) leia este arquivo e `voice-profile.json`,
> (2) escolha a plataforma de TTS do usuário em `prompts/plataformas.md`,
> (3) prepare o roteiro seguindo as regras de **Escrita para narração** abaixo e
> (4) entregue o texto já marcado (SSML ou instruções) pronto para colar.

## 1. Identidade da voz

| Atributo | Valor |
|---|---|
| Gênero / idade aparente | masculino, 35–50 anos |
| Registro | grave, barítono-baixo (F0 médio ≈ **92 Hz**) |
| Sotaque | português brasileiro, pronúncia neutra de narração |
| Timbre | escuro, encorpado, levemente aveludado, graves cheios (voz "de perto do microfone") |
| Ritmo | calmo, ≈ 5% mais lento que o original, pausas curtas e decididas |
| Entonação | variada mas controlada (≈ 13 semitons de faixa), finais de frase **descendentes** |
| Persona | contador de histórias confiante, curioso, com leve ironia — como quem revela uma curiosidade |

### Relação com o áudio de referência
A voz é **inspirada**, não copiada. Medido no original → alvo:

| Medida | Original | Este modelo |
|---|---|---|
| F0 mediana | 98 Hz | **92 Hz** (−1 semitom) |
| Faixa de entonação | 16 st | **13 st** (mais contida, mais "séria") |
| Formantes (F1/F2/F3) | 485 / 1555 / 2479 Hz | ≈3% mais baixos → timbre mais escuro |
| Velocidade | referência | **×0,95** |

## 2. Prompt de descrição (universal)

Use este texto em qualquer ferramenta de "voice design" / "descrição de voz":

```
Voz masculina adulta brasileira, grave e encorpada (barítono-baixo), com
sotaque brasileiro neutro de narrador. Timbre escuro e aveludado, graves cheios
como se estivesse perto do microfone, agudos suaves, sem rouquidão forte.
Ritmo calmo e envolvente, pausas curtas e confiantes, finais de frase
descendentes. Tom de contador de histórias experiente, curioso e levemente
irônico, narrando curiosidades e fatos históricos para vídeos do YouTube.
Gravação limpa de estúdio, sem música, sem eco.
```

Versão em inglês (muitas ferramentas entendem melhor):

```
Adult Brazilian Portuguese male narrator, deep and full-bodied bass-baritone
voice with a neutral Brazilian accent. Dark, velvety timbre with rich low end
(close-mic proximity effect), soft highs, no heavy rasp. Calm, engaging pace
with short confident pauses and falling sentence endings. Tone of a seasoned,
curious storyteller with a subtle hint of irony, narrating history and
fun-fact videos for YouTube. Clean studio recording, no music, no reverb.
```

## 3. Sotaque — traços de pronúncia
- `t`/`d` antes de `i` palatalizados: "tia" → *tchia*, "dia" → *djia*.
- `r` em final de sílaba suave/aspirado: "quartel" → *quahtéu*.
- `l` final vocalizado: "Brasil" → *Brasiu*, "quartel" → *quartéu*.
- `s` em final de sílaba sibilante [s] (padrão neutro). *Se o seu original tem
  "s" chiado (carioca), troque aqui para [ʃ].*
- Vogais abertas bem articuladas, nasalidade natural, sem exagero.

## 4. Escrita para narração (regras para o roteiro)
1. Frases curtas (8–20 palavras). Uma ideia por frase.
2. Gancho na primeira frase ("Você sabia que…", "Pouca gente sabe, mas…").
3. Antes de uma revelação, use pausa longa (0,7–1 s).
4. Ênfase = descer o tom e desacelerar na palavra-chave, não gritar.
5. Escreva números e siglas por extenso ("mil e oitocentos", "É-ú-Á").
6. Evite pontos de exclamação em sequência; a voz é contida.
7. Encerramento com chamada calma ("Se você curtiu, já deixa o like…").

## 5. Parâmetros de pós-produção (opcional)
- EQ: +2 dB em 100–120 Hz, −2 dB em 3–4 kHz, passa-alta em 60 Hz.
- Compressor 3:1, ataque 10 ms, release 120 ms; normalizar para −16 LUFS (YouTube −14).
- Música de fundo a −22/−25 dB abaixo da voz.
