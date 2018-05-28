function retval = lw (n)

  retval = sin ( (pi / 2) * (1 - cos ( 2*((0:n)' + 0.5)/n * pi ) ) / 2 )

endfunction

w = [ lw(512) ];

function retval = rectangle_lw (n, b)

  if (nargin != 2)
    print_usage ();
  endif

  retval = zeros (n, 1);
  t = floor (1 / b);

  retval(1:t, 1) = ones (t, 1);

endfunction

% Ventana rectangular
w0 = [ zeros(1000,1); rectangle_lw(20, 1/20); zeros(1000,1) ];
W = fft(w0);
r = real(W);
i = imag(W);
spectrumH0 = log(1+sqrt((r .* r) + (i .* i)));

% Ventana Vorbis
w1 = [ zeros(1000,1); lw(19); zeros(1000,1) ];
W = fft(w1);
r = real(W);
i = imag(W);
spectrumH1 = log(1+sqrt((r .* r) + (i .* i)));

todo = [spectrumH0, spectrumH1];

save -ascii "window_spectrum.dat" todo

%__gnuplot_set__ terminal fig color textspecial
%__gnuplot_set__ noxtics
%__gnuplot_set__ noytics
%__gnuplot_set__ xlabel "w"
%__gnuplot_set__ ylabel "Spectrum"
%__gnuplot_set__ output "window_spectrum.fig"
%__gnuplot_plot__ [0:500] (spectrumH0) title "Rectangular", (spectrumH1) title "sin(pi/2 ∗ sin^2((x + 0.5)∕n ∗ pi))"
