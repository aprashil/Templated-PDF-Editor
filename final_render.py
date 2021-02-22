from fpdf import FPDF 

def final_render(output_dir, edited_template):
    """
    Renders the final pdf file and saves it in the output directory.
    Currently only supports single page PDF's but additional functionality
    will be added in the future.
    """

    pdf = FPDF()       
    pdf.add_page()  
    pdf.set_font("Arial", size = 11)
    for i in edited_template: 
        pdf.cell(200, 5, txt = i, ln = 2, align = 'L') 
        print(i)
    pdf.output(output_dir)

    return 1
