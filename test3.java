// this is in only java *use javac test3.java* to run

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MeasurementConverterActivity extends AppCompatActivity {

    // Define UI elements
    private EditText inputEditText;
    private Spinner unitSpinner;
    private TextView resultTextView;

    // Define conversion factors
    private final double meterToFeet = 3.28084;
    private final double kilogramToPound = 2.20462;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_measurement_converter);

        // Initialize UI elements
        inputEditText = findViewById(R.id.inputEditText);
        unitSpinner = findViewById(R.id.unitSpinner);
        resultTextView = findViewById(R.id.resultTextView);

        // Handle conversion button click
        Button convertButton = findViewById(R.id.convertButton);
        convertButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                double inputValue = Double.parseDouble(inputEditText.getText().toString());
                String selectedUnit = unitSpinner.getSelectedItem().toString();

                // Perform conversion based on selected unit
                double result;
                switch (selectedUnit) {
                    case "Meters to Feet":
                        result = inputValue * meterToFeet;
                        break;
                    case "Kilograms to Pounds":
                        result = inputValue * kilogramToPound;
                        break;
                    // Add more conversion cases as needed
                    default:
                        result = inputValue; // Default case
                }

                // Display result
                resultTextView.setText(inputValue + " " + selectedUnit + " is " + result + " in the desired unit.");
            }
        });
    }
}
