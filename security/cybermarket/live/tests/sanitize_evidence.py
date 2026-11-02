"""Redact credentials and fixture values while retaining test failure diagnostics."""

import hashlib
import re
from pathlib import Path

root = Path("technical-results")
patterns = [
    (r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+", "[REDACTED_JWT]"),
    (r"(?i)[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", "[REDACTED_EMAIL]"),
    (r"CM (?:Billing|Shipping) Sentinel", "[SYNTHETIC_ADDRESS]"),
    (
        r"(?s)-----BEGIN (?:RSA )?PRIVATE KEY-----.*?-----END (?:RSA )?PRIVATE KEY-----",
        "[REDACTED_PRIVATE_KEY]",
    ),
]
for path in root.glob("*.xml"):
    content = path.read_text()
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    path.write_text(content)
checksums = [
    f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}"
    for path in sorted(root.iterdir())
    if path.is_file() and path.name != "SHA256SUMS"
]
(root / "SHA256SUMS").write_text("\n".join(checksums) + "\n")
