# txt_to_pcm
another useless project that allows you to convert raw text to pcm (wav)
<pre>
technical details:
  one letter lenght: 0.02s = 882 samples // yes, its too much
  frequency: 8 * (char value) + 500
  possible precision loss: floor(sin()*5000) // by experimentation, its enough to decode later
 </pre>
