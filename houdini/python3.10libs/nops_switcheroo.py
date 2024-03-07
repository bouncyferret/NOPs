def Switcheroo(kwargs: dict) -> None:

    shape: str = kwargs["node"].userData("nodeshape")
    newshape: str = ""
    match shape:

        case "_wbt_helixrev":
            newshape = "_wbt_helix"
        case "_wbt_helix":
            newshape = "_wbt_helixrev"
        case "_wbt_mandelbrotB":
            newshape = "_wbt_mandelbrotrev"
        case "_wbt_mandelbrotrev":
            newshape = "_wbt_mandelbrotB"
        case _:
            newshape = shape
    
    kwargs["node"].setUserData("nodeshape",newshape)
