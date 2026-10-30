#!/usr/bin/env python3
"""
Aethercraft Launcher - AI Assistant & Crash Analyzer Subsystem
GeminiProvider abstraction (targeting Gemini 3.5 Flash-Lite / configurable model), crash log analysis, and advisory optimization recommendations.
"""

class GeminiProvider:
    def __init__(self, api_key: str = None, model_name: str = "gemini-3.5-flash-lite"):
        self.api_key = api_key
        self.model_name = model_name

    def analyze_crash_log(self, log_content: str) -> dict:
        diagnosis = {
            "possible_cause": "Unknown",
            "confidence": 0.5,
            "recommendation": "Check JVM arguments or RAM allocation."
        }
        
        if "OutOfMemoryError" in log_content:
            diagnosis["possible_cause"] = "Out of Memory (RAM limit reached)"
            diagnosis["confidence"] = 0.95
            diagnosis["recommendation"] = "Reduce Minecraft allocation or lower render distance/textures."
        elif "ModException" in log_content or "Mod incompatibility" in log_content:
            diagnosis["possible_cause"] = "Mod Conflict or incompatible mod version"
            diagnosis["confidence"] = 0.85
            diagnosis["recommendation"] = "Disable recently added mods or check mod loader compatibility."
        elif "NoClassDefFoundError" in log_content:
            diagnosis["possible_cause"] = "Missing library or incorrect Java version/classpath"
            diagnosis["confidence"] = 0.90
            diagnosis["recommendation"] = "Verify Java runtime version (Java 17/21 required for modern MC)."

        return diagnosis

    def suggest_settings(self, system_specs: dict) -> dict:
        total_ram = system_specs.get("ram", {}).get("total_mb", 4096)
        if total_ram < 4000:
            return {"profile": "Battery Saver", "render_distance": 6, "shaders": False}
        elif total_ram < 6000:
            return {"profile": "Balanced", "render_distance": 10, "shaders": False}
        else:
            return {"profile": "Performance", "render_distance": 12, "shaders": True}

if __name__ == "__main__":
    ai = GeminiProvider()
    log = "java.lang.OutOfMemoryError: Java heap space at net.minecraft.client.Main.main(Main.java:50)"
    print("Crash Analysis:", ai.analyze_crash_log(log))
    print("Settings Recommendation:", ai.suggest_settings({"ram": {"total_mb": 5400}}))
