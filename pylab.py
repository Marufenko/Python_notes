    import pylab
    
    value = []
    function = []
    function2 = []
    
    for i in range(30):
        value.append(i)
        function.append(i**2)
        function2.append(i**3)
    
    pylab.figure('first')
    pylab.title('Quadratic')
    pylab.xlabel('values')
    pylab.ylabel('function')
    pylab.plot(value,function)
    
    pylab.figure('second')
    pylab.title('Qubic')
    pylab.xlabel('values')
    pylab.ylabel('function2')
    pylab.ylim(0,1000)               #set range
    pylab.plot(value,function2)
    
    pylab.figure('compare')
    pylab.ylim(0,3000)
    pylab.plot(value,function, 'b--', label = 'quad', linewidth = 2.0)
    pylab.plot(value,function2, 'ro', label = 'qub')
    pylab.legend(loc = 'upper left')
