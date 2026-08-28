# Cluster: tts-voice-availability

## Members

- 1365367741560913970 — ТТС и кол-во персонажей (CONFIRMED_CURRENT_BUG/Medium)
- 1414388215669981324 — Рандомный ттс каждый раунд (CANNOT_VERIFY/Low)
- 1421828766404972624 — ТТС рита (CONFIG_OR_CONTENT_ISSUE/Medium)

## Common symptom (from individual dossiers)

- 1365367741560913970: Патронских («подписочных») TTS-голосов и лимита персонажей не существует: TTSTab.UpdateResults показывает все ttsVoice без гейтинга (Disabled=false), CanHaveVoice проверяет только пол; подтверждено ответом разработчика «не успели сделать».
- 1414388215669981324: Механика «рандомный TTS каждый раунд» не локализована: серверный fallback в ServerDbBase детерминирован (DefaultSexVoice), серверный код выдачи голоса в репо не найден; тело треда пустое, скриншоты не интерпретированы.
- 1421828766404972624: Голос «Рита» отсутствует в Resources/Prototypes/_Erida/Voice/tts-voices.yml (выбранное подмножество после переработки Tts #28/#9), пикер TTSTab показывает только ttsVoice-прототипы; спец-голос медборгов — заявленное намерение («ТТС бывает специализированный»).

## Root cause notes

Shared mechanism per member dossiers; where mechanisms diverge the cluster marks a failure FAMILY (same subsystem, distinct causes) rather than a single fix.

## Recommended action

Single fix only where dossiers confirm one root cause; otherwise coordinate fixes per member dossier's Proposed fix section to avoid duplicate investigation.

## Validation matrix

| Thread | Check | Expected |
|---|---|---|
| 1365367741560913970 | re-verify per dossier Validation plan | see dossier |
| 1414388215669981324 | re-verify per dossier Validation plan | see dossier |
| 1421828766404972624 | re-verify per dossier Validation plan | see dossier |
