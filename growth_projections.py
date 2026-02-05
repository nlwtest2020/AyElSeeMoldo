import pandas as pd
import numpy as np

"""
Growth Projections for MOD and GEO
Starting: March 1, 2026

Key assumptions:
- MOD current pace: $305K in 7 months = $43,571/month (exceptional, not sustainable)
- MOD historical 5-year average: ~$22,000/month
- Set ambitious targets that aim to RETAIN most of the gains while growing
- GEO uses historical baseline with growth targets
"""

# =============================================================================
# BASELINE DATA
# =============================================================================

# MOD: Current exceptional performance
MOD_CURRENT_MONTHLY = 43571  # $305K / 7 months
MOD_HISTORICAL_AVG = 22000   # Approximate 5-year average monthly

# GEO: Historical baseline
GEO_BASELINE_MONTHLY = 3229  # Based on 5-year weighted average

# =============================================================================
# PROJECTION MODEL - GOAL-ORIENTED TARGETS
# =============================================================================

def calculate_mod_target(months_out, current=MOD_CURRENT_MONTHLY,
                         historical=MOD_HISTORICAL_AVG):
    """
    MOD targets that acknowledge the hot streak but set ambitious retention goals.

    Philosophy: They're on a run - the goal is to RETAIN as much as possible
    through deliberate effort, not just accept passive regression.

    Conservative floor: 70% of current pace (~$30,500/month)
    Target: Maintain 85% of current pace and grow 5% annually from there
    """
    # Sustainable floor (what we'd expect with passive regression)
    floor = current * 0.70  # ~$30,500

    # Target baseline: aim to retain 85% of current exceptional performance
    target_baseline = current * 0.85  # ~$37,035

    # Annual growth target: 5% (ambitious but achievable with intentional effort)
    monthly_growth = (1.05 ** (1/12)) - 1  # ~0.41% monthly

    return target_baseline * ((1 + monthly_growth) ** months_out)


def calculate_geo_target(months_out, baseline=GEO_BASELINE_MONTHLY):
    """
    GEO targets with ambitious growth.
    Target: 10% annual growth (aggressive for smaller center building momentum)
    """
    monthly_growth_rate = (1.10 ** (1/12)) - 1  # ~0.80% monthly
    return baseline * ((1 + monthly_growth_rate) ** months_out)


# =============================================================================
# GENERATE PROJECTIONS
# =============================================================================

print("=" * 75)
print("REVENUE GROWTH TARGETS")
print("Starting: March 1, 2026")
print("=" * 75)

print("\n" + "=" * 75)
print("CONTEXT & STRATEGY")
print("=" * 75)

MOD_TARGET_BASELINE = MOD_CURRENT_MONTHLY * 0.85
MOD_FLOOR = MOD_CURRENT_MONTHLY * 0.70

print(f"""
MOD Current Performance:
  - FY25-26 to date: $305,000 in 7 months
  - Current monthly average: ${MOD_CURRENT_MONTHLY:,.0f}
  - Annualized pace: ${MOD_CURRENT_MONTHLY * 12:,.0f} (record-breaking)
  - This is {MOD_CURRENT_MONTHLY/MOD_HISTORICAL_AVG:.1f}x historical average (~${MOD_HISTORICAL_AVG:,.0f}/month)

MOD Target Strategy:
  - Current pace is exceptional - likely includes favorable timing/one-time factors
  - Goal: RETAIN as much momentum as possible through intentional effort
  - Target baseline: 85% of current pace = ${MOD_TARGET_BASELINE:,.0f}/month
  - Conservative floor: 70% of current = ${MOD_FLOOR:,.0f}/month
  - Growth target: 5% annually from target baseline

GEO Target Strategy:
  - Current baseline: ${GEO_BASELINE_MONTHLY:,.0f}/month (5-year weighted average)
  - Smaller center = higher growth potential
  - Growth target: 10% annually (aggressive but achievable)
""")

# Milestones
milestones = [
    (6, "September 1, 2026"),
    (12, "March 1, 2027"),
    (18, "September 1, 2027"),
    (24, "March 1, 2028"),
]

print("=" * 75)
print("MOD TARGETS (Retain Momentum + 5% Annual Growth)")
print("=" * 75)
print(f"\n{'Milestone':<25} {'Monthly Target':>15} {'Annual Target':>15} {'vs Current':>12}")
print("-" * 70)

print(f"{'Current pace':<25} ${MOD_CURRENT_MONTHLY:>13,.0f} ${MOD_CURRENT_MONTHLY*12:>13,.0f} {'--':>12}")
print(f"{'Target baseline (85%)':<25} ${MOD_TARGET_BASELINE:>13,.0f} ${MOD_TARGET_BASELINE*12:>13,.0f} {'-15.0%':>12}")

for months, date_label in milestones:
    target = calculate_mod_target(months)
    annual = target * 12
    vs_current = (target / MOD_CURRENT_MONTHLY - 1) * 100
    print(f"{date_label:<25} ${target:>13,.0f} ${annual:>13,.0f} {vs_current:>+11.1f}%")

print("\n" + "=" * 75)
print("GEO TARGETS (10% Annual Growth)")
print("=" * 75)
print(f"\n{'Milestone':<25} {'Monthly Target':>15} {'Annual Target':>15} {'vs Baseline':>12}")
print("-" * 70)

print(f"{'Current baseline':<25} ${GEO_BASELINE_MONTHLY:>13,.0f} ${GEO_BASELINE_MONTHLY*12:>13,.0f} {'--':>12}")

