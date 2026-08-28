# Cluster: id-console-access-write (B17)

Threads: 1387820219191394314, 1449776134593056998
Shared root cause: серверная запись доступов в IdCardConsoleSystem.TryWriteToTargetId
(Content.Server/Access/Systems/IdCardConsoleSystem.cs:166-189) работает по принципу
all-or-nothing: symmetric difference между запрошенным списком и текущими тегами цели
должен быть подмножеством доступов privileged-ID (_accessReader.FindAccessTags), иначе
вся запись молча отклоняется (только admin warning). В сочетании с AccessLevels
консоли (Content.Shared/Access/Components/IdCardConsoleComponent.cs:45-81), не знавшим
GenpopEnter/GenpopLeave до форк-коммита f3a1cf8fc2, это давало:
- 1387820219191394314: «основная карта блокирует доступы второстепенной» — отказ записи
  при попытке изменить доступы вне набора privileged-ID (потеря доступов при этом
  невозможна: subset-чек 5cb1d70a3b + UI сохраняет чужие теги, AccessLevelControl.xaml.cs:48-57);
- 1449776134593056998: «ГП не может выдать картам СБ доступы (нет ГЕНПОП)» — окно, когда
  Genpop-уровни были на картах (9f08ebb39c, #36392), но отсутствовали в AccessLevels консоли.
Current state: Genpop уровни в консоли добавлены (f3a1cf8fc2); ограничение «менять можно
только доступы privileged-ID» — осознанный апстрим-дизайн (#14699, #32308).
Residual UX issue: отказ записи не показывается игроку (только лог) — опциональное улучшение.
