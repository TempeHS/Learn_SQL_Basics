# Utilities for SQL Lessons

This directory contains utility scripts for managing the SQL lessons project.

## MD to PDF Converter

Converts markdown lesson files to professionally formatted PDF documents with emoji support.

### Quick Start

**Option 1: Automated (Recommended)**

```bash
bash utils/convert_lessons.sh
```

This will automatically:

- Check for required dependencies
- Offer to install them if missing
- Convert all lessons from `markdown_lessons/` to `pdf_lessons/`

**Option 2: Manual Installation**

1. Install dependencies first:

```bash
bash utils/install_dependencies.sh
```

2. Convert lessons:

```bash
python3 utils/md_to_pdf.py --directory markdown_lessons --output-dir pdf_lessons
```

### Features

✅ **Full emoji support** - Renders emojis correctly (🎯, 📚, 🛠️, etc.)  
✅ **GitHub-style formatting** - Professional markdown rendering  
✅ **A4 page optimization** - Ready for printing  
✅ **Syntax highlighting** - Color-coded SQL and code blocks  
✅ **Automatic page breaks** - Smart section breaks for better readability

### Dependencies Installed

The installation script automatically installs:

**System Packages:**

- WeasyPrint dependencies (pango, harfbuzz, cairo)
- Emoji fonts (Noto Color Emoji, Symbola)
- Font configuration tools

**Python Packages:**

- `weasyprint` - Professional PDF generation
- `markdown` - Markdown parsing
- `pygments` - Syntax highlighting
- `beautifulsoup4` - HTML processing

### Usage Options

**Convert all lessons:**

```bash
python3 utils/md_to_pdf.py --directory markdown_lessons --output-dir pdf_lessons
```

**Convert single file:**

```bash
python3 utils/md_to_pdf.py --file markdown_lessons/lesson1_instructions.md --output-dir pdf_lessons
```

**Verbose output:**

```bash
python3 utils/md_to_pdf.py --directory markdown_lessons --output-dir pdf_lessons --verbose
```

**Page break modes:**

```bash
# Mode 1: Each ## heading starts a new page (default - good for lessons)
python3 utils/md_to_pdf.py --directory markdown_lessons --page-break-mode sections

# Mode 2: Continuous layout (compact for printing)
python3 utils/md_to_pdf.py --directory markdown_lessons --page-break-mode continuous
```

### Troubleshooting

**Error: "WeasyPrint not available"**

- Run: `bash utils/install_dependencies.sh`

**Emojis not rendering:**

- Ensure emoji fonts are installed: `bash utils/install_dependencies.sh`
- Check font cache: `fc-cache -f -v`

**Permission denied:**

- Make scripts executable: `chmod +x utils/*.sh`

### Project Structure

```
utils/
├── md_to_pdf.py              # Main converter script
├── install_dependencies.sh    # Dependency installation
├── convert_lessons.sh         # Quick conversion wrapper
└── README.md                  # This file
```

### Notes

- PDFs are generated with A4 page size
- GitHub-style CSS is applied for professional appearance
- Images are automatically resolved to absolute paths
- Syntax highlighting supports SQL and multiple programming languages
- British English spelling is used throughout
