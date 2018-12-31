function retval = rectangle_lw (n, b)

  if (nargin != 2)
    print_usage ();
  endif

  retval = zeros (n, 1);
  t = floor (1 / b);

  retval(1:t, 1) = ones (t, 1);

endfunction

function retval = lw (n)
  
  #retval = 0.5 - 0.5 * cos (2 * pi * (0 : n)' / n);

  retval = sin ( (pi / 2) * (1 - cos ( 2*((0:n)' + 0.5)/n * pi ) ) / 2 )

  #retval = sin ( (pi / 2) * sin^2((0:n)') )

endfunction

% Ventana rectangular
w0 = [ (rectangle_lw (513, 1/513)) ];

% Ventana Vorbis
w = [ lw(512) ];

todas = [w0, w];

save -ascii "window.dat" todas
