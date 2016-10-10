function [ X, labels, t ] = generate_data( dataname, n, noise )
%GENERATE_DATA Generates the requested dataset. The parameter
% dataset defines which data will be generated.
% This function was taken from the Dimensionality Reduction toolbox
% developed by Laurens van der Maaten. This is a modified version of
% the original file.

    if ~exist('n', 'var')
		n = 1000;
    end
    if ~exist('noise', 'var')
        noise = 0.05;
    end

	switch dataname
        case 'swiss'
            t = (3 * pi / 2) * (1 + 2 * rand(n, 1));  
            height = 30 * rand(n, 1);
            X = [t .* cos(t) height t .* sin(t)] + noise * randn(n, 3);
            labels = uint8(t);
            t = [t height];
            
        case 'brokenswiss'
            t = [(3 * pi / 2) * (1 + 2 * rand(ceil(n / 2), 1) * .4); (3 * pi / 2) * (1 + 2 * (rand(floor(n / 2), 1) * .4 + .6))];  
            height = 30 * rand(n, 1);
            X = [t .* cos(t) height t .* sin(t)] + noise * randn(n, 3);
            labels = uint8(t);
            t = [t height];
            
        case 'helix'
    	    t = [1:n]' / n;
    	    t = t .^ (1.0) * 2 * pi;
            X = [(2 + cos(8 * t)) .* cos(t) (2 + cos(8 * t)) .* sin(t) sin(8 * t)] + noise * randn(n, 3);
    	    labels = uint8(t);
            
        case 'intersect'
            t = [1:n]' ./ n .* (2 * pi);
            x = cos(t);
            y = sin(t);
            height = rand(length(x), 1) * 5;
            X = [x x .* y height] + noise * randn(n, 3);
            labels = uint8(5 * t);
            
        otherwise
            error('Unknown dataset name.');

end