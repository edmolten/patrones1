function [ X ] = dataset(name, n, noise)
% Genera en X la matriz de nx3 con los datos del dataset especificado en name.
% Los datos tienen ruido igual a noise.
% name solo puede tomar valores 'swissroll', 'brokenswissroll', 'helix' o 'intersect'.
	switch name
        case 'swissroll'
            t = (3 * pi / 2) * (1 + 2 * rand(n, 1));  
            height = 30 * rand(n, 1);
            X = [t .* cos(t) height t .* sin(t)] + noise * randn(n, 3);
        case 'brokenswissroll'
            t = [(3 * pi / 2) * (1 + 2 * rand(ceil(n / 2), 1) * .4); (3 * pi / 2) * (1 + 2 * (rand(floor(n / 2), 1) * .4 + .6))];  
            height = 30 * rand(n, 1);
            X = [t .* cos(t) height t .* sin(t)] + noise * randn(n, 3);
        case 'helix'
    	    t = [1:n]' / n;
    	    t = t .^ (1.0) * 2 * pi;
            X = [(2 + cos(8 * t)) .* cos(t) (2 + cos(8 * t)) .* sin(t) sin(8 * t)] + noise * randn(n, 3);
        case 'intersect'
            t = [1:n]' ./ n .* (2 * pi);
            x = cos(t);
            y = sin(t);
            height = rand(length(x), 1) * 5;
            X = [x x .* y height] + noise * randn(n, 3);
end