#!/usr/bin/env python3
import json, sys
from pathlib import Path

def main():
    root = Path(__file__).resolve().parents[1]
    pkg = json.loads((root / 'package.json').read_text(encoding='utf-8'))
    problems = []
    oc = pkg.get('openclaw', {})
    for key in ('extensions','setupEntry'):
        vals = oc.get(key, []) if key == 'extensions' else [oc.get(key)]
        for rel in vals:
            if rel and not (root / rel).exists():
                problems.append(f'{key}: declared path missing: {rel}')
    manifest = root / 'openclaw.plugin.json'
    if not manifest.exists():
        problems.append('openclaw.plugin.json missing')
    if problems:
        print('PLUGIN-SURFACE-AUDIT: FAIL')
        print('\n'.join(problems))
        return 1
    print('PLUGIN-SURFACE-AUDIT: PASS')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
