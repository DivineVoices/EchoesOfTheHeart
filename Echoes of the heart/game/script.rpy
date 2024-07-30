label start:
    python:
        mc = renpy.input("Votre nom ?", length=12)
        mc = mc.strip()
        if not mc:
            mc = "Ruan Mei"
            
    call ch0
    
    return
