# Aethercraft Launcher - Development State

## Current Status Overview
- **Project Name:** Aethercraft Launcher
- **Target OS:** Android 14 (aarch64) with Termux host integration
- **Execution Mode:** Hybrid Python core backend + Android architecture stub & Gradle project preparation

## System Status Matrix
| Subsystem | Status | Technical Evidence / Notes |
| :--- | :--- | :--- |
| System Inspector | **IMPLEMENTED** | Successfully inspects kernel, Android version, CPU cores/freq/governor, RAM, storage, GPU/Vulkan, Termux, and Java runtime via `/proc`, `getprop`, and system utilities. |
| JVM Optimizer & Memory Manager | **IMPLEMENTED** | Dynamically calculates heap (`-Xmx`, `-Xms`) based on host RAM with a 1.5GB safety reserve for Android OOM protection. |
| Instance & Version Manager | **IMPLEMENTED** | Creates isolated instance directories (`instances/{name}`), configures metadata, JSON profiles, and log paths. |
| Launch Pipeline & Process Manager | **IMPLEMENTED** | Assembles JVM arguments, executes Java process, captures `stdout`/`stderr`, and handles exit codes. |
| Crash Analyzer & AI Provider | **IMPLEMENTED** | Analyzes crash logs (OutOfMemoryError, ModConflict, NoClassDefFoundError) via `GeminiProvider` abstraction without hardcoded API keys. |
| FSR & Upscaling Subsystem | **PARTIAL / EXPERIMENTAL** | Quality modes (Ultra Quality, Quality, Balanced, Performance) and dynamic resolution algorithms implemented; hardware pipeline integration requires translation layer (Termux-X11 / ANGLE). |
| Frame Generation Subsystem | **EXPERIMENTAL** | Interface defined (`FrameGenerationBackend`), but hardware-level interpolation on Android needs specialized Vulkan/OpenGL hooks. Marked as experimental to avoid fake claims. |
| Benchmark & Monitoring | **IMPLEMENTED** | Simulates and measures Average FPS, 1% Low, Frame Time, and exports JSON reports. |
| Android UI & Gradle App | **PARTIAL** | Core architecture defined; Gradle project skeleton ready for APK build integration. |
