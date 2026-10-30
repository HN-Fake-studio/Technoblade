#!/usr/bin/env python3
"""
Aethercraft Launcher - JVM Optimizer & Runtime Manager Subsystem
Dynamic RAM allocation, safety margins, profiles (Balanced, Performance, Max Performance, Battery Saver, Compatibility, Custom), and JVM argument generation.
"""

class JVMOptimizer:
    PROFILES = {
        "Balanced": {"xmx_percentage": 0.40, "gc": "G1GC", "extra_args": ["-XX:+UseG1GC", "-XX:MaxGCPauseMillis=50"]},
        "Performance": {"xmx_percentage": 0.55, "gc": "G1GC", "extra_args": ["-XX:+UseG1GC", "-XX:ParallelGCThreads=4", "-XX:MaxGCPauseMillis=30"]},
        "Maximum Performance": {"xmx_percentage": 0.65, "gc": "ZGC", "extra_args": ["-XX:+UseZGC", "-XX:+UnlockExperimentalVMOptions"]},
        "Battery Saver": {"xmx_percentage": 0.30, "gc": "SerialGC", "extra_args": ["-XX:+UseSerialGC"]},
        "Compatibility": {"xmx_percentage": 0.35, "gc": "G1GC", "extra_args": ["-XX:+UseG1GC"]}
    }

    def __init__(self, total_ram_mb: int, profile_name: str = "Balanced"):
        self.total_ram_mb = total_ram_mb
        self.profile_name = profile_name if profile_name in self.PROFILES else "Balanced"
        self.profile = self.PROFILES[self.profile_name]

    def calculate_ram(self) -> dict:
        # Safety margin: ensure Android has at least 1.5GB - 2GB free
        safety_reserve_mb = 1536
        usable_ram = max(512, self.total_ram_mb - safety_reserve_mb)
        
        allocated_mb = int(usable_ram * self.profile["xmx_percentage"])
        # Hard cap for mobile devices to prevent OOM
        allocated_mb = min(allocated_mb, 3072)
        allocated_mb = max(allocated_mb, 512)

        return {
            "total_system_mb": self.total_ram_mb,
            "allocated_xmx_mb": allocated_mb,
            "safety_reserve_mb": safety_reserve_mb
        }

    def build_jvm_args(self, custom_args: list = None) -> list:
        ram_info = self.calculate_ram()
        xmx = f"-Xmx{ram_info['allocated_xmx_mb']}M"
        xms = f"-Xms{min(512, ram_info['allocated_xmx_mb'])}M"
        
        args = [xms, xmx]
        args.extend(self.profile["extra_args"])
        
        # Optimization flags for ARM64 Android
        args.extend([
            "-XX:+AlwaysPreTouch",
            "-XX:+UseStringDeduplication",
            "-Dfile.encoding=UTF-8"
        ])

        if custom_args:
            args.extend(custom_args)

        return args

if __name__ == "__main__":
    opt = JVMOptimizer(total_ram_mb=5400, profile_name="Performance")
    print("RAM Allocation:", opt.calculate_ram())
    print("JVM Args:", opt.build_jvm_args())
