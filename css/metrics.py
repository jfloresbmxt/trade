'''
Function to create personalize metrics box
'''
def metrics(sline, i, iconname):
    fontsize = 28
    lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'

    htmlstr = f"""<p style='background-color: rgb(231,234,233, 0.75);
                            color:rgb(0, 0, 0, 0.9);
                            font-size: {fontsize}px;
                            border-width: 2px;
                            border-style: solid;
                            border-color: rgb(35, 91, 78);
                            border-radius: 7px;
                            padding-left: 12px; 
                            padding-top: 0px; 
                            padding-bottom: 8px;
                            line-height: 30px;'>
                            <span style='font-size: 14px;
                            margin-top: 0;
                            margin-bottom: 10px;'>{sline}</style></span>
                            <BR>
                            <i class='{iconname} fa-xs'></i> {i}
                            </style></p>"""
    
    return lnk + htmlstr