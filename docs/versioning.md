# Versioning

Luz follows [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`).

## When each number bumps

| Change | Type | Example |
|---|---|---|
| Bug fix, no new syntax | PATCH | `1.15.0 → 1.15.1` |
| New feature, built-in, or stdlib module | MINOR | `1.15.0 → 1.16.0` |
| Syntax change that breaks existing code | MAJOR | `1.x.x → 2.0.0` |

**Key rule:** if someone has `.luz` code written today and it fails after an update, that update must be a MAJOR. If the update fixes a bug — PATCH. If it only adds things — MINOR.

## Release flow

Releases are organized around **GitHub Milestones**. Each milestone groups related issues under a target version (e.g., `v1.16.0 – Methods Update`).

```
develop  ──●──●──●──────●──●──●──────●─→
             feat      feat          feat
master   ──────────────●────────────────●─→
                     v1.16.0         v1.17.0
```

1. A milestone is created with a name and target version (e.g., `v1.16.0 – Methods Update`).
2. Related issues are assigned to that milestone.
3. Work happens on `develop` (or `feature/*` branches that merge into `develop`).
4. When all milestone issues are closed → merge `develop` into `master` → tag `vX.Y.Z` → GitHub Release.
5. The milestone is then closed.

**Hotfixes** go directly to `master`, get a PATCH bump, and are tagged immediately — no milestone needed.

## When to open a new milestone

A good milestone has **2–4 related issues** that together represent a coherent improvement. Avoid:

- Single-issue milestones (use a PATCH or just a PR instead).
- Milestones with 10+ issues (they never close and block releases).

## Branch strategy

| Branch | Purpose |
|---|---|
| `master` | Stable, released code. Every commit here is a tag. |
| `develop` | Integration branch. Features merge here first. |
| `feature/*` | Short-lived branches for individual issues. |

## Current version

The current stable release is always the latest tag on `master`. Check the [releases page](https://github.com/Elabsurdo984/luz-lang/releases) for the full changelog.
