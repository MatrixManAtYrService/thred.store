set -euo pipefail
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
BEFORE=$(mktemp)
AFTER=$(mktemp)
node listInstalledFonts.js | sort > $BEFORE
for font in "cnr.otf" "ArchivoNarrow-Regular.otf" "ArchivoNarrow-Bold.otf"
do
    cp -v "$DIR/$font" "/usr/share/fonts/$font"
    chmod 0444 /usr/share/fonts/$font
done
node listInstalledFonts.js | sort > $AFTER
diff $BEFORE $AFTER
