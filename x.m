total = sum(sum(S));
msum = 0;
K = 0;
for i = 1:n
    msum = msum + S(i,i);
    if(msum / total >= rate)
        K = i
        break;
    end
end
