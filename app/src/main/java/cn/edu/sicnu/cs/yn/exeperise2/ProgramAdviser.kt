package cn.edu.sicnu.cs.yn.exeperise2

class ProgramAdviser {
    // Model 层：存数据，提供查询
    private val adviceMap = mapOf(
        "default" to R.string.recommend_lang
    )

    fun getAdvice(key: String = "default"): Int {
        return adviceMap[key] ?: R.string.result_hint
    }
}
