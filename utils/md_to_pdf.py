#!/usr/bin/env python3
"""
Markdown to PDF Converter - A4 Pages with GitHub Styling

This utility converts Markdown documents to high-quality PDF files with
GitHub-style formatting, optimised for A4 page printing. It maintains proper
formatting, syntax highlighting for code blocks, and handles educational
content appropriately.

The converter uses WeasyPrint for superior PDF rendering and supports
GitHub-flavoured Markdown with tables, code blocks, and other educational
content formatting.

Usage:
    python src/tools/md_to_pdf_converte        help=('Convert all markdown files in the proj        help=('Convert all markdown fi        help=('Convert all markdown files in the project '
              '(searches docs/, samples/, and root)'))es in the project '
              '(searches docs/, samples/, and root)'))ct '
              '(searches docs/, samples/, and root)')).py [options]

Examples:
    # Convert all markdown files in docs/
    python src/tools/md_to_pdf_converter.py --all

    # Convert specific file
    python src/tools/md_to_pdf_converter.py --file docs/exercises/exercise.md

    # Convert with custom output directory
    python src/tools/md_to_pdf_converter.py --all --output-dir ./pdf_exports

    # Convert single file with verbose output
    python src/tools/md_to_pdf_converter.py --file README.md --verbose

Dependencies:
    - weasyprint: Professional PDF generation from HTML/CSS
    - markdown: Markdown parsing with extensions
    - pygments: Syntax highlighting for code blocks
    - beautifulsoup4: HTML processing and cleanup
"""

import sys
import argparse
import re
from pathlib import Path
from typing import List

# Attempt to import required dependencies with graceful failure
try:
    from weasyprint import HTML, CSS

    WEASYPRINT_AVAILABLE = True
except ImportError:
    WEASYPRINT_AVAILABLE = False
    weasyprint_error = """
❌ WeasyPrint not available. This is the preferred PDF generation library.

🔧 Installation options:

1. Ubuntu/Debian (recommended for Codespaces):
   sudo apt-get update
   sudo apt-get install python3-pip python3-cffi python3-brotli \\
       libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0
   pip install weasyprint

2. Alternative installation:
   pip install weasyprint

📚 WeasyPrint provides superior PDF quality with proper CSS styling
    and GitHub-like formatting.
"""

try:
    import markdown
    import markdown.extensions.extra
except ImportError as e:
    print(f"❌ Missing required markdown dependencies: {e}")
    print("📦 Install with: pip install markdown")
    sys.exit(1)


