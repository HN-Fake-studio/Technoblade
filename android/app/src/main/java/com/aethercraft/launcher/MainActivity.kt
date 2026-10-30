package com.aethercraft.launcher

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val titleText: TextView = findViewById(R.id.titleText)
        val launchButton: Button = findViewById(R.id.launchButton)

        titleText.text = "Aethercraft Launcher v1.0\nHigh-Performance Minecraft Java Launcher"

        launchButton.setOnClickListener {
            titleText.text = "Status: Initializing Instance & Launch Pipeline..."
        }
    }
}
