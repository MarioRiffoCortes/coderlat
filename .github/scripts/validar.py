"""Valida frontmatter de artículos de coderLAT. Uso: validar.py archivo.md ..."""
import re, sys, datetime, pathlib
import yaml

REQUIRED = ["title", "date", "author"]
TAXONOMIAS = ["tool", "resource", "country"]
SLUG = re.compile(r"^[a-z0-9][a-z0-9\-]*$")
MAX_IMG = 1024 * 1024
errores = []

def err(f, m): errores.append(f"{f}: {m}")

for f in sys.argv[1:]:
    p = pathlib.Path(f)
    txt = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m:
        err(f, "falta el encabezado (frontmatter) entre '---'"); continue
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        err(f, f"YAML inválido: {e}"); continue
    for k in REQUIRED:
        if not fm.get(k): err(f, f"falta '{k}'")
    d = fm.get("date")
    if d and not isinstance(d, datetime.datetime):
        try: datetime.datetime.strptime(str(d), "%d-%m-%Y %H:%M")
        except ValueError: err(f, "'date' debe tener formato dd-mm-aaaa hh:mm")
    tax = fm.get("taxonomy") or {}
    for t in TAXONOMIAS:
        vals = tax.get(t)
        if not vals: err(f, f"falta taxonomy.{t}"); continue
        for v in (vals if isinstance(vals, list) else [vals]):
            if not SLUG.match(str(v)):
                err(f, f"taxonomy.{t}: '{v}' debe ir en minúsculas, sin tildes ni espacios")
    if not p.parent.name or not SLUG.match(p.parent.name):
        err(f, f"la carpeta '{p.parent.name}' debe ser un slug en minúsculas con guiones")
    if len(txt.split("---", 2)[-1].strip()) < 200:
        err(f, "el artículo es demasiado corto (mínimo ~200 caracteres)")
    for img in p.parent.glob("*"):
        if img.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"} and img.stat().st_size > MAX_IMG:
            err(str(img), "imagen mayor a 1 MB")

if errores:
    print("\n".join(errores)); sys.exit(1)
print("OK: contenido válido")
