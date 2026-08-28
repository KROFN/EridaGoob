# Cluster: tts-volume-mute — «TTS нельзя отключить» (2 треда)

## Треды
- 1480519345594568866 (2026-03-09, тег «Серьёзный») — оба ползунка на нуле, слышны голоса и оповещения. ПЕРВИЧНЫЙ.
- 1421848934644449382 (2025-09-28) — при «полностью отключённом» TTS «немного слышно».

## Подтверждённый общий корень (код)
1. FILE: Content.Client/_CorvaxGoob/TTS/TTSSystem.cs
   SYMBOL: MinimalVolume = -10f (строка 45); AdjustVolume (133–143)
   Факт: громкость любого TTS = `MinimalVolume + SharedAudioSystem.GainToVolume(_volume)` — постоянная база -10 дБ; никакого «hard mute» в пайплайне нет.
2. FILE: Content.Client/_CorvaxGoob/TTS/TTSSystem.Announcements.cs
   SYMBOL: PlayTTS (строка 29)
   Факт: оповещения = `(AdjustVolume(false) + GainToVolume(_announcementsVolume)) / 2` — усреднение каналов, обнуление одного ползунка не исключает звук.
3. FILE: Content.Client/Options/UI/Tabs/AudioTab.xaml.cs (строки 29–84) и Content.Client/_CorvaxGoob/TTS/TTSTab.xaml
   Факт: привязок к CCVars.TTSVolume ("tts.volume") в найденных UI-файлах НЕТ; TTSTab — только выбор голоса. Ползунки, которые игроки считают TTS, управляют соседними системами (VoiceChat — отдельная Goob-система) [INFER].
4. FILE: Content.Shared/_Erida/CCVar/CCVars.TTS.cs
   Факт: CCVars.TTSVolume ("tts.volume", 0f, CLIENTONLY) и CCVars.AnnouncementsSound ("audio.announcements_volume", 0.5f) — единственные клиентские регуляторы, подписаны в TTSSystem.Initialize (строки 59–60) [SRC].
   Нюанс: семантика GainToVolume/clamp громкости в RobustToolbox локально не верифицируема (RobustToolbox отсутствует в дереве репо) [?].

## Причинная цепочка
Игрок обнуляет «TTS-ползунки» в настройках → фактический tts.volume не изменяется (нет UI-привязки) либо остаётся >0 → PlayTTSEvent/TTSAnnouncedEvent всё равно воспроизводятся → формула с базой -10 дБ и усреднением даёт слышимый, а не нулевой результат → «TTS слышен при полном отключении».

## Предлагаемое лечение (общее, НЕ реализовывать)
- TTSSystem.OnPlayTTS / PlayTTS: early return при нулевой громкости канала (детерминированный mute).
- AudioTab: добавить ползунки, привязанные к CCVars.TTSVolume и CCVars.AnnouncementsSound, 0 = mute.

## Смежные, НЕ входящие в кластер
- tts-voice-availability: 1365367741560913970 (подписные голоса), 1414388215669981324 (рандомный голос), 1421828766404972624 (Рита) — другая тема (выбор/доступность голосов), объединены только в отдельном хинте кластера, не здесь.