class MarkdownToPdfConverter:
    """Converts Markdown documents to PDF with GitHub-style formatting."""

    def __init__(self, verbose: bool = False, page_break_mode: str = "sections"):
        self.verbose = verbose
        self.converted_count = 0
        self.page_break_mode = page_break_mode  # "sections" or "continuous"

        # Validate page break mode
        if page_break_mode not in ["sections", "continuous"]:
            raise ValueError("page_break_mode must be 'sections' or 'continuous'")

        # Check for WeasyPrint availability
        if not WEASYPRINT_AVAILABLE:
            print(weasyprint_error)
            print(
                "❌ Cannot proceed without WeasyPrint. "
                "Please install dependencies first."
            )
            sys.exit(1)

    def log(self, message: str) -> None:
        """Print verbose log messages with British English styling."""
        if self.verbose:
            print(f"🔧 {message}")

    def get_github_css(self) -> str:
        """Return CSS styles that mimic GitHub's markdown rendering for A4 pages."""
        # Adjust spacing for continuous mode
        compact = self.page_break_mode == "continuous"

        margin = "1.5cm" if compact else "2cm"
        font_size = "10pt" if compact else "11pt"
        line_height = "1.4" if compact else "1.6"
        heading_margin_top = "16px" if compact else "24px"
        heading_margin_bottom = "12px" if compact else "16px"
        h1_size = "18pt" if compact else "20pt"
        h2_size = "14pt" if compact else "16pt"
        paragraph_margin = "12px" if compact else "16px"

        return f"""
        @page {{
            size: A4;
            margin: {margin};
            @bottom-center {{
                content: "Page " counter(page) " of " counter(pages);
                font-family: Roboto, Arial, sans-serif;
                font-size: 10pt;
                colour: #666;
            }}
            }}
        }}

        body {{
            font-family: Roboto, Arial, 'Noto Color Emoji', 'Segoe UI Emoji', 'Apple Color Emoji', sans-serif;
            font-size: {font_size};
            line-height: {line_height};
            colour: #24292e;
            max-width: none;
            margin: 0;
            padding: 0;
            background-colour: #fff;
        }}

        /* Headings */
        h1, h2, h3, h4, h5, h6 {{
            font-family: Roboto, Arial, sans-serif;
            font-weight: 600;
            line-height: 1.25;
            margin-top: {heading_margin_top};
            margin-bottom: {heading_margin_bottom};
            colour: #24292e;
        }}

        h1 {{
            font-size: {h1_size};
            border-bottom: 1px solid #eaecef;
            padding-bottom: 8px;
            page-break-after: avoid;
        }}

        h2 {{
            font-size: {h2_size};
            border-bottom: 1px solid #eaecef;
            padding-bottom: 6px;
            page-break-after: avoid;
        }}

        h3 {{
            font-size: 12pt;
            page-break-after: avoid;
        }}

        h4 {{
            font-size: 11pt;
            page-break-after: avoid;
        }}

        h5, h6 {{
            font-size: 10pt;
            page-break-after: avoid;
        }}

        /* Paragraphs and text */
        p {{
            font-family: Roboto, Arial, sans-serif;
            margin-top: 0;
            margin-bottom: {paragraph_margin};
            orphans: 2;
            widows: 2;
        }}

        /* Links */
        a {{
            font-family: Roboto, Arial, sans-serif;
            colour: #0366d6;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        /* Lists */
        ul, ol {{
            margin-top: 0;
            margin-bottom: {paragraph_margin};
            padding-left: 30px;
        }}
        
        /* Prevent compounding margins on nested lists */
        li > ul,
        li > ol {{
            margin-top: 4px;
            margin-bottom: 4px;
            padding-left: 20px;
        }}

        li {{
            font-family: Roboto, Arial, sans-serif;
            margin-bottom: 2px;
        }}

        /* Code blocks */
        pre {{
            font-family: 'SFMono-Regular', Consolas, monospace;
            background-colour: #f6f8fa;
            border-radius: 6px;
            font-size: 9pt;
            line-height: 1.45;
            overflow: auto;
            padding: 12px;
            margin-bottom: {paragraph_margin};
            page-break-inside: avoid;
        }}

        code {{
            font-family: 'SFMono-Regular', Consolas, monospace;
            background-colour: rgba(27,31,35,0.05);
            border-radius: 3px;
            font-size: 9pt;
            margin: 0;
            padding: 2px 4px;
        }}

        pre code {{
            background-colour: transparent;
            border: 0;
            display: inline;
            line-height: inherit;
            margin: 0;
            max-width: auto;
            overflow: visible;
            padding: 0;
            word-wrap: normal;
        }}

        /* Tables */
        table {{
            font-family: Roboto, Arial, sans-serif;
            border-collapse: collapse;
            border-spacing: 0;
            margin-top: 0;
            margin-bottom: {paragraph_margin};
            width: 100%;
            overflow: auto;
            font-size: 9pt;
        }}

        table th {{
            font-family: Roboto, Arial, sans-serif;
            font-weight: 600;
            background-colour: #f6f8fa;
            border: 1px solid #d0d7de;
            padding: 4px 8px;
        }}

        table td {{
            font-family: Roboto, Arial, sans-serif;
            border: 1px solid #d0d7de;
            padding: 4px 8px;
        }}

        table tr {{
            background-colour: #fff;
            border-top: 1px solid #c6cbd1;
        }}

        table tr:nth-child(2n) {{
            background-colour: #f6f8fa;
        }}

        /* Blockquotes */
        blockquote {{
            font-family: Roboto, Arial, sans-serif;
            border-left: 4px solid #dfe2e5;
            colour: #6a737d;
            margin: 0 0 {paragraph_margin} 0;
            padding: 0 16px;
        }}

        /* Horizontal rules */
        hr {{
            background-colour: #e1e4e8;
            border: 0;
            height: 2px;
            margin: 16px 0;
            padding: 0;
        }}

        /* Images */
        img {{
            max-width: 100%;
            height: auto;
            border-style: none;
        }}

        /* Task lists */
        .task-list-item {{
            list-style-type: none;
        }}

        .task-list-item-checkbox {{
            margin: 0 6px 0 -20px;
            vertical-align: middle;
        }}

        /* Syntax highlighting */
        .codehilite {{
            background-colour: #f6f8fa;
            border-radius: 6px;
            margin-bottom: {paragraph_margin};
            page-break-inside: avoid;
        }}

        .codehilite pre {{
            background-colour: transparent;
            margin: 0;
        }}

        /* Page breaks */
        .page-break {{
            page-break-before: always;
        }}

        /* Educational content styling */
        .exercise-header {{
            background-colour: #f1f8ff;
            border: 1px solid #c8e1ff;
            border-radius: 6px;
            padding: 12px;
            margin-bottom: 16px;
        }}

        .warning {{
            background-colour: #fff5b4;
            border: 1px solid #d4ac0d;
            border-radius: 6px;
            padding: 8px;
            margin: 12px 0;
        }}

        .info {{
            background-colour: #f1f8ff;
            border: 1px solid #c8e1ff;
            border-radius: 6px;
            padding: 8px;
            margin: 12px 0;
        }}

        .success {{
            background-colour: #f0fff4;
            border: 1px solid #22c55e;
            border-radius: 6px;
            padding: 8px;
            margin: 12px 0;
        }}
        """

    def setup_markdown_parser(self) -> markdown.Markdown:
        """Configure markdown parser with extensions for educational content."""
        extensions = [
            "markdown.extensions.extra",  # Tables, fenced code, etc.
            "markdown.extensions.codehilite",  # Syntax highlighting
            "markdown.extensions.toc",  # Table of contents
            "markdown.extensions.tables",  # Table support
            "markdown.extensions.fenced_code",  # Fenced code blocks
        ]

        extension_configs = {
            "codehilite": {
                "css_class": "codehilite",
                "use_pygments": True,
                "guess_lang": True,
            },
            "toc": {
                "permalink": False,  # Don't add permalink anchors in PDF
            },
        }

        return markdown.Markdown(
            extensions=extensions,
            extension_configs=extension_configs,
            output_format="html5",
        )

    def preprocess_markdown(self, content: str, input_file: Path) -> str:
        """Preprocess markdown content for better PDF conversion."""
        # Fix relative image paths to be absolute paths
        content = self.fix_image_paths(content, input_file)

        # Replace GitHub-style alerts with custom classes
        content = re.sub(
            r"> \*\*Note:\*\*(.*?)(?=\n\n|\n$|\Z)",
            r'<div class="info">**Note:**\1</div>',
            content,
            flags=re.DOTALL | re.MULTILINE,
        )

        content = re.sub(
            r"> \*\*Warning:\*\*(.*?)(?=\n\n|\n$|\Z)",
            r'<div class="warning">**Warning:**\1</div>',
            content,
            flags=re.DOTALL | re.MULTILINE,
        )

        content = re.sub(
            r"> \*\*Important:\*\*(.*?)(?=\n\n|\n$|\Z)",
            r'<div class="warning">**Important:**\1</div>',
            content,
            flags=re.DOTALL | re.MULTILINE,
        )

        # Add page breaks before major sections (## headings) based on mode
        if self.page_break_mode == "sections":
            lines = content.split("\n")
            processed_lines = []

            for i, line in enumerate(lines):
                # Don't add page break before the first heading
                if line.startswith("## ") and i > 0:
                    # Check if previous line isn't already a page break
                    page_break_div = '<div class="page-break"></div>'
                    if (
                        processed_lines
                        and not processed_lines[-1].strip() == page_break_div
                    ):
                        processed_lines.append(page_break_div)
                        processed_lines.append("")

                processed_lines.append(line)

            content = "\n".join(processed_lines)
            self.log("📄 Applied section page breaks (Mode 1: Sections)")
        else:
            self.log("📄 Continuous layout mode (Mode 2: No section breaks)")

        return content

    def fix_image_paths(self, content: str, input_file: Path) -> str:
        """Fix relative image paths to be absolute paths for PDF generation."""

        def replace_image_path(match):
            alt_text = match.group(1)
            image_path = match.group(2)
            title = match.group(3) if match.group(3) else ""

            self.log(f"🖼️  Processing image: {image_path}")

            # Skip if already HTTP/HTTPS URL or file:// URL
            if image_path.startswith(("http://", "https://", "file://")):
                self.log(f"📌 Skipping (web/file URL): {image_path}")
                return match.group(0)

            # Calculate absolute path relative to the input file
            input_dir = input_file.parent

            # Handle different relative path formats
            if image_path.startswith("/"):
                # Project-relative path (starts with / but relative to project root)
                absolute_path = Path.cwd() / image_path.lstrip("/")
                self.log(f"📁 Project root path: {absolute_path}")
            else:
                # Relative path from current file
                absolute_path = input_dir / image_path
                self.log(f"📁 Relative path: {absolute_path}")

            # Resolve to get canonical path
            try:
                resolved_path = absolute_path.resolve()
                self.log(f"🔍 Resolved to: {resolved_path}")
                if resolved_path.exists():
                    # Convert to file:// URL for WeasyPrint
                    file_url = resolved_path.as_uri()
                    self.log(f"🔗 File URL: {file_url}")
                    if title:
                        result = f"![{alt_text}]({file_url} {title})"
                    else:
                        result = f"![{alt_text}]({file_url})"
                    self.log(f"✅ Image path converted: {result}")
                    return result
                else:
                    self.log(f"⚠️  Image not found: {absolute_path}")
                    return match.group(0)  # Return original if not found
            except Exception as e:
                self.log(f"⚠️  Error resolving image path {image_path}: {e}")
                return match.group(0)  # Return original on error

        # Pattern to match markdown images: ![alt](path "title")
        pattern = r'!\[([^\]]*)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)'
        original_content = content
        processed_content = re.sub(pattern, replace_image_path, content)

        if original_content != processed_content:
            self.log("📝 Image paths were modified in the content")
        else:
            self.log("📝 No image paths were found or modified")

        return processed_content

    def convert_markdown_to_html(self, markdown_content: str, input_file: Path) -> str:
        """Convert markdown content to HTML with GitHub-style formatting."""
        # Preprocess the markdown (now includes image path fixing)
        processed_content = self.preprocess_markdown(markdown_content, input_file)

        # Setup markdown parser
        md_parser = self.setup_markdown_parser()

        # Convert to HTML
        html_content = md_parser.convert(processed_content)

        # Wrap in full HTML document
        full_html = f"""
        <!DOCTYPE html>
        <html lang="en-GB">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Converted Document</title>
            <style>
                {self.get_github_css()}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """

        return full_html

    def convert_file_to_pdf(self, input_file: Path, output_file: Path) -> bool:
        """Convert a single markdown file to PDF."""
        try:
            mode_desc = (
                "sections" if self.page_break_mode == "sections" else "continuous"
            )
            self.log(f"Converting {input_file.name} to PDF " f"(mode: {mode_desc})...")

            # Read markdown content
            with open(input_file, "r", encoding="utf-8") as f:
                markdown_content = f.read()

            # Convert to HTML (now includes image path fixing)
            html_content = self.convert_markdown_to_html(markdown_content, input_file)

            # Create output directory if it doesn't exist
            output_file.parent.mkdir(parents=True, exist_ok=True)

            # Convert HTML to PDF using WeasyPrint
            html_doc = HTML(string=html_content)
            html_doc.write_pdf(
                str(output_file), stylesheets=[CSS(string=self.get_github_css())]
            )

            self.log(f"✅ Successfully converted {input_file.name}")
            self.converted_count += 1
            return True

        except Exception as e:
            print(f"❌ Failed to convert {input_file}: {e}")
            return False

    def find_markdown_files(self, directory: Path) -> List[Path]:
        """Find all markdown files in a directory and its subdirectories."""
        markdown_files = []

        if not directory.exists():
            print(f"❌ Directory does not exist: {directory}")
            return markdown_files

        # Find all .md files recursively
        for file_path in directory.rglob("*.md"):
            if file_path.is_file():
                markdown_files.append(file_path)

        return sorted(markdown_files)

    def convert_all_in_directory(self, input_dir: Path, output_dir: Path) -> None:
        """Convert all markdown files in a directory to PDF."""
        markdown_files = self.find_markdown_files(input_dir)

        if not markdown_files:
            print(f"ℹ️  No markdown files found in {input_dir}")
            return

        print(f"📄 Found {len(markdown_files)} markdown files to convert")

        for md_file in markdown_files:
            # Calculate relative path to maintain directory structure
            relative_path = md_file.relative_to(input_dir)

            # Create output path with .pdf extension
            output_path = output_dir / relative_path.with_suffix(".pdf")

            self.convert_file_to_pdf(md_file, output_path)

    def convert_single_file(self, input_file: Path, output_dir: Path) -> None:
        """Convert a single markdown file to PDF."""
        if not input_file.exists():
            print(f"❌ File does not exist: {input_file}")
            return

        if not input_file.suffix.lower() == ".md":
            print(f"❌ File is not a markdown file: {input_file}")
            return

        # Create output filename
        output_file = output_dir / input_file.with_suffix(".pdf").name

        self.convert_file_to_pdf(input_file, output_file)


