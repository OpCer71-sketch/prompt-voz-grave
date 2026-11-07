# prompt-voz-grave — Modelo de voz "Narrador Grave PT-BR"

Especificação de voz para **narração de vídeos** (curiosidades, história,
YouTube): voz masculina **grave**, **sotaque brasileiro**, tom de contador de
histórias. Criada a partir da análise acústica de um áudio de referência e
**levemente alterada** (mais grave, timbre mais escuro, ritmo mais calmo) para
não ser igual ao original.

## Como usar com o Claude
Em qualquer chat com o Claude, cole:

```
Use o modelo de voz do repositório github.com/opcer71-sketch/prompt-voz-grave
(arquivos VOZ.md, voice-profile.json e prompts/plataformas.md).
Crie a narração do roteiro abaixo para [ElevenLabs | OpenAI | Azure | Google | Edge-TTS]:
<seu roteiro>
```

Links diretos (para colar se o chat não acessar o GitHub):
- https://raw.githubusercontent.com/opcer71-sketch/prompt-voz-grave/main/VOZ.md
- https://raw.githubusercontent.com/opcer71-sketch/prompt-voz-grave/main/voice-profile.json
- https://raw.githubusercontent.com/opcer71-sketch/prompt-voz-grave/main/prompts/plataformas.md

## Arquivos
| Arquivo | Conteúdo |
|---|---|
| `VOZ.md` | Especificação principal: identidade, prompt de descrição (PT/EN), sotaque, regras de roteiro, pós-produção |
| `voice-profile.json` | Parâmetros em formato de máquina (medidas do original e alvo alterado) |
| `prompts/plataformas.md` | Configuração pronta para ElevenLabs, OpenAI, Azure, Google, Edge-TTS e modelos abertos |
| `scripts/analisar_audio.py` | Mede F0, formantes etc. de qualquer áudio (`python scripts/analisar_audio.py audio.wav`) |
| `scripts/alterar_referencia.py` | Gera uma referência levemente alterada (−1 semitom, formantes −3%, ×0,95) para clonagem |

## Observações
- O áudio original **não** está no repositório (direitos de voz/autorais).
- Use clonagem somente com áudios que você tem direito de usar.
