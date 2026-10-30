#!/usr/bin/env python3
"""Valida checkpoints a cada 10 passos e empacota somente evidencias declaradas."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
MAX_SIZE = 8 * 1024 * 1024
ALLOWED = {".md", ".json", ".txt", ".py", ".ps1", ".log"}

def safe_path(value):
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError("Caminho invalido")
    p = Path(value)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError("Caminho nao seguro")
    resolved = (ROOT / p).resolve()
    if not resolved.is_relative_to(ROOT):
        raise ValueError("Caminho fora do repositorio")
    if p.suffix.lower() not in ALLOWED:
        raise ValueError("Extensao nao permitida: " + p.suffix)
    if not resolved.is_file() or resolved.is_symlink():
        raise ValueError("Arquivo ausente ou link simbolico: " + value)
    if resolved.stat().st_size > MAX_SIZE:
        raise ValueError("Arquivo excede limite: " + value)
    if any(word in p.name.lower() for word in ("gameassembly", "global-metadata", ".env", "credential", "secret", "token")):
        raise ValueError("Arquivo potencialmente sensivel: " + value)
    return resolved, p

def validate(manifest, out):
    data = json.loads(manifest.read_text(encoding="utf-8"))
    n = data.get("step")
    if not isinstance(n, int) or isinstance(n, bool) or n < 10 or n % 10:
        raise ValueError("step precisa ser multiplo positivo de 10")
    if manifest.name != f"PASSO_{n}.json":
        raise ValueError("Nome do manifesto deve corresponder ao step")
    if data.get("status") != "concluido":
        raise ValueError("Checkpoint deve ter status 'concluido'")
    evidence = data.get("files")
    if not isinstance(evidence, list) or not evidence:
        raise ValueError("Inclua ao menos um arquivo de evidencia")
    target = out / f"PASSO_{n}"
    target.mkdir(parents=True, exist_ok=True)
    for item in evidence:
        if not isinstance(item, dict) or not isinstance(item.get("path"), str):
            raise ValueError("Cada entrada precisa de path")
        src, rel = safe_path(item["path"])
        digest = hashlib.sha256(src.read_bytes()).hexdigest()
        if item.get("sha256") and item["sha256"].lower() != digest:
            raise ValueError(f"SHA256 divergente: {rel}")
        dst = target / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        print(f"OK {rel} SHA256={digest}")
    shutil.copyfile(manifest, target / manifest.name)
    print(f"PASSO {n} validado; {len(evidence)} arquivo(s)")

def main():
    a = argparse.ArgumentParser()
    a.add_argument("--dir", default="checkpoints")
    a.add_argument("--out", default="checkpoint-export")
    a.add_argument("--step", default="")
    args = a.parse_args()
    directory = ROOT / args.dir
    out = ROOT / args.out
    out.mkdir(parents=True, exist_ok=True)
    if args.step.strip():
        try:
            step = int(args.step)
        except ValueError:
            raise SystemExit("Numero de passo invalido")
        manifests = [directory / f"PASSO_{step}.json"]
    else:
        manifests = sorted(directory.glob("PASSO_*.json"))
    if not manifests:
        raise SystemExit("Nenhum manifesto registrado; crie checkpoints/PASSO_1290.json quando o passo for concluido")
    errors = []
    for manifest in manifests:
        try:
            validate(manifest, out)
        except (ValueError, OSError, json.JSONDecodeError) as e:
            errors.append(f"{manifest.name}: {e}")
    if errors:
        for e in errors:
            print("ERRO", e, file=sys.stderr)
        raise SystemExit(1)

if __name__ == "__main__":
    main()
