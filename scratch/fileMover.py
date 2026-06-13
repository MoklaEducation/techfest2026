#!/usr/bin/env python3

import argparse
import shutil
from pathlib import Path

import platform


def main():
    parser = argparse.ArgumentParser(
        description="Generate copy operations and markdown links for problem IDs."
    )

    parser.add_argument(
        "-i",
        "--input",
        default="problem.txt",
        help="Input file containing problem IDs (default: problem.txt)",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="links.txt",
        help="Output links file (default: links.txt)",
    )

    parser.add_argument(
        "--src-template",
        default="D:\\repo\\mokla\\StepIntoTech2026\\judge\\problems\\{problemId}",
        help="Source directory template (default: source/{problemId})",
    )

    parser.add_argument(
        "--dst-template",
        default="D:\\repo\\mokla\\techfest2026\\codequest\\{problemId}",
        help="Destination directory template (default: destination/{problemId})",
    )

    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually perform the recursive copies. Otherwise just print commands.",
    )
    
    args = parser.parse_args()

    input_file = Path(args.input)
    output_file = Path(args.output)

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    links = []

    with input_file.open("r", encoding="utf-8") as f:
        problem_ids = [line.strip() for line in f if line.strip()]

    for problem_id in problem_ids:
        src = Path(args.src_template.format(problemId=problem_id))
        dst = Path(args.dst_template.format(problemId=problem_id))

        if platform.system() == "Windows":
          copy_cmd = f'robocopy "{src}" "{dst}" /E'
        else:
          copy_cmd = f'cp -r "{src}" "{dst}"'

        print(copy_cmd)

        if args.execute:
            if not src.exists():
                print(f"WARNING: Source does not exist: {src}")
            else:
                shutil.copytree(src, dst, dirs_exist_ok=True)

        links.append(
            f"[Test cases available here!]"
            f"(https://github.com/MoklaEducation/techfest2026/tree/main/codequest/{problem_id})"
        )

    output_file.write_text("\n".join(links) + "\n", encoding="utf-8")

    print(f"\nGenerated {len(links)} links in {output_file}")


if __name__ == "__main__":
    main()