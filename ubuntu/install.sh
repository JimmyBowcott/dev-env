set -euo pipefail

OS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo
echo "Installing packages from package lists..."
"$OS_DIR/scripts/packages.sh"
echo "Packages installed"

echo
echo "Syncing home directory"
"$OS_DIR/scripts/dotfiles.sh"
echo "Copied files to ~/"

echo
echo "Running postinstall script"
"$OS_DIR/scripts/postinstall.sh"
echo "Postinstall completed"

echo
echo " Setup complete. Please reboot device."
