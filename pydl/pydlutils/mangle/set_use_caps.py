# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
def set_use_caps(x,cm,polygon_use_caps,add=False,tol=1.0e-10,allow_doubles=False,allow_neg_doubles=False):
    """Set the bits in use_caps for a polygon.

    Parameters
    ----------
    x
    cm
    polygon_use_caps
    add
    tol
    allow_doubles
    allow_neg_doubles

    Returns
    -------

    """
    import numpy as np
    from . import is_cap_used
    if add:
        use_caps = long(polygon_use_caps)
    else:
        use_caps = 0L
    t2 = tol**2
    use_caps |= 2L**len(cm) - 1L
    if not allow_doubles:
        #
        # Check for doubles
        #
        for i in range(len(cm)):
            if is_cap_used(use_caps,i):
                for j in range(i+1,len(cm)):
                    if is_cap_used(use_caps,j):
                        if np.sum(x[i]-x[j])**2 < t2:
                            if ((np.absolute(cm[i]-cm[j]) < tol) or
                                ((cm[i] + cm[j]) < tol and not allow_neg_doubles)):
                                #
                                # Don't use
                                #
                                use_caps -= 2L**j
    return use_caps

