set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo
echo "Installing packages from package lists..."
"$REPO/scripts/packages.sh"
echo "Packages installed"

echo
echo "Installing AUR packages..."
"$REPO/scripts/aur.sh"
echo "Packages installed from AUR"

echo
echo "Syncing home directory"
"$REPO/scripts/dotfiles.sh"
echo "Copied files to ~/"

echo
echo "Running postinstall scripts"
"$REPO/scripts/postinstall.sh"
echo "Postinstall completed"

echo
echo " Setup complete. Please reboot device."
