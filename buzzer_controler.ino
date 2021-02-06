int buzzer = 9;
float seno;
int frequencia;


char comando;
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  pinMode(buzzer,OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  comando = Serial.read();
  switch(comando){
    case 'l': // ligar para flag de fadiga 
     digitalWrite(LED_BUILTIN,HIGH);
     delay(1000);
     for(int x=0;x<180;x++){
        //converte graus para radiando e depois obtém o valor do seno
        seno=(sin(x*3.1416/180));
        //gera uma frequência a partir do valor do seno
        frequencia = 2000+(int(seno*1000));
        tone(buzzer,frequencia);
        delay(2);
     }
     digitalWrite(LED_BUILTIN,LOW);
     delay(1000);
     noTone(buzzer);
    break;

    case 'd':
      digitalWrite(LED_BUILTIN,LOW);
      noTone(buzzer);
    break;
  }                   // wait for a second
}
