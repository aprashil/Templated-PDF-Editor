from fpdf import FPDF 

def final_render(output_dir, edited_template):
    pdf = FPDF()       
    pdf.add_page()  
    pdf.set_font("Arial", size = 11)
    for i in edited_template: 
        #pdf.cell(50,5, txt = i, ln = 1, align = 'C') 
        pdf.cell(200, 5, txt = i, ln = 2, align = 'L') 
        print(i)
    pdf.output(output_dir)

    return 1
