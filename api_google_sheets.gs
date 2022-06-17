// Criar o botão
function onOpen(){
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Ranking').addItem('Get Score', 'PredictAll').addToUi();
}

host = 'google-sheets-healthinsurance.herokuapp.com'

// Helper Function
function ApiCall(data, endpoint){
  var url = 'https://' + host + endpoint;
  var payload = JSON.stringify(data);
  var options = {'method':'POST', 'contentType':'application/json', 'payload':payload};
  var response = UrlFetchApp.fetch(url, options);

  // get response
  var rc = response.getResponseCode();
  var responseText = response.getContentText();

  if(rc !== 200){
    Logger.log('Response (%s) %s', rc, responseText);
  } 
  else{
    prediction = JSON.parse(responseText);
  }
  return prediction

};

// Fazer a Predição do Score
function PredictAll(){
  var ss = SpreadsheetApp.getActiveSheet();
  var titleColumns = ss.getRange('A1:K1').getValues()[0];
  var lastRow = ss.getLastRow()

  var data = ss.getRange('A2' + ':' + 'K' + lastRow).getValues();

  // percorrer todas as linhas
  for(row in data){
    var json = new Object()

    // percorrer todas as colunas
    for(var j=0; j < titleColumns.length; j++){
      json[titleColumns[j]] = data[row][j];
    };

    // Lista de json para enviar
    var json_send = new Object();

    json_send['id'] = json['id']
    json_send['Gender'] = json['Gender']
    json_send['Age'] = json['Age']
    json_send['Driving_License'] = json['Driving_License']
    json_send['Region_Code'] = json['Region_Code']
    json_send['Previously_Insured'] = json['Previously_Insured']
    json_send['Vehicle_Age'] = json['Vehicle_Age']
    json_send['Vehicle_Damage'] = json['Vehicle_Damage']
    json_send['Annual_Premium'] = json['Annual_Premium']
    json_send['Policy_Sales_Channel'] = json['Policy_Sales_Channel']
    json_send['Vintage'] = json['Vintage']

    pred = ApiCall(json_send, '/healthinsurance/predict');

    // Enviar score para o google sheets
    ss.getRange(Number(row) + 2, 12).setValue(pred[0]['score'])

  };
  // Ordenar pela colua Score
  ss.sort(12, false);
};