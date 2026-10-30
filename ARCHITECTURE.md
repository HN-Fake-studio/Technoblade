# AETHERCRAFT LAUNCHER - SYSTEM ARCHITECTURE

## 1. Overview
Aethercraft Launcher is a high-performance, modular Minecraft Java Edition launcher designed for Android (Termux / Native integration). Built with zero bloat, emphasizing low frame-time variance, smart memory capping, and advanced optimization subsystems.

## 2. Directory Structure
```
AETHERCRAFT_LAUNCHER/
├── android/
├── launcher/          # Launcher engine & instance orchestration
├── core/              # System inspector & hardware validation
├── minecraft/         # Instance, version & asset management
├── runtime/           # Java runtime & JVM memory optimizer
├── renderer/          # OpenGL ES / Vulkan fallback manager
├── performance/       # Auto optimizer & thermal guard
├── framegen/          # Frame generation backend interface (Experimental)
├── upscaler/          # Generic upscaler interface
├── fsr/               # FSR manager & dynamic resolution scaling
├── mods/              # Mod loader compatibility manager
├── profiles/          # Profile duplication & export manager
├── ai/                # GeminiProvider AI crash analyzer
├── monitor/           # Telemetry & performance counter
├── benchmark/         # A/B testing & metrics exporter
├── logs/              # Log rotation & secret redaction
├── scripts/           # Utility scripts
├── tools/             # Build & deployment tools
├── docs/              # Architectural documentation
├── tests/             # Automated test suite
└── assets/            # Static assets
```

## 3. Core Subsystems & Status
- **System Inspector (`IMPLEMENTED`)**: Validates Android version, kernel, CPU, RAM, storage, GPU, and Java environment.
- **JVMOptimizer (`IMPLEMENTED`)**: Computes safe heap allocations (`-Xmx`, `-Xms`) keeping a 1.5GB Android OOM safety margin.
- **Instance & Launch Pipeline (`IMPLEMENTED`)**: Manages isolated instance directories, builds JVM arguments, and executes processes.
- **Crash Analyzer (`IMPLEMENTED`)**: Diagnoses OutOfMemoryError, Mod Conflicts, and classpath errors via `GeminiProvider`.
- **FSR & Upscaling (`PARTIAL`)**: Quality scaling modes and dynamic resolution control.
- **Frame Generation (`EXPERIMENTAL`)**: Interface defined; hardware pipeline integration pending Vulkan/OpenGL hooks.
