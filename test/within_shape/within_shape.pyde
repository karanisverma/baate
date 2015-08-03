size(300,300);

//drawRect
int w=200;
int h=40;
rect(50,50,w,h);

//setFont and String
PFont font;
font = loadFont("ArialMT-48.vlw"); 
// set the FontSize to the height of the rect
textFont(font, h); 
String s = "The quick brown fox jumped over the lazy dog";

float tS=h;
//the textSize() is shorten by 1 until the textWidth() smaller then the width of the rect
while(textWidth(s)>w){
 tS-=1;
 textSize(tS);
 println(textWidth(s));
}
fill(0);
//draw the text in the middle of the rect 
text(s,50+(w-textWidth(s))/2,50+h/2+tS/2);
