"""
For adding up the delta angles in a split up curve such as a
cul-du-sac.
"""
from math import pi
def DMStoDD(DMS):
        """
        Expectes a string formatted D-M-S, returns float.
        """
	DMS = DMS.split('-')
	return (float(DMS[0]) + float(DMS[1])/60 + float(DMS[2])/3600)

def DDtoDMS(dd):
        """
        Expects a number, returns string formatted D-M-S.
        """
        is_positive = dd >= 0
        dd = abs(dd)
        minutes,seconds = divmod(dd*3600,60)
        degrees,minutes = divmod(minutes,60)
        degrees = degrees if is_positive else -degrees
        return (int(degrees),int(minutes),int(seconds))

def curveSum(radius,*deltas):
        """
        Takes either a list of delta angles formatted D-M-S or
        single string space delimited with delta angles i.e.
        'D-M-S D-M-S D-M-S' or ['D-M-S', 'D-M-S', 'D-M-S'].
        Returns total delta angle for the curve and the arc lengths
        for the segments to 3 points of precision (plats here all
        seem to round off at 2 and result in some error).
        """
        
        if len(deltas) > 1:
                pass
        elif len(deltas) == 1:
                deltas = deltas[0].split(' ')
        circumference = 2*pi*radius
        dd = sum([DMStoDD(delta) for delta in deltas])
        DMS = DDtoDMS(dd)
        return '%s-%s-%s'%(DMS[0],DMS[1],DMS[2]),\
               ' '.join([str(round((DMStoDD(delta)/360.0)* circumference,3)) for delta in deltas])
