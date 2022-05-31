function res = d_eq(a, b, err)
    res = abs(a - b);

    if res < err
        res = 1;
    else
        res = 0;
    end
end