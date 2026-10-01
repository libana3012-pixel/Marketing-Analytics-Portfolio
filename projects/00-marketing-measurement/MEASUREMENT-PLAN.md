# Measurement plan | fictional website
**Design specification, not deployed tracking**

| Proposed event | Trigger, subject to website design | What it helps explain |
| --- | --- | --- |
| `view_opening_hours` | Opens opening-hours information | Practical visit intent |
| `view_directions` | Clicks the directions link | Interest in visiting |
| `view_ticket_info` | Opens ticket-information page | Ticket research, not sale |
| `select_event` | Opens an event page | Topic interest |
| `select_shop` | Follows the shop link | Shop interest, not revenue |

Before implementing: verify the interaction exists, review consent/privacy, configure and preview tags, confirm event payloads in DebugView, test duplicate firing and document definitions.

Use consistent UTM naming such as `utm_source=instagram&utm_medium=social&utm_campaign=spring_exhibition`. Do not conflate Search Console clicks with GA4 sessions. Never present a zero recorded event as proof that no visitor took action.
