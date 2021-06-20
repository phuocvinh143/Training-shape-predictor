def get_max_area_rect(rects):
    if len(rects) == 0: 
        return
    areas = []
    for rect in rects:
        areas.append(rect.area())
    return rects[areas.index(max(areas))]