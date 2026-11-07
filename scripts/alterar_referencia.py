#!/usr/bin/env python3
"""Gera uma versão LEVEMENTE ALTERADA de um áudio de referência (para usar
como amostra em ferramentas de clonagem/design de voz), aplicando os
parâmetros de `voice-profile.json` -> alvo_alterado.

Uso:
    pip install praat-parselmouth numpy
    python scripts/alterar_referencia.py entrada.mp3 saida.wav

Use somente com áudios cujo uso você tem direito (sua voz ou com autorização).
Requer ffmpeg no PATH para entradas que não sejam WAV.
"""
import json, os, subprocess, sys, tempfile
import parselmouth
from parselmouth.praat import call

AQUI = os.path.dirname(os.path.abspath(__file__))
perfil = json.load(open(os.path.join(AQUI, "..", "voice-profile.json"), encoding="utf-8"))
alvo = perfil["alvo_alterado"]

def main(entrada, saida):
    with tempfile.TemporaryDirectory() as tmp:
        wav = os.path.join(tmp, "in.wav")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", entrada, "-ac", "1", "-ar", "44100", wav], check=True)
        s = parselmouth.Sound(wav)
        # Change gender: formant shift ratio, nova mediana de F0, multiplicador de faixa, fator de duração
        ref = perfil["referencia_medida"]
        faixa = alvo["faixa_entonacao_semitons"] / ref["faixa_entonacao_semitons"]
        out = call(s, "Change gender", 65, 300,
                   alvo["deslocamento_formantes"],
                   alvo["f0_mediana_hz"],
                   faixa,
                   1 / alvo["velocidade_relativa"])
        out.scale_peak(0.95)
        out.save(saida, "WAV")
    print("Gerado:", saida)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
