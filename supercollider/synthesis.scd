/*
Some little functions to create simple sounds...
*/
var p;
var f;
f = "disonance_001.wav";
p = thisProcess.nowExecutingPath.dirname ++ "/audio/" ++ f;
s.boot; //You need to start the SuperCollider server...
Server.local.options.outDevice = "Built-in Output"; //To decide your sound device...
s.quit; //To stop the server...
s.record(path: p, duration: 2, numChannels: 1); //Command to record the output to a file...

//Sine waves
{SinOsc.ar(440, 0, 0.9)}.play;
{SinOsc.ar(440, 0, 0.9)}.scope;

//consonance of pure tones...
{SinOsc.ar(440, 0, 0.4) + SinOsc.ar(880, 0, 0.4)}.play;
{SinOsc.ar(440, 0, 0.4) + SinOsc.ar(880, 0, 0.4)}.scope;

//dissonance of pure tones...
{SinOsc.ar(440, 0, 0.4) + SinOsc.ar(488, 0, 0.4)}.play;
{SinOsc.ar(440, 0, 0.4) + SinOsc.ar(488, 0, 0.4)}.scope;

//Simple compound sounds...
{
	SinOsc.ar(220, 0, 0.5)
	+ SinOsc.ar(440, 0, 0.3)
	+ SinOsc.ar(660, 0, 0.1)
	+ SinOsc.ar(880, 0, 0.2)
	+ SinOsc.ar(1100, 0, 0.1)
}.play;
{
	SinOsc.ar(220, 0, 0.5)
	+ SinOsc.ar(440, 0, 0.3)
	+ SinOsc.ar(660, 0, 0.1)
	+ SinOsc.ar(880, 0, 0.2)
	+ SinOsc.ar(1100, 0, 0.1)
}.scope;

//Sounds with simple mobile spectrums...
{
	SinOsc.ar(220, 0, 0.35)
	+ SinOsc.ar(440, 0, SinOsc.ar(220,0,0.25))
	+ SinOsc.ar(660, 0, 0.1)
	+ SinOsc.ar(880, 0, SinOsc.ar(220,0,0.1))
	+ SinOsc.ar(1100, 0, SinOsc.ar(220,0,0.05))
}.play;