for months, date_label in milestones:
    target = calculate_geo_target(months)
    annual = target * 12
    vs_baseline = (target / GEO_BASELINE_MONTHLY - 1) * 100
    print(f"{date_label:<25} ${target:>13,.0f} ${annual:>13,.0f} {vs_baseline:>+11.1f}%")

print("\n" + "=" * 75)
print("COMBINED TARGETS")
print("=" * 75)
print(f"\n{'Milestone':<25} {'Monthly':>12} {'Quarterly':>14} {'Annual':>14}")
print("-" * 70)

combined_current = MOD_CURRENT_MONTHLY + GEO_BASELINE_MONTHLY
combined_target_baseline = MOD_TARGET_BASELINE + GEO_BASELINE_MONTHLY
print(f"{'Current pace':<25} ${combined_current:>10,.0f} ${combined_current*3:>12,.0f} ${combined_current*12:>12,.0f}")
print(f"{'Target baseline':<25} ${combined_target_baseline:>10,.0f} ${combined_target_baseline*3:>12,.0f} ${combined_target_baseline*12:>12,.0f}")

for months, date_label in milestones:
    mod_target = calculate_mod_target(months)
    geo_target = calculate_geo_target(months)
    combined = mod_target + geo_target
    print(f"{date_label:<25} ${combined:>10,.0f} ${combined*3:>12,.0f} ${combined*12:>12,.0f}")

print("\n" + "=" * 75)
print("SUMMARY: TARGET REVENUE BY MILESTONE")
print("=" * 75)
print(f"""
                          MOD            GEO         COMBINED
                     Monthly/Annual  Monthly/Annual  Monthly/Annual
Current pace:        ${MOD_CURRENT_MONTHLY:>6,.0f} / ${MOD_CURRENT_MONTHLY*12/1000:>5.0f}K   ${GEO_BASELINE_MONTHLY:>5,.0f} / ${GEO_BASELINE_MONTHLY*12/1000:>5.1f}K    ${combined_current:>6,.0f} / ${combined_current*12/1000:>5.0f}K
Target baseline:     ${MOD_TARGET_BASELINE:>6,.0f} / ${MOD_TARGET_BASELINE*12/1000:>5.0f}K   ${GEO_BASELINE_MONTHLY:>5,.0f} / ${GEO_BASELINE_MONTHLY*12/1000:>5.1f}K    ${combined_target_baseline:>6,.0f} / ${combined_target_baseline*12/1000:>5.0f}K
""")

targets = []
for months, date_label in milestones:
    mod_target = calculate_mod_target(months)
    geo_target = calculate_geo_target(months)
    combined = mod_target + geo_target
    targets.append({
        'milestone': date_label,
        'months': months,
        'mod_monthly': mod_target,
        'geo_monthly': geo_target,
        'combined_monthly': combined,
    })
    short_label = f"{months} months:"
    print(f"{short_label:<15} ${mod_target:>6,.0f} / ${mod_target*12/1000:>5.0f}K   ${geo_target:>5,.0f} / ${geo_target*12/1000:>5.1f}K    ${combined:>6,.0f} / ${combined*12/1000:>5.0f}K")

final_mod = calculate_mod_target(24)
final_geo = calculate_geo_target(24)
final_combined = final_mod + final_geo

print("\n" + "=" * 75)
print("KEY INSIGHTS")
print("=" * 75)
print(f"""
1. MOD Strategy - Retain the Momentum:
   - Current pace ${MOD_CURRENT_MONTHLY:,.0f}/month is {MOD_CURRENT_MONTHLY/MOD_HISTORICAL_AVG:.1f}x historical average
   - Target: retain 85% of current pace as new baseline (${MOD_TARGET_BASELINE:,.0f}/month)
   - Then grow 5% annually from that elevated baseline
   - 24-month target: ${final_mod:,.0f}/month (${final_mod*12:,.0f}/year)

2. GEO Strategy - Accelerate Growth:
   - Smaller base creates opportunity for higher % growth
   - Target: 10% annual growth from ${GEO_BASELINE_MONTHLY:,.0f}/month baseline
   - 24-month target: ${final_geo:,.0f}/month (${final_geo*12:,.0f}/year)
   - Focus: replicate successful MOD strategies at smaller scale

3. Combined Portfolio Targets:
   - Current pace: ${combined_current:,.0f}/month (${combined_current*12:,.0f}/year)
   - Target baseline: ${combined_target_baseline:,.0f}/month (${combined_target_baseline*12:,.0f}/year)
   - 24-month target: ${final_combined:,.0f}/month (${final_combined*12:,.0f}/year)
   - Net growth vs target baseline: {((final_combined)/combined_target_baseline - 1)*100:+.1f}%

4. What "Ambitious but Achievable" Means:
   - MOD: Accept ~15% pullback from exceptional pace, then grow from there
   - GEO: Push for 10% annual growth (aggressive but realistic for smaller center)
   - Combined: Targets represent real growth from sustainable baseline

5. Tracking Success:
   - GREEN: Hit or exceed monthly targets
   - YELLOW: Within 10% of target
   - RED: More than 10% below target for 2+ consecutive months
""")

# Export targets to CSV for reference
df_targets = pd.DataFrame(targets)
df_targets.to_csv("growth_targets.csv", index=False)
print("\nTargets exported to: growth_targets.csv")
