class MeasurementConverterActivity : AppCompatActivity() {

    // Define UI elements
    val inputEditText: EditText = findViewById(R.id.inputEditText)
    val unitSpinner: Spinner = findViewById(R.id.unitSpinner)
    val resultTextView: TextView = findViewById(R.id.resultTextView)

    // Define conversion factors
    val meterToFeet = 3.28084
    val kilogramToPound = 2.20462

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
