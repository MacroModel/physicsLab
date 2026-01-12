#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from getpass import getpass
from pathlib import Path
from typing import Any, Optional


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


ENV_HELP = """Environment variables (optional):
  PL_TOKEN       Token for token login
  PL_AUTH_CODE   AuthCode for token login
  PL_EMAIL       Email for email login
  PL_PASSWORD    Password for email login (discouraged; prefer prompt)
"""


def _read_text_file(path: str) -> str:
    return Path(path).expanduser().read_text(encoding="utf-8").strip()


def _read_intro(args: argparse.Namespace) -> str:
    if getattr(args, "intro", None):
        return str(args.intro).strip()
    if getattr(args, "intro_file", None):
        return _read_text_file(str(args.intro_file))
    raise SystemExit("Missing introduction: pass --intro or --intro-file.")


def _load_sav_json(path: str) -> dict[str, Any]:
    sav_path = Path(path).expanduser()
    try:
        raw = sav_path.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        raise SystemExit(f"SAV file not found: {sav_path}") from e

    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise SystemExit(f"Invalid .sav JSON: {sav_path} ({e})") from e


def _sav_summary_info(sav: dict[str, Any]) -> dict[str, Any]:
    summary = sav.get("Summary") or {}
    return {
        "ID": summary.get("ID"),
        "Subject": summary.get("Subject"),
        "Category": summary.get("Category"),
        "Type": summary.get("Type"),
        "Image": summary.get("Image"),
        "Language": summary.get("Language"),
    }


def _print_inspect(sav_path: str) -> None:
    sav = _load_sav_json(sav_path)
    info = _sav_summary_info(sav)
    print(f"SAV: {Path(sav_path).expanduser().resolve()}")
    for k in ["ID", "Subject", "Category", "Type", "Image", "Language"]:
        print(f"{k}: {info.get(k)}")
    print(f"Published: {bool(info.get('ID'))}")


def _add_auth_args(parser: argparse.ArgumentParser) -> None:
    auth = parser.add_argument_group("authentication")
    auth_mode = auth.add_mutually_exclusive_group()
    auth_mode.add_argument(
        "--token",
        default=os.getenv("PL_TOKEN"),
        help="Token login token (or env PL_TOKEN). Requires --auth-code / PL_AUTH_CODE.",
    )
    auth_mode.add_argument(
        "--email",
        default=os.getenv("PL_EMAIL"),
        help="Email login email (or env PL_EMAIL).",
    )
    auth.add_argument(
        "--auth-code",
        default=os.getenv("PL_AUTH_CODE"),
        help="Token login auth code (or env PL_AUTH_CODE).",
    )
    auth.add_argument(
        "--password",
        default=os.getenv("PL_PASSWORD"),
        help="Email login password (or env PL_PASSWORD). Prefer leaving empty to prompt.",
    )
    auth.add_argument(
        "--no-prompt",
        action="store_true",
        help="Fail instead of prompting for missing password.",
    )


