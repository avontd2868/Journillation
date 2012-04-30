package com.isc.Journillation;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.widget.Toast;
import android.widget.Button;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.EditText;
import android.view.View.OnKeyListener;
import android.view.KeyEvent;
import android.widget.ProgressBar;
import java.util.Random;
import android.widget.TextView;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ImageView;
//EndImports

public class Journillation extends Activity {
public int iscVTrue = 1;
public int iscVQuitAfter = 0;
public String iscVmdH2end = " ##\n";
public String iscVmdH2 = "\n\n## ";
public String iscVFinalState = "";
public String iscVmdH1end = " #\n\n";
public String iscVmdH1begin = "# ";
public String iscVDate = "";
public String iscVJournalFile = "changeme.mkd";
public String iscVJournalA1 = "";
public String iscVJournalQ1 = "What did I have for breakfast today?";
public String iscVJournalEntry = "";
private EditText iscWindow1DateBox0;
private TextView iscWindow1Label0;
private Button iscWindow1Finish0;
private Button iscWindow1Save0;
private Button iscWindow1Button20;
private EditText iscWindow1MainEntry0;
private EditText iscWindow1ATextField10;
private EditText iscWindow1QTextBox0;
private TextView iscWindow1Title0;

//EndOfGlobalVariables


@Override
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
iscWindow1();
//iscApp1Launched
}

private class ISCWebViewClient extends WebViewClient {
@Override
public boolean shouldOverrideUrlLoading(WebView view, String url) {
view.loadUrl(url);
return true;
}
}

public void iscWindow1(){
setContentView(R.layout.iscwindow1layout);
iscWindow1DateBox0 = (EditText)this.findViewById(R.id.iscWindow1DateBox0);
iscWindow1DateBox0.setOnKeyListener(new OnKeyListener() {
@Override
public boolean onKey(View v, int keyCode, KeyEvent event) {
iscGetTextBox9();
//iscWindow1DateBoxChanged
return false;
}
});
iscWindow1Finish0 = (Button)this.findViewById(R.id.iscWindow1Finish0);
iscWindow1Finish0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscSetNumber8();
//iscWindow1FinishClicked
}
});
iscWindow1Save0 = (Button)this.findViewById(R.id.iscWindow1Save0);
iscWindow1Save0.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscGetTextField7();
//iscWindow1SaveClicked
}
});
iscWindow1Button20 = (Button)this.findViewById(R.id.iscWindow1Button20);
iscWindow1Button20.setOnClickListener(new OnClickListener() {
@Override
public void onClick(View v) {
iscAppQuit19();
//iscWindow1Button2Clicked
}
});
iscWindow1QTextBox0 = (EditText)this.findViewById(R.id.iscWindow1QTextBox0);
iscWindow1QTextBox0.setOnKeyListener(new OnKeyListener() {
@Override
public boolean onKey(View v, int keyCode, KeyEvent event) {
iscGetTextBox10();
//iscWindow1QTextBoxChanged
return false;
}
});
//iscWindow1Opened
}

public void iscSaveAllTextToFile4()
{
try {
OutputStreamWriter out = new OutputStreamWriter(openFileOutput("iscVJournalFile",0));
out.write(iscVFinalState);
out.close();
} catch (java.io.IOException e) {
}
iscIfThen11();
//iscSaveAllTextToFile4Done
}


public void iscSaveTextFileDialog5()
{
iscSaveAllTextToFile4();
//iscSaveTextFileDialog5Done
}


public void iscGetTextField6()
{
iscWindow1ATextField10 = (EditText)this.findViewById(R.id.iscWindow1ATextField10);
String strThisString = iscWindow1ATextField10.getText().toString();
iscVJournalA1 = strThisString;
iscCombineText18();
//iscGetTextField6Done
}


public void iscGetTextField7()
{
iscWindow1MainEntry0 = (EditText)this.findViewById(R.id.iscWindow1MainEntry0);
String strThisString = iscWindow1MainEntry0.getText().toString();
iscVJournalEntry = strThisString;
iscGetTextField6();
//iscGetTextField7Done
}


public void iscSetNumber8()
{
iscVQuitAfter = iscVTrue;
iscGetTextField7();
//iscSetNumber8Done
}


public void iscGetTextBox9()
{
iscWindow1DateBox0 = (EditText)this.findViewById(R.id.iscWindow1DateBox0);
String strThisString = iscWindow1DateBox0.getText().toString();
iscVDate = strThisString;
//iscGetTextBox9Done
}


public void iscGetTextBox10()
{
iscWindow1QTextBox0 = (EditText)this.findViewById(R.id.iscWindow1QTextBox0);
String strThisString = iscWindow1QTextBox0.getText().toString();
iscVJournalQ1 = strThisString;
//iscGetTextBox10Done
}


public void iscIfThen11()
{
if (iscVQuitAfter == iscVTrue)
{
iscAppQuit19();
//iscIfThen11True

}
else
{
//iscIfThen11False
}
}


public void iscCombineText12()
{
iscVFinalState = iscVFinalState + iscVJournalA1;
iscSaveTextFileDialog5();
//iscCombineText12Done
}


public void iscCombineText13()
{
iscVFinalState = iscVFinalState + iscVmdH2end;
iscCombineText12();
//iscCombineText13Done
}


public void iscCombineText14()
{
iscVFinalState = iscVFinalState + iscVJournalQ1;
iscCombineText13();
//iscCombineText14Done
}


public void iscCombineText15()
{
iscVFinalState = iscVFinalState + iscVmdH2;
iscCombineText14();
//iscCombineText15Done
}


public void iscCombineText16()
{
iscVFinalState = iscVFinalState + iscVJournalEntry;
iscCombineText15();
//iscCombineText16Done
}


public void iscCombineText17()
{
iscVFinalState = iscVFinalState + iscVmdH1end;
iscCombineText16();
//iscCombineText17Done
}


public void iscCombineText18()
{
iscVFinalState = iscVmdH1begin + iscVDate;
iscCombineText17();
//iscCombineText18Done
}


public void iscAppQuit19()
{
this.finish();}


//EndOfFunctions

}
