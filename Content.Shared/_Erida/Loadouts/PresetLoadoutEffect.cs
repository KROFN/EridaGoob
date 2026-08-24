// SPDX-License-Identifier: AGPL-3.0-or-later

using System.Diagnostics.CodeAnalysis;
using Content.Shared.Humanoid.Prototypes;
using Content.Shared.Preferences;
using Content.Shared.Preferences.Loadouts;
using Content.Shared.Preferences.Loadouts.Effects;
using Robust.Shared.Player;
using Robust.Shared.Prototypes;
using Robust.Shared.Utility;

namespace Content.Shared._Erida.Loadouts;

// erida edit
public sealed partial class PresetMarkerEffect : LoadoutEffect
{
    [DataField(required: true)]
    public string Preset = string.Empty;

    public override bool Validate(HumanoidCharacterProfile profile, RoleLoadout loadout, ICommonSession? session,
        IDependencyCollection collection, [NotNullWhen(false)] out FormattedMessage? reason)
    {
        reason = null;
        return true;
    }
}

// erida edit
public sealed partial class RequirePresetEffect : LoadoutEffect
{
    [DataField(required: true)]
    public ProtoId<LoadoutGroupPrototype> Group = default!;

    [DataField(required: true)]
    public string Preset = string.Empty;

    public override bool Validate(HumanoidCharacterProfile profile, RoleLoadout loadout, ICommonSession? session,
        IDependencyCollection collection, [NotNullWhen(false)] out FormattedMessage? reason)
    {
        var protoManager = collection.Resolve<IPrototypeManager>();

        var chosen = "custom";

        if (loadout.SelectedLoadouts.TryGetValue(Group, out var selected))
        {
            foreach (var item in selected)
            {
                if (!protoManager.TryIndex(item.Prototype, out var loadoutProto))
                    continue;

                foreach (var effect in loadoutProto.Effects)
                {
                    if (effect is PresetMarkerEffect marker)
                    {
                        chosen = marker.Preset;
                        break;
                    }
                }
            }
        }

        if (chosen == "custom" || chosen == Preset)
        {
            reason = null;
            return true;
        }

        reason = FormattedMessage.FromUnformatted(Loc.GetString("loadout-preset-locked"));
        return false;
    }
}
