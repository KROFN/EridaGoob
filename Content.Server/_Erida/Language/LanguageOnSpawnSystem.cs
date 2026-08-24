// SPDX-FileCopyrightText: 2026 Erida Contributors
//
// SPDX-License-Identifier: AGPL-3.0-or-later

using Content.Server._EinsteinEngines.Language;
using Content.Shared._EinsteinEngines.Language.Components;
using Content.Shared._Erida.Language;
using Robust.Shared.Player;

namespace Content.Server._Erida.Language;

// erida edit
public sealed partial class LanguageOnSpawnInitSystem : EntitySystem
{
    [Dependency] private LanguageSystem _language = default!;

    public override void Initialize()
    {
        base.Initialize();

        SubscribeLocalEvent<LanguageOnSpawnComponent, MapInitEvent>(OnMapInit);
        SubscribeLocalEvent<LanguageOnSpawnComponent, ComponentShutdown>(OnShutdown);
    }

    private void OnMapInit(Entity<LanguageOnSpawnComponent> ent, ref MapInitEvent args)
    {
        UpdateLanguages(ent);
    }

    private void OnShutdown(Entity<LanguageOnSpawnComponent> ent, ref ComponentShutdown args)
    {
        UpdateLanguages(ent);
    }

    private void UpdateLanguages(Entity<LanguageOnSpawnComponent> ent)
    {
        if (!TryComp<LanguageSpeakerComponent>(ent, out var speaker))
            return;

        _language.UpdateEntityLanguages((ent, speaker));
    }
}
