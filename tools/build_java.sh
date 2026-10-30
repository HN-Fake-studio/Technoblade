#!/usr/bin/env bash
# Aethercraft Launcher - Java Build Script
set -e

JAVA_HOME="/data/data/com.termux/files/usr/lib/jvm/java-17-openjdk"
PATH="$JAVA_HOME/bin:$PATH"

echo "[*] Using JAVA_HOME: $JAVA_HOME"
echo "[*] Checking javac version:"
javac -version

echo "[*] Compiling Aethercraft Launcher Java components (if any)..."
# If there are java source files, compile them here
echo "[*] Build check completed successfully."