def _login(args: argparse.Namespace):
    from physicsLab import web  # noqa: PLC0415

    if args.token:
        if not args.auth_code:
            raise SystemExit("Missing --auth-code (or PL_AUTH_CODE) for token login.")
        return web.token_login(token=args.token, auth_code=args.auth_code)

    if not args.email:
        raise SystemExit(
            "Missing credentials: use --token/--auth-code or set --email (or PL_EMAIL)."
        )
    password: Optional[str] = args.password
    if password is None:
        if args.no_prompt:
            raise SystemExit(
                "Missing password: pass --password, set PL_PASSWORD, or omit --no-prompt to enter interactively."
            )
        password = getpass("Physics-Lab password: ")
    return web.email_login(args.email, password)


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="upload_experiment.py",
        description="Publish/update a Physics-Lab experiment (.sav) via physicsLab WebAPI.",
        epilog=ENV_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    inspect_p = sub.add_parser(
        "inspect", help="Print basic metadata from a local .sav file."
    )
    inspect_p.add_argument(
        "--sav",
        default=str(_repo_root() / "riscv_pe_to_pl.sav"),
        help="Path to the .sav file.",
    )

    publish_p = sub.add_parser("publish", help="Publish a new (unpublished) .sav.")
    publish_p.add_argument(
        "--sav",
        default=str(_repo_root() / "riscv_pe_to_pl.sav"),
        help="Path to the .sav file.",
    )
    publish_p.add_argument("--title", required=True, help="Experiment title.")
    intro_g = publish_p.add_mutually_exclusive_group(required=True)
    intro_g.add_argument("--intro", help="Experiment introduction text.")
    intro_g.add_argument(
        "--intro-file",
        help="Path to a UTF-8 text file used as the introduction.",
    )
    publish_p.add_argument(
        "--category",
        choices=["experiment", "discussion"],
        default="experiment",
        help="Publish to Experiment or Discussion area.",
    )
    publish_p.add_argument("--image", default=None, help="Optional cover image path.")
    publish_p.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate inputs and print what would be uploaded without calling the WebAPI.",
    )
    _add_auth_args(publish_p)

    update_p = sub.add_parser("update", help="Update an already published .sav.")
    update_p.add_argument("--sav", required=True, help="Path to the .sav file.")
    intro_g2 = update_p.add_mutually_exclusive_group(required=False)
    intro_g2.add_argument("--intro", help="New introduction text (optional).")
    intro_g2.add_argument("--intro-file", help="Path to new introduction text.")
    update_p.add_argument("--title", default=None, help="New title (optional).")
    update_p.add_argument("--image", default=None, help="Optional new cover image path.")
    update_p.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate inputs and print what would be uploaded without calling the WebAPI.",
    )
    _add_auth_args(update_p)

    defaults_p = sub.add_parser(
        "publish-rv32i",
        help="Convenience preset: publish ./riscv_pe_to_pl.sav with RV32I title and docs/rv32i_intro.md.",
    )
    defaults_p.add_argument(
        "--sav",
        default=str(_repo_root() / "riscv_pe_to_pl.sav"),
        help="Path to the .sav file.",
    )
    defaults_p.add_argument(
        "--intro-file",
        default=str(_repo_root() / "docs" / "rv32i_intro.md"),
        help="Path to the introduction text file.",
    )
    defaults_p.add_argument(
        "--category",
        choices=["experiment", "discussion"],
        default="experiment",
        help="Publish to Experiment or Discussion area.",
    )
    defaults_p.add_argument("--image", default=None, help="Optional cover image path.")
    defaults_p.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate inputs and print what would be uploaded without calling the WebAPI.",
    )
    _add_auth_args(defaults_p)

    return parser.parse_args(argv)


def main() -> int:
    repo_root = _repo_root()
    sys.path.insert(0, str(repo_root))

    from physicsLab import Category, Experiment, OpenMode  # noqa: PLC0415

    args = _parse_args(sys.argv[1:])

    if args.command == "inspect":
        _print_inspect(args.sav)
        return 0

    if args.command in ("publish", "publish-rv32i"):
        sav_info = _sav_summary_info(_load_sav_json(args.sav))
        if sav_info.get("ID") is not None:
            raise SystemExit(
                "This .sav already looks published (Summary.ID is set). Use `update` instead."
            )

        title = "RV32I" if args.command == "publish-rv32i" else args.title
        intro = _read_intro(
            argparse.Namespace(
                intro=None if args.command == "publish-rv32i" else args.intro,
                intro_file=args.intro_file,
            )
        )
        category = {
            "experiment": Category.Experiment,
            "discussion": Category.Discussion,
        }[args.category]

        if args.dry_run:
            print("Dry run (no network requests).")
            _print_inspect(args.sav)
            print(f"Will publish as: title={title!r}, category={category.name}, image={args.image!r}")
            print(f"Intro chars: {len(intro)}")
            return 0

        user = _login(args)
        with Experiment(OpenMode.load_by_filepath, args.sav) as expe:
            expe.edit_publish_info(title=title, introduction=intro)
            expe.upload(user, category, args.image)
        print("Publish done.")
        return 0

    if args.command == "update":
        sav_info = _sav_summary_info(_load_sav_json(args.sav))
        if sav_info.get("ID") is None:
            raise SystemExit(
                "This .sav looks unpublished (Summary.ID is None). Use `publish` instead."
            )

        intro = _read_intro(args) if (args.intro or args.intro_file) else None

        if args.dry_run:
            print("Dry run (no network requests).")
            _print_inspect(args.sav)
            print(f"Will update: title={args.title!r}, image={args.image!r}, intro_chars={len(intro) if intro else None}")
            return 0

        user = _login(args)
        with Experiment(OpenMode.load_by_filepath, args.sav) as expe:
            if args.title is not None or intro is not None:
                expe.edit_publish_info(title=args.title, introduction=intro, wx=False)
            expe.update(user, args.image)
        print("Update done.")
        return 0

    raise SystemExit(f"Unknown command: {args.command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
