//using kotlin language run using *javac test2.java*

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Spinner
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MeasurementConverterActivity : AppCompatActivity() {

    // Define UI elements
    val inputEditText: EditText by lazy { findViewById<EditText>(R.id.inputEditText) }
    val unitSpinner: Spinner by lazy { findViewById<Spinner>(R.id.unitSpinner) }
    val resultTextView: TextView by lazy { findViewById<TextView>(R.id.resultTextView) }

    // Define conversion factors.
    val meterToFeet = 3.28084
    val kilogramToPound = 2.20462

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_measurement_converter)

        // Handle conversion button click
        val convertButton: Button = findViewById(R.id.convertButton)
        convertButton.setOnClickListener {
            val inputValue = inputEditText.text.toString().toDouble()
            val selectedUnit = unitSpinner.selectedItem.toString()

            // Perform conversion based on selected unit
            val result = when (selectedUnit) {
                "Meters to Feet" -> inputValue * meterToFeet
                "Kilograms to Pounds" -> inputValue * kilogramToPound
                // Add more conversion cases as needed
                else -> inputValue // Default case
            }

            // Display result
            resultTextView.text = "$inputValue $selectedUnit is $result in the desired unit."
        }
    }
}
