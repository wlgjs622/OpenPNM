r"""
===============================================================================
Submodule -- throat_diameter
===============================================================================

"""
import scipy as _sp

def cylinder(geometry,
             tsd_name,tsd_shape,tsd_loc,tsd_scale,
             throat_seed='throat.seed',
             **kwargs):
    r"""
    Calculate throat diameter from seeds for a cylindrical throat
    """
    import scipy.stats as spst
    prob_fn = getattr(spst,tsd_name)
    P = prob_fn(tsd_shape,loc=tsd_loc,scale=tsd_scale)
    value=P.ppf(geometry[throat_seed])
    return value
    
def cylinder_from_radius(geometry,
             tsd_name,tsd_shape,tsd_loc,tsd_scale,
             throat_seed='throat.seed',
             **kwargs):
    r"""
    Calculate throat diameter from seeds for a cylindrical throat
    """
    import scipy.stats as spst
    prob_fn = getattr(spst,tsd_name)
    P = prob_fn(tsd_shape,loc=tsd_loc,scale=tsd_scale)
    value=P.ppf(geometry[throat_seed])*2
    return value

def voronoi(network,
            throat_area='throat.area',
            **kwargs):
    r"""
    Calculate throat diameter from analysis of Voronoi facets
    Equivalent circular diameter from voronoi area
    Could do better here and work out minimum diameter from verts
    """
    throats = network.throats()
    areas = network[throat_area][throats]
    value = 2*_sp.sqrt(areas/_sp.pi)#64 bit sqrt doesn't work!
    return value