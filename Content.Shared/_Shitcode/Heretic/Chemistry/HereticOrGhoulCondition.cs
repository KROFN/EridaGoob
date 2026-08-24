// SPDX-License-Identifier: AGPL-3.0-or-later

using Content.Shared.EntityConditions;
using Content.Shared.Heretic;
using Content.Shared.Mind;
using Content.Shared.Roles;
using JetBrains.Annotations;
using Robust.Shared.Prototypes;

namespace Content.Shared._Shitcode.Heretic.Chemistry;

/// <summary>
///     Passes for minds with the heretic role and ghouls.
/// </summary>
public sealed partial class HereticOrGhoulConditionSystem : EntityConditionSystem<MetaDataComponent, HereticOrGhoulCondition>
{
    [Dependency] private readonly SharedMindSystem _mind = default!;
    [Dependency] private readonly SharedRoleSystem _role = default!;
    [Dependency] private readonly EntityManager _ent = default!;

    protected override void Condition(Entity<MetaDataComponent> ent, ref EntityConditionEvent<HereticOrGhoulCondition> args)
    {
        var result = _ent.HasComponent<GhoulComponent>(ent.Owner);

        if (!result && _mind.TryGetMind(ent.Owner, out var mindId, out _))
        {
            result = (_role.MindIsAntagonist(mindId) && _ent.HasComponent<HereticComponent>(mindId))
                || _ent.HasComponent<GhoulComponent>(mindId);
        }

        args.Result = result;
    }
}

/// <inheritdoc cref="HereticOrGhoulConditionSystem"/>
[UsedImplicitly]
public sealed partial class HereticOrGhoulCondition : EntityConditionBase<HereticOrGhoulCondition>
{
    /// <summary>
    /// Guidebook text
    /// </summary>
    [DataField]
    public LocId? GuidebookComponentName;

    public override string EntityConditionGuidebookText(IPrototypeManager prototype)
    {
        if (GuidebookComponentName == null)
            return string.Empty;

        return Loc.GetString("reagent-effect-condition-guidebook-has-component",
            ("comp", Loc.GetString(GuidebookComponentName)),
            ("invert", Inverted));
    }
}
