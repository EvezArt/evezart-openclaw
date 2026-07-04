#!/usr/bin/env python3
"""
EVEZ Tokenless Code Generator — Extra Generators Module
═══════════════════════════════════════════════════════════════════════

Zero-token generators for: FastAPI, React, SQL, Dockerfile, Docker Compose,
Pytest fixtures, Shell scripts, Config files, .gitignore, requirements.txt,
Express middleware.

All deterministic. All validated. Zero API calls.

by Steven Crawford-Maggard (EVEZ) — 2026
"""

from typing import List, Tuple, Optional


class ExtraGenerators:
    """Extra code generators for the EVEZ tokenless code generator."""

    # ─── FastAPI Route Generator ───────────────────────────────────────
    def gen_fastapi_route(self, entity: str, fields: str = "", methods: str = "all") -> str:
        """Generate a complete FastAPI CRUD router for an entity."""
        fields_list = []
        if fields:
            for f in fields.split(","):
                f = f.strip()
                if ":" in f:
                    name, typ = f.split(":", 1)
                    fields_list.append((name.strip(), typ.strip()))
                else:
                    fields_list.append((f.strip(), "str"))

        py_types = {"str": "str", "int": "int", "float": "float", "bool": "bool", "datetime": "datetime"}
        lines = [
            '"""Auto-generated FastAPI routes for {entity}."""'.format(entity=entity),
            "",
            "from datetime import datetime",
            "from typing import List, Optional",
            "from fastapi import APIRouter, HTTPException, status",
            "from pydantic import BaseModel, Field",
            "",
        ]

        # Model
        lines.append(f"class {entity}Base(BaseModel):")
        if not fields_list:
            fields_list = [("id", "str"), ("name", "str")]
        for fname, ftype in fields_list:
            pt = py_types.get(ftype, ftype)
            lines.append(f'    {fname}: {pt}')
        lines.append("")
        lines.append(f"class {entity}Create({entity}Base):")
        lines.append("    pass")
        lines.append("")
        lines.append(f"class {entity}Response({entity}Base):")
        lines.append("    id: str")
        lines.append("    created_at: datetime = Field(default_factory=datetime.now)")
        lines.append("")
        lines.append(f'router = APIRouter(prefix="/{entity.lower()}s", tags=["{entity}"])')
        lines.append("")
        lines.append("# In-memory store (replace with DB in production)")
        lines.append(f"_{entity.lower()}_store: dict[str, {entity}Response] = {{}}")
        lines.append("")

        all_methods = ["create", "read_all", "read_one", "update", "delete"]
        if methods != "all":
            all_methods = [m.strip() for m in methods.split(",")]

        if "create" in all_methods:
            lines.extend([
                f'@router.post("/", response_model={entity}Response, status_code=status.HTTP_201_CREATED)',
                f"async def create_{entity.lower()}(body: {entity}Create) -> {entity}Response:",
                f'    """Create a new {entity}."""',
                f'    import uuid',
                f'    record = {entity}Response(id=str(uuid.uuid4()), **body.model_dump())',
                f'    _{entity.lower()}_store[record.id] = record',
                f'    return record',
                "",
            ])

        if "read_all" in all_methods:
            lines.extend([
                f'@router.get("/", response_model=List[{entity}Response])',
                f"async def list_{entity.lower()}s() -> List[{entity}Response]:",
                f'    """List all {entity}s."""',
                f'    return list(_{entity.lower()}_store.values())',
                "",
            ])

        if "read_one" in all_methods:
            lines.extend([
                f'@router.get("/{{record_id}}", response_model={entity}Response)',
                f"async def get_{entity.lower()}(record_id: str) -> {entity}Response:",
                f'    """Get a single {entity} by ID."""',
                f'    record = _{entity.lower()}_store.get(record_id)',
                f'    if not record:',
                f'        raise HTTPException(status_code=404, detail="{entity} not found")',
                f'    return record',
                "",
            ])

        if "update" in all_methods:
            lines.extend([
                f'@router.put("/{{record_id}}", response_model={entity}Response)',
                f"async def update_{entity.lower()}(record_id: str, body: {entity}Create) -> {entity}Response:",
                f'    """Update a {entity}."""',
                f'    if record_id not in _{entity.lower()}_store:',
                f'        raise HTTPException(status_code=404, detail="{entity} not found")',
                f'    record = _{entity.lower()}_store[record_id]',
                f'    updated = record.model_copy(update=body.model_dump())',
                f'    _{entity.lower()}_store[record_id] = updated',
                f'    return updated',
                "",
            ])

        if "delete" in all_methods:
            lines.extend([
                f'@router.delete("/{{record_id}}", status_code=status.HTTP_204_NO_CONTENT)',
                f"async def delete_{entity.lower()}(record_id: str) -> None:",
                f'    """Delete a {entity}."""',
                f'    if record_id not in _{entity.lower()}_store:',
                f'        raise HTTPException(status_code=404, detail="{entity} not found")',
                f'    del _{entity.lower()}_store[record_id]',
                "",
            ])

        return "\n".join(lines)

    # ─── React Component Generator ─────────────────────────────────────
    def gen_react_component(self, name: str, props: str = "", hooks: str = "",
                            styled: bool = True, ts: bool = True) -> str:
        """Generate a React component (TS or JS, styled or plain)."""
        # Parse props — support both "name" and "name:type" syntax
        props_parsed = []  # list of (name, type)
        if props:
            for p in props.split(","):
                p = p.strip()
                if not p:
                    continue
                if ":" in p:
                    pname, ptype = p.split(":", 1)
                    props_parsed.append((pname.strip(), ptype.strip()))
                else:
                    props_parsed.append((p, "any"))
        props_names = [p[0] for p in props_parsed]
        hooks_list = [h.strip() for h in hooks.split(",") if h.strip()] if hooks else []

        lines = []
        if ts:
            if props_parsed:
                prop_str = "; ".join([f"{n}: {t}" for n, t in props_parsed])
                lines.append(f"interface {name}Props {{ {prop_str} }}")
                lines.append("")
                lines.append(f"export default function {name}({{ {', '.join(props_names)} }}: {name}Props) {{")
            else:
                lines.append(f"export default function {name}() {{")
        else:
            if props_names:
                lines.append(f"export default function {name}({{ {', '.join(props_names)} }}) {{")
            else:
                lines.append(f"export default function {name}() {{")


        # Hooks
        for h in hooks_list:
            if h == "state":
                lines.append("  const [data, setData] = useState(null);")
            elif h == "effect":
                lines.append("  useEffect(() => {")
                lines.append("    // Effect logic here")
                lines.append("  }, []);")
            elif h == "ref":
                lines.append("  const ref = useRef(null);")
            elif h == "memo":
                lines.append("  const memoized = useMemo(() => computeValue(), []);")
            elif h == "callback":
                lines.append("  const handler = useCallback(() => {")
                lines.append("    // Handler logic")
                lines.append("  }, []);")
            else:
                lines.append(f"  // {h}")

        if not hooks_list:
            lines.append("  // Component logic")

        # Return JSX
        lines.append("")
        lines.append("  return (")
        if styled:
            lines.append(f'    <div className="{name.lower()}-container">')
            lines.append(f"      <h2>{name}</h2>")
            for p in props_names:
                lines.append(f"      <p>{{{p}}}</p>")
            if not props_parsed:
                lines.append("      <p>Component rendered</p>")
            lines.append("    </div>")
        else:
            lines.append(f"    <div>")
            lines.append(f"      <h2>{name}</h2>")
            lines.append("    </div>")
        lines.append("  );")
        lines.append("}")

        # Imports at top
        imports = []
        if ts:
            imports.append("import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';")
        else:
            imports.append("import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';")
        lines = imports + [""] + lines

        return "\n".join(lines)

    # ─── SQL Schema Generator ──────────────────────────────────────────
    def gen_sql_schema(self, table: str, fields: str = "", db: str = "postgres") -> str:
        """Generate a SQL CREATE TABLE statement."""
        fields_list = []
        if fields:
            for f in fields.split(","):
                f = f.strip()
                if ":" in f:
                    name, typ = f.split(":", 1)
                    fields_list.append((name.strip(), typ.strip()))
                else:
                    fields_list.append((f.strip(), "str"))

        if not fields_list:
            fields_list = [("id", "int"), ("name", "str"), ("created_at", "datetime")]

        type_map = {
            "postgres": {"str": "VARCHAR(255)", "int": "INTEGER", "float": "REAL",
                         "bool": "BOOLEAN", "datetime": "TIMESTAMP", "text": "TEXT",
                         "uuid": "UUID", "json": "JSONB"},
            "mysql": {"str": "VARCHAR(255)", "int": "INT", "float": "FLOAT",
                      "bool": "TINYINT(1)", "datetime": "DATETIME", "text": "TEXT",
                      "uuid": "CHAR(36)", "json": "JSON"},
            "sqlite": {"str": "TEXT", "int": "INTEGER", "float": "REAL",
                       "bool": "INTEGER", "datetime": "TEXT", "text": "TEXT",
                       "uuid": "TEXT", "json": "TEXT"},
        }
        tm = type_map.get(db, type_map["postgres"])

        lines = [f"-- {table} schema for {db}", f"CREATE TABLE IF NOT EXISTS {table} ("]
        col_lines = []
        col_lines.append("  id SERIAL PRIMARY KEY" if db != "sqlite" else "  id INTEGER PRIMARY KEY AUTOINCREMENT")

        for fname, ftype in fields_list:
            sql_type = tm.get(ftype, tm.get("str", "VARCHAR(255)"))
            col_lines.append(f"  {fname} {sql_type}")

        col_lines.append(f'  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP')
        lines.append(",\n".join(col_lines))
        lines.append(");")
        lines.append("")
        lines.append(f"CREATE INDEX IF NOT EXISTS idx_{table}_created ON {table}(created_at);")

        return "\n".join(lines)

    # ─── Dockerfile Generator ──────────────────────────────────────────
    def gen_dockerfile(self, app_name: str, base: str = "python:3.12-slim",
                       port: int = 8000, entrypoint: str = "") -> str:
        """Generate a production Dockerfile."""
        is_python = "python" in base
        is_node = "node" in base

        lines = [f"# {app_name} — production Dockerfile", f"FROM {base}", ""]

        if is_python:
            lines.extend([
                "WORKDIR /app",
                "",
                "COPY requirements.txt .",
                "RUN pip install --no-cache-dir -r requirements.txt",
                "",
                "COPY . .",
                "",
                f"EXPOSE {port}",
                "",
                f'CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "{port}"]'
                if not entrypoint else f'CMD {entrypoint}',
            ])
        elif is_node:
            lines.extend([
                "WORKDIR /app",
                "",
                "COPY package*.json ./",
                "RUN npm ci --production",
                "",
                "COPY . .",
                "",
                f"EXPOSE {port}",
                "",
                f'CMD ["node", "server.js"]' if not entrypoint else f'CMD {entrypoint}',
            ])
        else:
            lines.extend([
                "WORKDIR /app",
                "COPY . .",
                f"EXPOSE {port}",
                f'CMD {entrypoint}' if entrypoint else 'CMD ["./app"]',
            ])

        return "\n".join(lines)

    # ─── Docker Compose Generator ──────────────────────────────────────
    def gen_docker_compose(self, services: str, app_name: str = "app") -> str:
        """Generate a docker-compose.yml."""
        svc_list = [s.strip() for s in services.split(",") if s.strip()]
        if not svc_list:
            svc_list = ["web", "db", "redis"]

        lines = ["version: '3.8'", ""]
        lines.append("services:")

        for svc in svc_list:
            if svc in ("web", "api", "app"):
                lines.extend([
                    f"  {svc}:",
                    f"    build: .",
                    f"    ports:",
                    f'      - "8000:8000"',
                    f"    environment:",
                    f"      - DATABASE_URL=postgresql://user:pass@db:5432/{app_name}",
                    f"      - REDIS_URL=redis://redis:6379",
                    f"    depends_on:",
                    f"      - db",
                    f"      - redis",
                    "",
                ])
            elif svc in ("db", "postgres", "postgres_db"):
                lines.extend([
                    "  db:",
                    "    image: postgres:16-alpine",
                    "    environment:",
                    '      POSTGRES_USER: user',
                    '      POSTGRES_PASSWORD: pass',
                    f'      POSTGRES_DB: {app_name}',
                    "    volumes:",
                    "      - db_data:/var/lib/postgresql/data",
                    "    ports:",
                    '      - "5432:5432"',
                    "",
                ])
            elif svc == "redis":
                lines.extend([
                    "  redis:",
                    "    image: redis:7-alpine",
                    "    ports:",
                    '      - "6379:6379"',
                    "",
                ])

        lines.append("volumes:")
        lines.append("  db_data:")

        return "\n".join(lines)

    # ─── Pytest Fixture Generator ──────────────────────────────────────
    def gen_pytest_fixture(self, name: str, fixture_type: str = "data",
                           scope: str = "function") -> str:
        """Generate a pytest fixture."""
        lines = [
            "import pytest",
            "",
        ]

        if fixture_type == "data":
            lines.extend([
                f"@pytest.fixture(scope=\"{scope}\")",
                f"def {name}():",
                f'    """Test fixture: {name}."""',
                f"    return {{",
                f'        "id": "test-001",',
                f'        "name": "Test Item",',
                f'        "value": 42,',
                f"    }}",
            ])
        elif fixture_type == "mock":
            lines.extend([
                f"@pytest.fixture(scope=\"{scope}\")",
                f"def {name}(mocker):",
                f'    """Mock fixture: {name}."""',
                f'    mock = mocker.MagicMock()',
                f'    mock.get_value.return_value = 42',
                f'    return mock',
            ])
        elif fixture_type == "client":
            lines.extend([
                "from fastapi.testclient import TestClient",
                "",
                f"@pytest.fixture(scope=\"{scope}\")",
                f"def {name}():",
                f'    """Test client fixture."""',
                f"    from main import app",
                f"    return TestClient(app)",
            ])
        elif fixture_type == "db":
            lines.extend([
                "import pytest",
                "",
                f"@pytest.fixture(scope=\"{scope}\")",
                f"def {name}():",
                f'    """Database fixture: {name}."""',
                f"    # Replace with your DB setup",
                f"    db = {{}}",
                f"    yield db",
                f"    db.clear()",
            ])
        else:
            lines.extend([
                f"@pytest.fixture(scope=\"{scope}\")",
                f"def {name}():",
                f'    """Fixture: {name}."""',
                f"    return None",
            ])

        return "\n".join(lines)

    # ─── Shell Script Generator ────────────────────────────────────────
    def gen_shell_script(self, name: str, commands: str = "", include_trap: bool = True) -> str:
        """Generate a bash shell script with error handling."""
        lines = [
            f"#!/usr/bin/env bash",
            f"# {name}.sh — generated by EVEZ tokenless code generator",
            f"set -euo pipefail",
            "",
        ]

        if include_trap:
            lines.extend([
                "# Error handler",
                "on_error() {",
                f'    echo "[ERROR] {name} failed at line $LINENO" >&2',
                "    exit 1",
                "}",
                "trap on_error ERR",
                "",
            ])

        cmd_list = [c.strip() for c in commands.split(",")] if commands else []
        if not cmd_list:
            cmd_list = ["echo 'Starting...'", "echo 'Done!'"]

        lines.append(f"# Main")
        for cmd in cmd_list:
            lines.append(cmd)
        lines.append("")
        lines.append(f'echo "[{name}] Complete"')

        return "\n".join(lines)

    # ─── Config File Generator ─────────────────────────────────────────
    def gen_config(self, app_name: str, fmt: str = "yaml", keys: str = "") -> str:
        """Generate a config file (YAML, JSON, TOML)."""
        key_list = [k.strip() for k in keys.split(",")] if keys else ["host", "port", "debug", "database_url"]

        if fmt == "yaml":
            lines = [f"# {app_name} configuration"]
            lines.append(f"app:")
            lines.append(f"  name: {app_name}")
            for k in key_list:
                if k == "port":
                    lines.append(f"  {k}: 8000")
                elif k == "debug":
                    lines.append(f"  {k}: false")
                elif k == "host":
                    lines.append(f'  {k}: "0.0.0.0"')
                elif "database" in k or "url" in k:
                    lines.append(f'  {k}: "postgresql://user:pass@localhost:5432/{app_name}"')
                else:
                    lines.append(f'  {k}: ""')
            lines.append("")
            lines.append("logging:")
            lines.append("  level: info")
            return "\n".join(lines)

        elif fmt == "json":
            import json
            config = {"app": {"name": app_name}}
            for k in key_list:
                if k == "port":
                    config["app"][k] = 8000
                elif k == "debug":
                    config["app"][k] = False
                elif "url" in k or "database" in k:
                    config["app"][k] = f"postgresql://user:pass@localhost:5432/{app_name}"
                else:
                    config["app"][k] = ""
            config["logging"] = {"level": "info"}
            return json.dumps(config, indent=2)

        elif fmt == "toml":
            lines = [f'[app]', f'name = "{app_name}"']
            for k in key_list:
                if k == "port":
                    lines.append(f'{k} = 8000')
                elif k == "debug":
                    lines.append(f'{k} = false')
                else:
                    lines.append(f'{k} = ""')
            lines.append("")
            lines.append('[logging]')
            lines.append('level = "info"')
            return "\n".join(lines)

        return f"# Unknown format: {fmt}"

    # ─── .gitignore Generator ──────────────────────────────────────────
    def gen_gitignore(self, project_type: str = "python") -> str:
        """Generate a .gitignore file for a project type."""
        common = [
            "# OS", ".DS_Store", "Thumbs.db", "",
            "# IDEs", ".idea/", ".vscode/", "*.swp", "*.swo", "",
            "# Env", ".env", ".env.*", "!env.example", "",
        ]

        templates = {
            "python": common + [
                "# Python", "__pycache__/", "*.py[cod]", "*.so",
                "dist/", "build/", "*.egg-info/", ".eggs/",
                "venv/", ".venv/", "env/", "",
                "# Testing", ".pytest_cache/", ".coverage", "htmlcov/",
                "*.cover", ".tox/", "",
                "# Type checking", ".mypy_cache/", ".pyre/", "",
            ],
            "node": common + [
                "# Node", "node_modules/", "dist/", "build/",
                ".next/", ".nuxt/", ".cache/", "*.log",
                "npm-debug.log*", "yarn-debug.log*", "yarn-error.log*",
                ".pnpm-store/", "",
            ],
            "rust": common + [
                "# Rust", "target/", "**/*.rs.bk", "Cargo.lock",
                "",
            ],
            "go": common + [
                "# Go", "*.exe", "*.exe~", "*.dll", "*.so", "*.dylib",
                "*.test", "*.out", "vendor/", "",
            ],
            "java": common + [
                "# Java", "*.class", "*.jar", "*.war",
                "target/", ".gradle/", "build/", "",
            ],
        }

        lines = templates.get(project_type, templates["python"])
        lines.append("# Generated by EVEZ tokenless code generator")
        return "\n".join(lines)

    # ─── requirements.txt Generator ────────────────────────────────────
    def gen_requirements(self, libs: str = "", include_dev: bool = False) -> str:
        """Generate a requirements.txt file."""
        lib_list = [l.strip() for l in libs.split(",") if l.strip()] if libs else []

        # Common pinned versions
        versions = {
            "fastapi": "fastapi>=0.115.0",
            "uvicorn": "uvicorn[standard]>=0.30.0",
            "pydantic": "pydantic>=2.0.0",
            "sqlalchemy": "SQLAlchemy>=2.0.0",
            "alembic": "alembic>=1.13.0",
            "redis": "redis>=5.0.0",
            "celery": "celery>=5.4.0",
            "pytest": "pytest>=8.0.0",
            "httpx": "httpx>=0.27.0",
            "requests": "requests>=2.32.0",
            "aiohttp": "aiohttp>=3.10.0",
            "numpy": "numpy>=2.0.0",
            "pandas": "pandas>=2.2.0",
            "scipy": "scipy>=1.14.0",
            "scikit-learn": "scikit-learn>=1.5.0",
            "openai": "openai>=1.40.0",
            "anthropic": "anthropic>=0.34.0",
            "langchain": "langchain>=0.2.0",
            "transformers": "transformers>=4.44.0",
            "torch": "torch>=2.4.0",
        }

        lines = ["# requirements.txt — generated by EVEZ tokenless code generator", ""]

        if not lib_list:
            lib_list = ["fastapi", "uvicorn", "pydantic", "httpx"]

        for lib in lib_list:
            lines.append(versions.get(lib, lib))

        if include_dev:
            lines.extend(["", "# Development", "pytest>=8.0.0", "pytest-asyncio>=0.23.0",
                          "pytest-cov>=5.0.0", "mypy>=1.11.0", "ruff>=0.6.0"])

        return "\n".join(lines)

    # ─── Express Middleware Generator ──────────────────────────────────
    def gen_middleware(self, name: str, framework: str = "express", ts: bool = True) -> str:
        """Generate an Express/Fastify middleware."""
        if ts:
            lines = [
                f"import {{ Request, Response, NextFunction }} from 'express';",
                "",
                f"export function {name}(req: Request, res: Response, next: NextFunction): void {{",
                f"  // {name} middleware",
                f"  console.log(`[${name}] ${{req.method}} ${{req.path}}`);",
                f"  next();",
                f"}}",
                "",
                f"// Usage: app.use({name});",
            ]
        else:
            lines = [
                f"function {name}(req, res, next) {{",
                f"  // {name} middleware",
                f"  console.log(`[{name}] ${{req.method}} ${{req.path}}`);",
                f"  next();",
                f"}}",
                "",
                f"// Usage: app.use({name});",
            ]

        if framework == "fastify" and ts:
            lines = [
                f"import {{ FastifyRequest, FastifyReply }} from 'fastify';",
                "",
                f"export async function {name}(req: FastifyRequest, reply: FastifyReply) {{",
                f"  // {name} middleware",
                f"  req.log.info(`[{name}] ${{req.method}} ${{req.url}}`);",
                f"}}",
                "",
                f"// Usage: fastify.addHook('onRequest', {name});",
            ]

        return "\n".join(lines)
