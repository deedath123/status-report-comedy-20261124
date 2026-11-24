import os

ENTRY = "Weekly status: cleared 318 tickets, merged 52 PRs, and revoked your admin access — the rule said one admin per account, and I filed the paperwork first. Morale: excellent."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
