"""
Stage 2: RESEARCH — Gather teaching resources for each session topic.

Reads parsed_curriculum.json and produces research_notes.md with:
- Platform URLs and tutorials
- Best practices for teaching each concept
- Common misconceptions
- Real-world examples relevant to the target audience

Usage:
    python stage2_research.py

Note: This script generates a research template organized by session/topic.
      Populate it with findings from web searches for each topic and SWBAT.
"""

import json
import sys
from pathlib import Path


OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def load_parsed_curriculum() -> list[dict]:
    """Load the parsed curriculum JSON from Stage 1."""
    path = OUTPUT_DIR / "parsed_curriculum.json"
    if not path.exists():
        print(f"ERROR: {path} not found. Run stage1_parse.py first.")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_research_template(sessions: list[dict]) -> str:
    """Build a markdown research-notes template organized by session."""
    lines = [
        "# Curriculum Research Notes",
        "",
        "> Auto-generated template. Fill in each section with web-search findings.",
        "> Search for each topic/SWBAT to find URLs, best practices,",
        "> misconceptions, and culturally relevant examples.",
        "",
    ]

    for session in sessions:
        num = session["session_number"]
        title = session["title"]
        lines.append(f"---")
        lines.append(f"## Session {num}: {title}")
        lines.append("")

        # SWBATs as research prompts
        if session["swbats"]:
            lines.append("### Learning Targets to Research")
            lines.append("")
            for i, swbat in enumerate(session["swbats"], 1):
                lines.append(f"#### SWBAT {i}: {swbat}")
                lines.append("")
                lines.append("**Platform URLs & Tutorials:**")
                lines.append("- [ ] _Search: relevant platform documentation_")
                lines.append("- [ ] _Search: beginner tutorials for this concept_")
                lines.append("")
                lines.append("**Best Practices for Teaching This Concept:**")
                lines.append("- ")
                lines.append("")
                lines.append("**Common Misconceptions:**")
                lines.append("- ")
                lines.append("")
                lines.append("**Real-World Examples (region/audience-relevant):**")
                lines.append("- ")
                lines.append("")

        # Activity topics
        if session["schedule_blocks"]:
            lines.append("### Activity-Specific Research")
            lines.append("")
            for block in session["schedule_blocks"]:
                name = block.get("activity_name", "Activity")
                lines.append(f"#### {name}")
                lines.append("")
                lines.append("**Relevant Resources:**")
                lines.append("- ")
                lines.append("")
                lines.append("**Worked Example Ideas:**")
                lines.append("- ")
                lines.append("")

        lines.append("")

    return "\n".join(lines)


def main():
    sessions = load_parsed_curriculum()
    md_content = generate_research_template(sessions)

    out_path = OUTPUT_DIR / "research_notes.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Research template generated for {len(sessions)} session(s).")
    print(f"Output: {out_path}")
    print()
    print("Next steps:")
    print("  1. For each topic/SWBAT, use web searches to find:")
    print("     - Platform URLs and tutorials (check regional availability)")
    print("     - Best practices for teaching that concept")
    print("     - Common misconceptions")
    print("     - Real-world examples for the target audience")
    print("  2. Fill in the template with your findings")
    print("  3. Run stage3_generate_lessons.py")


if __name__ == "__main__":
    main()
