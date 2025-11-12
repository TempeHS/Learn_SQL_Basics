#!/bin/bash
# Install all dependencies required for MD to PDF conversion with emoji support

echo "=================================================="
echo "Installing Dependencies for MD to PDF Converter"
echo "=================================================="
echo ""

# Update package list
echo "📦 Updating package list..."
sudo apt-get update -qq

# Install system dependencies for WeasyPrint
echo "📦 Installing WeasyPrint system dependencies..."
sudo apt-get install -y -qq \
    python3-pip \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info

echo "✓ System dependencies installed"
echo ""

# Install emoji font support
echo "🎨 Installing emoji fonts..."
sudo apt-get install -y -qq \
    fonts-noto-color-emoji \
    fonts-symbola \
    fonts-noto \
    fonts-dejavu-core \
    fontconfig

echo "✓ Emoji fonts installed"
echo ""

# Refresh font cache
echo "🔄 Refreshing font cache..."
fc-cache -f -v > /dev/null 2>&1

echo "✓ Font cache refreshed"
echo ""

# Install Python packages
echo "🐍 Installing Python packages..."
pip install --quiet --upgrade pip
pip install --quiet markdown weasyprint pygments beautifulsoup4

echo "✓ Python packages installed"
echo ""

# Verify installation
echo "🔍 Verifying installation..."
python3 -c "import weasyprint; import markdown; import pygments; print('✓ All Python packages verified')"

echo ""
echo "=================================================="
echo "✓ Installation Complete!"
echo "=================================================="
echo ""
echo "You can now run: python3 utils/md_to_pdf.py --all"
echo ""
