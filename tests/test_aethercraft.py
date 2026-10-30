#!/usr/bin/env python3
"""
Aethercraft Launcher - Automated Unit & Integration Tests
Validates SystemInspector, JVMOptimizer, FSRManager, GeminiProvider, and BenchmarkRunner.
"""

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.system_inspector import SystemInspector
from runtime.jvm_optimizer import JVMOptimizer
from fsr.fsr_manager import FSRManager
from ai.ai_assistant import GeminiProvider
from benchmark.benchmark_runner import BenchmarkRunner

class TestAethercraftLauncher(unittest.TestCase):

    def test_system_inspector(self):
        inspector = SystemInspector()
        specs = inspector.inspect_all()
        self.assertIn("os", specs)
        self.assertIn("ram", specs)
        self.assertIn("cpu", specs)

    def test_jvm_optimizer(self):
        opt = JVMOptimizer(total_ram_mb=5400, profile_name="Performance")
        ram_info = opt.calculate_ram()
        self.assertGreater(ram_info["allocated_xmx_mb"], 0)
        self.assertLessEqual(ram_info["allocated_xmx_mb"], 3072)
        args = opt.build_jvm_args()
        self.assertTrue(any("-Xmx" in arg for arg in args))

    def test_fsr_manager(self):
        fsr = FSRManager(1920, 1080, "Balanced")
        w, h = fsr.compute_render_resolution()
        self.assertGreater(w, 0)
        self.assertGreater(h, 0)
        w_adj, h_adj = fsr.adjust_dynamic_resolution(30.0, 60.0)
        self.assertGreater(w_adj, 0)

    def test_ai_crash_analyzer(self):
        ai = GeminiProvider()
        diagnosis = ai.analyze_crash_log("java.lang.OutOfMemoryError: Java heap space")
        self.assertEqual(diagnosis["possible_cause"], "Out of Memory (RAM limit reached)")
        self.assertGreater(diagnosis["confidence"], 0.9)

    def test_benchmark_runner(self):
        runner = BenchmarkRunner("Balanced")
        results = runner.run_benchmark_simulation(duration_sec=1)
        self.assertEqual(results["profile"], "Balanced")
        self.assertIn("average_fps", results)
        self.assertIn("one_percent_low", results)

if __name__ == "__main__":
    unittest.main()