def main():
    """Handle command line arguments and execute conversion."""
    parser = argparse.ArgumentParser(
        description="Convert Markdown files to PDF with GitHub formatting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --all                   # Convert all markdown files
  %(prog)s --file README.md        # Convert single file
  %(prog)s --all --output-dir ./pdf_exports    # Custom output directory
  %(prog)s --file docs/setup-guide.md --verbose    # Verbose output
  %(prog)s --file README.md --page-break-mode sections     # Mode 1 (default)
  %(prog)s --file README.md --page-break-mode continuous   # Mode 2

Page Break Modes:
  Mode 1 (sections): Each ## heading starts a new page - good for exercises
  Mode 2 (continuous): No section page breaks - compact for printing

The converter uses British English spelling and maintains GitHub-style
formatting optimised for A4 printing with proper page breaks and
educational content styling.
        """,
    )

    # Input options (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--all",
        action="store_true",
        help="Convert all markdown files in the project (searches docs/, samples/, and root)",
    )
    input_group.add_argument(
        "--file", type=str, help="Convert a specific markdown file"
    )
    input_group.add_argument(
        "--directory",
        type=str,
        help="Convert all markdown files in a specific directory",
    )

    # Output options
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./pdf_lessons",
        help="Output directory for PDF files (default: ./pdf_lessons)",
    )

    # Utility options
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    parser.add_argument(
        "--page-break-mode",
        type=str,
        choices=["sections", "continuous"],
        default="sections",
        help=(
            'Page break mode: "sections" (new page for each ## heading) '
            'or "continuous" (no section page breaks for compact printing)'
        ),
    )

    args = parser.parse_args()

    # Initialize converter with page break mode
    converter = MarkdownToPdfConverter(
        verbose=args.verbose, page_break_mode=args.page_break_mode
    )

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("🔧 MD to PDF Converter - GitHub Style Formatting")
    print(f"📁 Output directory: {output_dir.absolute()}")

    # Display mode information
    mode_name = (
        "Mode 1: Sections"
        if args.page_break_mode == "sections"
        else "Mode 2: Continuous"
    )
    mode_desc = (
        "Each ## heading starts a new page"
        if args.page_break_mode == "sections"
        else "No page breaks between sections"
    )
    print(f"📄 Page break mode: {mode_name} ({mode_desc})")
    print()

    # Process based on arguments
    if args.all:
        # Convert markdown lessons directory
        directories_to_search = [
            Path("markdown_lessons"),  # Primary lessons directory
            Path("docs"),
            Path("samples"),
        ]

        for directory in directories_to_search:
            if directory.exists():
                print(f"🔍 Searching {directory}...")
                converter.convert_all_in_directory(directory, output_dir)
                print()

    elif args.file:
        input_file = Path(args.file)
        converter.convert_single_file(input_file, output_dir)

    elif args.directory:
        input_dir = Path(args.directory)
        converter.convert_all_in_directory(input_dir, output_dir)

    # Summary
    print("✅ Conversion complete!")
    print(f"📊 Files converted: {converter.converted_count}")
    print(f"📁 Output location: {output_dir.absolute()}")

    if converter.converted_count > 0:
        print(
            "📄 PDF files are formatted for A4 printing with "
            "GitHub-style markdown rendering"
        )


if __name__ == "__main__":
    main()
