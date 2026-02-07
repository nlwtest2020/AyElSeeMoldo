# Multi-Agent Market Research System

A multi-agent system for conducting structured market research across countries and research pathways.

## Project Structure

```
├── config/
│   ├── countries.json            # Target countries and regions
│   ├── pathways.json             # Research pathways and workflows
│   └── research_parameters.json  # Agent and validation settings
├── agents/                       # Agent definitions and logic
├── data/
│   ├── raw/                      # Unprocessed collected data
│   ├── validated/                # Cross-referenced and validated data
│   └── final/                    # Analysis-ready output data
├── prompts/                      # Prompt templates for research agents
├── GEO.xlsx                      # Geographic reference data
└── Test Rev Expen.xlsx           # Revenue and expenditure test data
```

## Configuration

- **countries.json** — Defines target countries with region groupings and enable/disable flags.
- **pathways.json** — Defines research pathways (market sizing, competitive landscape, regulatory review, consumer insights) and their step sequences.
- **research_parameters.json** — Controls data sources, validation thresholds, output formats, and agent concurrency settings.

## Data Pipeline

1. **Raw** — Agents collect data from configured sources into `data/raw/`.
2. **Validated** — Data is cross-referenced against multiple sources and checked against confidence thresholds in `data/validated/`.
3. **Final** — Validated data is formatted for analysis and stored in `data/final/`.
