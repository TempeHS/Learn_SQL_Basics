# Quick Start Guide: Converting Lessons to PDF

## ✅ Ready to Use!

The MD to PDF conversion tool is now fully configured and tested.

### Quick Commands

**Convert all lessons (recommended):**

```bash
bash utils/convert_lessons.sh
```

**Or manually:**

```bash
python3 utils/md_to_pdf.py --directory markdown_lessons --output-dir pdf_lessons
```

## What's Been Set Up

✅ **Dependencies Installed:**

- WeasyPrint (PDF generation)
- Markdown parser with extensions
- Pygments (syntax highlighting)
- Emoji fonts (Noto Color Emoji, Symbola)
- All system dependencies

✅ **Script Configuration:**

- Default input directory: `markdown_lessons/`
- Default output directory: `pdf_lessons/`
- Emoji font family added to CSS
- GitHub-style formatting
- A4 page optimization

✅ **Successfully Tested:**

- All 10 lessons converted successfully
- PDFs saved to `pdf_lessons/` directory
- Emoji support enabled

## Features

🎯 **Professional Formatting**

- GitHub-style markdown rendering
- Syntax highlighting for SQL code
- Clean, readable layout

📄 **A4 Optimized**

- Ready for printing
- Proper page breaks
- Page numbers included

😊 **Full Emoji Support**

- Renders 🎯, 📚, 🛠️, ✅, and all other emojis
- Noto Color Emoji font installed
- Fallback fonts configured

## Files Created

```
utils/
├── md_to_pdf.py              # Main conversion script (updated)
├── install_dependencies.sh    # Installs all dependencies
├── convert_lessons.sh         # Quick conversion wrapper
└── README.md                  # Detailed documentation
```

## Conversion Modes

**Mode 1: Sections (Default)**

- Each ## heading starts a new page
- Best for lesson materials
- Easier to navigate

**Mode 2: Continuous**

- No section page breaks
- More compact
- Better for printing

To use Mode 2:

```bash
python3 utils/md_to_pdf.py --directory markdown_lessons --page-break-mode continuous
```

## Next Steps

1. ✅ All 10 lessons have been converted
2. Check `pdf_lessons/` directory for the PDFs
3. PDFs are ready for distribution to students
4. Re-run conversion anytime lessons are updated

## Troubleshooting

If you need to reinstall dependencies:

```bash
bash utils/install_dependencies.sh
```

For help with the converter:

```bash
python3 utils/md_to_pdf.py --help
```

---

**Last tested:** Successfully converted all 10 lessons  
**Status:** ✅ Production ready
