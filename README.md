# ruralstar-ops-dashboard
Operational dashboard for RuralStar incidents extracted from WhatsApp communications
# RuralStar Ops Dashboard

## Context
RuralStar sites are monitored operationally through daily BO RAN analysis and real-time incident communications exchanged in WhatsApp groups. While effective for coordination, WhatsApp-based incident handling lacks structure, history, and objective visibility.

## Problem Statement
NOC engineers rely on unstructured WhatsApp messages to assess network status, identify impacted rural sites, and produce daily operational reports. This makes it difficult to obtain a clear, objective, and historical view of network incidents and availability.

## Proposed Solution
This project delivers an operational dashboard for NOC engineers that consolidates RuralStar network status from WhatsApp incident communications and BO RAN daily analysis. Using a deterministic NLP-based parser, the system extracts incident lifecycle events, affected rural sites and far-ends, and maintains a day-by-day operational history.

The dashboard provides a daily operational view (up to J-1), enables objective network status assessment, and supports root-cause analysis through structured incident data and exportable daily reports.

## Scope & Limitations
- Focused on RuralStar sites and their far-ends only
- Does not replace NMS tools
- No real-time KPI ingestion
- No predictive analytics
- No automatic root-cause analysis (only structured insights and recommendations)

## High-Level Architecture
WhatsApp Messages → NLP Incident Parser → Incident State Engine → Database → Dashboard & Daily Reports

## Expected Outputs
- Live and historical view of RuralStar incidents
- Daily operational dashboard (J-1)
- One-click exportable daily incident and availability report
