// SPDX-FileCopyrightText: 2026 Erida Contributors
//
// SPDX-License-Identifier: AGPL-3.0-or-later

using Content.Shared._EinsteinEngines.Language;
using Content.Shared._EinsteinEngines.Language.Events;
using Robust.Shared.GameStates;
using Robust.Shared.Prototypes;

namespace Content.Shared._Erida.Language;

// erida edit
[RegisterComponent, NetworkedComponent]
public sealed partial class LanguageOnSpawnComponent : Component
{
    [DataField(required: true)]
    public List<ProtoId<LanguagePrototype>> Languages = [];

    [DataField]
    public bool UnderstoodOnly;
}

// erida edit
public sealed partial class LanguageOnSpawnSystem : EntitySystem
{
    public override void Initialize()
    {
        base.Initialize();

        SubscribeLocalEvent<LanguageOnSpawnComponent, DetermineEntityLanguagesEvent>(OnDetermineLanguages);
    }

    private void OnDetermineLanguages(Entity<LanguageOnSpawnComponent> ent, ref DetermineEntityLanguagesEvent args)
    {
        args.UnderstoodLanguages.UnionWith(ent.Comp.Languages);

        if (!ent.Comp.UnderstoodOnly)
            args.SpokenLanguages.UnionWith(ent.Comp.Languages);
    }
}
