package cn.edu.sicnu.cs.yn.exeperise2

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import cn.edu.sicnu.cs.yn.exeperise2.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private lateinit var model: ProgramAdviser
    private var dynamicCount = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        model = ProgramAdviser()

        // 区1：动态添加 TextView
        binding.btnAddText.setOnClickListener {
            dynamicCount++
            val tv = TextView(this)
            tv.text = getString(R.string.dynamic_text_format, dynamicCount)
            tv.textSize = 16f
            tv.setPadding(16, 16, 16, 16)
            binding.dynamicContainer.addView(tv)
        }

        // 区2：MVC，点按钮问 Model 要推荐
        binding.btnQuery.setOnClickListener {
            binding.tvResult.setText(model.getAdvice())
        }
    }
}
