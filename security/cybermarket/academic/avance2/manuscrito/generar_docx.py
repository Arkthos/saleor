"""Generate the public academic manuscript; optional authors stay in private configuration.

Run with the Codex primary runtime Python (python-docx dependency).
"""

import argparse
import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION_START
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


def field(p, name):
    r = p.add_run()
    x = OxmlElement("w:fldSimple")
    x.set(qn("w:instr"), name)
    r._r.addnext(x)


def columns(section, n):
    cols = section._sectPr.find(qn("w:cols"))
    cols.set(qn("w:num"), str(n))
    cols.set(qn("w:space"), "360")


def text(p, s):
    # Break long code paths and URLs at natural separators without changing the source.
    for segment in re.split(r"(`[^`]+`|\*\*[^*]+\*\*)", s):
        bold = segment.startswith("**")
        code = segment.startswith("`")
        segment = segment.strip("`") if code else segment[2:-2] if bold else segment
        segment = re.sub(r"(?<=[/_])(?=\S)", "\u200b", segment)
        r = p.add_run(segment)
        r.bold = bold
        if code:
            r.font.name = "Courier New"
            r.font.size = Pt(8.5)


def table(doc, rows):
    n = len(rows[0])
    t = doc.add_table(rows=1, cols=n)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    widths = {2: [1.25, 5.85], 3: [0.85, 5.3, 0.95], 4: [0.78, 2.05, 1.15, 3.12]}[n]
    for c, w in zip(t.columns, widths, strict=False):
        c.width = Inches(w)
    for idx, vals in enumerate(rows):
        cells = t.rows[0].cells if idx == 0 else t.add_row().cells
        for j, (c, v) in enumerate(zip(cells, vals, strict=False)):
            c.width = Inches(widths[j])
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            tcpr = c._tc.get_or_add_tcPr()
            mar = OxmlElement("w:tcMar")
            for side in ["top", "left", "bottom", "right"]:
                el = OxmlElement("w:" + side)
                el.set(qn("w:w"), "65")
                el.set(qn("w:type"), "dxa")
                mar.append(el)
            tcpr.append(mar)
            borders = OxmlElement("w:tcBorders")
            for side in ["top", "left", "bottom", "right"]:
                el = OxmlElement("w:" + side)
                el.set(qn("w:val"), "single")
                el.set(qn("w:sz"), "4")
                el.set(qn("w:color"), "D9D9D9")
                borders.append(el)
            tcpr.append(borders)
            p = c.paragraphs[0]
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.02
            text(p, v)
            for r in p.runs:
                r.font.size = Pt(9.5)
                r.bold = idx == 0
            if j == 0 or n == 3 and j == 2:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if idx == 0:
                sh = OxmlElement("w:shd")
                sh.set(qn("w:fill"), "E7E7E7")
                tcpr.append(sh)
        trpr = t.rows[idx]._tr.get_or_add_trPr()
        nosplit = OxmlElement("w:cantSplit")
        trpr.append(nosplit)
        if idx == 0:
            trpr.append(OxmlElement("w:tblHeader"))
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--source", type=Path, default=Path(__file__).with_name("INFORME_AVANCE2.md")
    )
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--authors-file", type=Path)
    args = ap.parse_args()
    lines = args.source.read_text().splitlines()
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Inches(8.5)
    sec.page_height = Inches(11)
    sec.top_margin = sec.bottom_margin = Inches(0.7)
    sec.left_margin = sec.right_margin = Inches(0.7)
    sec.footer_distance = Inches(0.3)
    styles = doc.styles
    for st in styles:
        for node in st.element.xpath(".//w:pBdr"):
            node.getparent().remove(node)
        for fonts in st.element.xpath(".//w:rFonts"):
            for key in list(fonts.attrib):
                if "theme" in key.lower():
                    del fonts.attrib[key]
    for name in ["Normal", "Title", "Subtitle", "Heading 1", "Heading 2", "Heading 3"]:
        s = styles[name]
        s.font.name = "Times New Roman"
        s.font.color.rgb = RGBColor(0, 0, 0)
    normal = styles["Normal"]
    normal.font.size = Pt(10.25)
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.line_spacing = 1.0
    normal.paragraph_format.widow_control = True
    styles["Title"].font.size = Pt(18)
    styles["Title"].paragraph_format.space_after = Pt(7)
    styles["Subtitle"].font.size = Pt(12)
    for name, size in [("Heading 1", 12), ("Heading 2", 10.5)]:
        s = styles[name]
        s.font.size = Pt(size)
        s.font.bold = True
        s.paragraph_format.space_before = Pt(9)
        s.paragraph_format.space_after = Pt(4)
        s.paragraph_format.keep_with_next = True
    p = doc.add_paragraph(lines[0][2:], style="Title")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph(
        "Segundo avance del proyecto CyberMarket CR", style="Subtitle"
    )
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    authors = (
        args.authors_file.read_text().strip()
        if args.authors_file
        else "Equipo CyberMarket CR"
    )
    for s in [
        authors,
        "Universidad Fidélitas · CY-703 Seguridad de Software",
        "Preparado el 2 de noviembre de 2026",
    ]:
        p = doc.add_paragraph(s)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(4)
    footer = sec.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    field(footer, "PAGE")
    body = False
    annex = False
    i = 4
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            continue
        if line == "Segundo avance del proyecto CyberMarket CR":
            continue
        if line.startswith("## I Continuidad") and not body:
            sec = doc.add_section(WD_SECTION_START.CONTINUOUS)
            columns(sec, 2)
            body = True
        if line == "## Referencias":
            sec = doc.add_section(WD_SECTION_START.NEW_PAGE)
            columns(sec, 1)
        if line.startswith(("## Anexo C ", "## Anexo D ")):
            doc.add_page_break()
        if line.startswith("## Anexo ") and not annex:
            sec = doc.add_section(WD_SECTION_START.NEW_PAGE)
            columns(sec, 1)
            annex = True
        if line.startswith("|"):
            rows = []
            while True:
                vals = [x.strip() for x in line.strip("|").split("|")]
                if not all(re.fullmatch(r"[-: ]+", x) for x in vals):
                    rows.append(vals)
                if i >= len(lines) or not lines[i].strip().startswith("|"):
                    break
                line = lines[i].strip()
                i += 1
            table(doc, rows)
            continue
        if line.startswith("```"):
            while i < len(lines) and not lines[i].startswith("```"):
                p = doc.add_paragraph()
                p.paragraph_format.space_after = Pt(0)
                r = p.add_run(lines[i])
                r.font.name = "Courier New"
                r.font.size = Pt(9)
                i += 1
            i += 1
            continue
        if line.startswith("### "):
            doc.add_paragraph(line[4:], style="Heading 2")
            continue
        if line.startswith("## "):
            doc.add_paragraph(line[3:], style="Heading 1")
            continue
        p = doc.add_paragraph()
        text(p, line)
        if body and not annex:
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if re.match(r"^\[\d+\]", line):
            p.paragraph_format.left_indent = Inches(0.18)
            p.paragraph_format.first_line_indent = Inches(-0.18)
            for r in p.runs:
                r.font.size = Pt(10.5)
    doc.core_properties.title = (
        "Análisis del diseño seguro de autenticación y autorización en Saleor"
    )
    doc.core_properties.author = "Equipo CyberMarket CR"
    doc.core_properties.subject = "Segundo avance CY-703"
    args.out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(args.out)


if __name__ == "__main__":
    main()
