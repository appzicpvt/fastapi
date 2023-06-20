from fastapi import APIRouter, UploadFile, Response
import io
import cairosvg

router = APIRouter(prefix="/converter", tags=["Converter"])


@router.post("/svg-to-png")
async def convert_svg_to_png(file: UploadFile):
    # Check if the uploaded file is an SVG file
    if file.content_type != "image/svg+xml":
        return {"error": "Invalid file type. Please upload an SVG file."}

    # Read SVG file content
    svg_content = await file.read()

    # Convert SVG content to byte string
    with io.BytesIO() as svg_buffer:
        svg_buffer.write(svg_content)
        svg_buffer.seek(0)

        # Convert SVG buffer to PNG buffer
        with io.BytesIO() as png_buffer:
            cairosvg.svg2png(bytestring=svg_buffer.getvalue(),
                             write_to=png_buffer)
            return Response(content=png_buffer.getvalue(), media_type="image/png")


@router.post("/svg-to-pdf")
async def convert_svg_to_pdf(file: UploadFile):
    # Check if the uploaded file is an SVG file
    if file.content_type != "image/svg+xml":
        return {"error": "Invalid file type. Please upload an SVG file."}

    # Read SVG file content
    svg_content = await file.read()

    # Convert SVG content to byte string
    with io.BytesIO() as svg_buffer:
        svg_buffer.write(svg_content)
        svg_buffer.seek(0)

        # Convert SVG buffer to PDF buffer
        with io.BytesIO() as pdf_buffer:
            cairosvg.svg2pdf(bytestring=svg_buffer.getvalue(),
                             write_to=pdf_buffer)
            return Response(content=pdf_buffer.getvalue(), media_type="application/pdf")


@router.post("/svg-to-eps")
async def convert_svg_to_eps(file: UploadFile):
    # Check if the uploaded file is an SVG file
    if file.content_type != "image/svg+xml":
        return {"error": "Invalid file type. Please upload an SVG file."}

    # Read SVG file content
    svg_content = await file.read()

    # Convert SVG content to byte string
    with io.BytesIO() as svg_buffer:
        svg_buffer.write(svg_content)
        svg_buffer.seek(0)

        # Convert SVG buffer to EPS buffer
        with io.BytesIO() as eps_buffer:
            cairosvg.svg2eps(bytestring=svg_buffer.getvalue(),
                             write_to=eps_buffer)
            return Response(content=eps_buffer.getvalue(), media_type="application/eps")
