#!/bin/bash

# Define directories
SITE_DIR="$HOME/Desktop/xibalba-solutions-site"
WIX_APP_DIR="$HOME/Desktop/xibalba-wix-app"

echo "Creating Wix App structure at $WIX_APP_DIR..."

# Create the new structure
mkdir -p "$WIX_APP_DIR/src"
mkdir -p "$WIX_APP_DIR/src/backend"

# Create a basic package.json for Wix CLI Apps
cat <<EOF > "$WIX_APP_DIR/package.json"
{
  "name": "xibalba-solutions",
  "version": "1.0.0",
  "description": "Xibalba Solutions Site on Wix",
  "scripts": {
    "dev": "wix app dev",
    "build": "wix app build",
    "release": "wix app release"
  },
  "devDependencies": {
    "@wix/cli": "latest",
    "@wix/cli-app": "latest"
  }
}
EOF

echo "Migrating HTML/CSS files to src..."

# Copy your existing files to the src directory
cp -r "$SITE_DIR"/*.html "$WIX_APP_DIR/src/" 2>/dev/null
cp -r "$SITE_DIR"/css "$WIX_APP_DIR/src/" 2>/dev/null
cp -r "$SITE_DIR"/*.png "$WIX_APP_DIR/src/" 2>/dev/null
cp -r "$SITE_DIR"/*.ico "$WIX_APP_DIR/src/" 2>/dev/null
cp -r "$SITE_DIR"/screenshots "$WIX_APP_DIR/src/" 2>/dev/null

echo "Migration complete!"
echo ""
echo "CRITICAL: You must now link this local code to a Wix App Identity."
echo "Please run the following commands manually:"
echo "1. cd $WIX_APP_DIR"
echo "2. npx wix login"
echo "3. npx wix app release"
echo ""
echo "On the first 'release', the CLI will ask if you want to create a new app. Select 'Yes'."
