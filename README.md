# RepoPulse

RepoPulse is a small, embeddable project-status widget powered by Git activity.

It gives visitors a quick view of what is happening with a project without
sending them to a separate GitHub page. The intended experience is closer to a
tiny Winamp or Spotify player than a development dashboard: compact, visual,
useful, and a little playful.

## The idea

A developer adds RepoPulse to a project page and gets a small status surface
showing information such as:

- the project name
- its current state
- the latest meaningful change
- when it was last updated
- the latest release, when available
- a link to the repository

RepoPulse is project-based. It is not intended to measure developer
productivity, rank contributors, or turn commit counts into a score.

## Example

```text
+------------------------------------+
| * SCHEMABIND              ACTIVE   |
|                                    |
| Improving CSV field handling       |
|                                    |
| v0.3.1               2 days ago    |
|                         View GitHub |
+------------------------------------+
```

The final embed should be similarly small:

```html
<repo-pulse
  repo="adamhx2/SchemaBind"
  theme="green">
</repo-pulse>

<script src="https://cdn.example.com/repo-pulse.js"></script>
```

The public embed API shown above is a design target and is not implemented yet.

## Themes

Version 1 is planned around four curated color options selected with simple
color swatches:

- green
- purple
- black
- white

These will be polished presets rather than a full color editor. Custom colors
and a theme builder can be considered after the core widget is stable.

## Proposed design

RepoPulse will keep project data separate from its presentation:

```text
GitHub or local Git
        |
RepoPulse generator
        |
pulse.json
        |
embeddable web component
```

The project owner controls the intentional status and message. Git supplies
supporting facts such as recent activity, update time, and release information.
This avoids pretending that commit frequency can reliably explain a project's
actual state.

The static JSON approach also keeps the widget lightweight:

- no visitor accounts
- no required RepoPulse backend
- no GitHub token exposed in the browser
- no GitHub API request for every page view
- compatible with static websites

## Initial scope

The first complete version should:

1. Read one public GitHub repository.
2. Combine repository activity with a small owner-controlled configuration.
3. Generate a portable `pulse.json` file.
4. Render one compact, responsive widget.
5. Offer the four curated color themes.
6. Link visitors back to the source repository.
7. Run automatically through GitHub Actions.

## Not in version 1

- productivity scores
- contributor rankings
- analytics dashboards
- activity graphs
- private repository support
- arbitrary color picking
- user accounts or a hosted control panel
- automatic claims that a project is abandoned or healthy

## Status

RepoPulse is currently in product definition and prototype planning. The
repository has been cleared of its early scaffold so the widget can be built
from a clean starting point.

See [ROADMAP.md](ROADMAP.md) for the planned build direction.

## Why build it?

People can always click through to GitHub. RepoPulse exists for the moments
when they should not have to.

A project page already has the visitor's attention. RepoPulse keeps the latest
movement in that context and gives the page a small sign of life.
