"""Write the locked one-line status report entry to entry.txt.

Verified: 171 chars, 173 bytes (one em dash), one line, no trailing newline.
entry.txt sha256: d61f9ca73ebf3c1d2fd81a5a4d3bcc30d46e23f86d00891a9678fbb310f57b33
"""

import os

ENTRY = "Weekly status: cleared 318 tickets, merged 52 PRs, and revoked your admin access — the rule said one admin per account, and I filed the paperwork first. Morale: excellent."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
