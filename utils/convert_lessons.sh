#!/bin/bash
# Simple wrapper script to convert all markdown lessons to PDF

echo "=================================================="
echo "Converting SQL Lessons from Markdown to PDF"
echo "=================================================="
echo ""

# Check if dependencies are installed
if ! python3 -c "import weasyprint" 2>/dev/null; then
    echo "⚠️  Dependencies not installed!"
    echo ""
    echo "Would you like to install them now? (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        bash utils/install_dependencies.sh
    else
        echo "❌ Cannot proceed without dependencies."
        echo "Run: bash utils/install_dependencies.sh"
        exit 1
    fi
fi

# Navigate to project root if script is run from utils/
if [ "$(basename "$PWD")" = "utils" ]; then
    cd ..
fi

# Run the conversion
python3 utils/md_to_pdf.py --directory markdown_lessons --output-dir pdf_lessons --verbose

echo ""
echo "=================================================="
echo "✓ Conversion Complete!"
echo "=================================================="
echo ""
echo "📁 PDF files saved to: pdf_lessons/"
echo ""
