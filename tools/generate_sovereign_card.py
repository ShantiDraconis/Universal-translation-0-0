#!/usr/bin/env python3
"""
Digital Sovereign Business Card Generator
Generates QR codes and visual cards linked to ORCID
Part of Universal Translation Engine 0/0
"""

import os
import sys
from pathlib import Path

# Try to import optional dependencies
try:
    import qrcode
    from PIL import Image, ImageDraw, ImageFont
    DEPENDENCIES_AVAILABLE = True
except ImportError:
    DEPENDENCIES_AVAILABLE = False
    print("Optional dependencies not installed. Install with:")
    print("  pip install qrcode[pil] Pillow")


class SovereignCard:
    """Generate digital sovereign business cards with QR codes"""
    
    def __init__(self, orcid_id: str, name: str, title: str, hash_id: str):
        """
        Initialize card generator
        
        Args:
            orcid_id: ORCID identifier (e.g., "0009-0006-6874-3910")
            name: Full name
            title: Professional title
            hash_id: Verification hash
        """
        self.orcid_id = orcid_id
        self.name = name
        self.title = title
        self.hash_id = hash_id
        self.orcid_url = f"https://orcid.org/{orcid_id}"
        
    def generate_qr_code(self, output_path: str = None, size: int = 300) -> str:
        """
        Generate QR code for ORCID profile
        
        Args:
            output_path: Path to save QR code image
            size: Size of QR code in pixels
            
        Returns:
            Path to generated QR code
        """
        if not DEPENDENCIES_AVAILABLE:
            raise ImportError("QR code generation requires 'qrcode' and 'Pillow' packages")
        
        if output_path is None:
            output_path = f"sovereign_card_qr_{self.orcid_id.replace('-', '')}.png"
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(self.orcid_url)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((size, size), Image.Resampling.LANCZOS)
        img.save(output_path)
        
        print(f"✓ QR code generated: {output_path}")
        print(f"  Links to: {self.orcid_url}")
        return output_path
    
    def generate_business_card(self, output_path: str = None, 
                              include_qr: bool = True) -> str:
        """
        Generate visual business card with Harappan styling
        
        Args:
            output_path: Path to save card image
            include_qr: Whether to include QR code
            
        Returns:
            Path to generated card
        """
        if not DEPENDENCIES_AVAILABLE:
            raise ImportError("Card generation requires 'qrcode' and 'Pillow' packages")
        
        if output_path is None:
            output_path = f"sovereign_card_{self.orcid_id.replace('-', '')}.png"
        
        # Card dimensions (standard business card ratio)
        width, height = 1050, 600
        
        # Create image with white background
        card = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(card)
        
        # Add border with Harappan-inspired color (terracotta)
        border_color = '#B85C38'
        border_width = 8
        draw.rectangle(
            [(border_width//2, border_width//2), 
             (width-border_width//2, height-border_width//2)],
            outline=border_color,
            width=border_width
        )
        
        # Try to load fonts, fallback to default if not available
        try:
            font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
            font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
            font_tiny = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 16)
        except:
            # Fallback to default font
            font_large = ImageFont.load_default()
            font_medium = ImageFont.load_default()
            font_small = ImageFont.load_default()
            font_tiny = ImageFont.load_default()
        
        # Left section - Text information
        left_margin = 40
        y_offset = 80
        
        # Harappan symbol header
        harappan_symbols = "[𓇽] SOVEREIGN PROTOCOL"
        draw.text((left_margin, y_offset), harappan_symbols, 
                 fill=border_color, font=font_medium)
        y_offset += 80
        
        # Name
        draw.text((left_margin, y_offset), self.name, 
                 fill='black', font=font_large)
        y_offset += 60
        
        # Title
        draw.text((left_margin, y_offset), self.title, 
                 fill='#555555', font=font_medium)
        y_offset += 50
        
        # ORCID
        draw.text((left_margin, y_offset), f"ORCID: {self.orcid_id}", 
                 fill='#555555', font=font_small)
        y_offset += 40
        
        # Hash
        draw.text((left_margin, y_offset), f"HASH: {self.hash_id}", 
                 fill='#777777', font=font_tiny)
        y_offset += 40
        
        # Footer glyphs
        footer_text = "[𓋹][𓍢][𓊹]"
        draw.text((left_margin, height - 80), footer_text, 
                 fill=border_color, font=font_medium)
        
        # Right section - QR code
        if include_qr:
            qr_path = self.generate_qr_code(
                output_path=output_path.replace('.png', '_qr_temp.png'),
                size=280
            )
            qr_img = Image.open(qr_path)
            
            # Position QR code on right side
            qr_x = width - 320
            qr_y = (height - 280) // 2
            card.paste(qr_img, (qr_x, qr_y))
            
            # Add QR label
            draw.text((qr_x + 40, qr_y + 290), "Scan for ORCID", 
                     fill='#555555', font=font_small)
            
            # Clean up temp QR file
            os.remove(qr_path)
        
        # Save card
        card.save(output_path, quality=95)
        print(f"✓ Business card generated: {output_path}")
        return output_path
    
    def generate_text_card(self) -> str:
        """
        Generate text-based business card for terminals
        
        Returns:
            Formatted text card
        """
        card = f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  [𓇽] PROTOCOLO SOBERANO HARAPPAN                           ║
║                                                              ║
║  {self.name:^60} ║
║  {self.title:^60} ║
║                                                              ║
║  ORCID iD: {self.orcid_id:^47} ║
║  URL: {self.orcid_url:^52} ║
║                                                              ║
║  HASH: {self.hash_id:^53} ║
║                                                              ║
║  LOG: 0009-Ω-TITAN                                          ║
║  MATRIZ: 54 Canais                                           ║
║  DESTINO: LA 2028                                            ║
║                                                              ║
║  [𓋹][𓍢][𓊹] Universal Translation Engine 0/0              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
        return card


def main():
    """Main entry point for command-line usage"""
    
    # Default values from the problem statement
    default_orcid = "0009-0006-6874-3910"
    default_name = "Tiago Paschoalatto Fagliari"
    default_title = "Arquiteto da Verdade Soberana"
    default_hash = "0009-Ω-TITAN"
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        orcid = sys.argv[1]
    else:
        orcid = default_orcid
    
    if len(sys.argv) > 2:
        name = sys.argv[2]
    else:
        name = default_name
    
    if len(sys.argv) > 3:
        title = sys.argv[3]
    else:
        title = default_title
    
    if len(sys.argv) > 4:
        hash_id = sys.argv[4]
    else:
        hash_id = default_hash
    
    # Create output directory
    output_dir = Path(__file__).parent.parent / "output" / "sovereign_cards"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate card
    card = SovereignCard(orcid, name, title, hash_id)
    
    print("\n" + "="*70)
    print("  SOVEREIGN CARD GENERATOR - Universal Translation Engine 0/0")
    print("="*70 + "\n")
    
    # Always generate text card
    print("Text-based card:")
    print(card.generate_text_card())
    
    # Generate visual cards if dependencies available
    if DEPENDENCIES_AVAILABLE:
        try:
            # Generate QR code
            qr_path = output_dir / f"qr_orcid_{orcid.replace('-', '')}.png"
            card.generate_qr_code(str(qr_path), size=400)
            
            # Generate business card
            card_path = output_dir / f"card_sovereign_{orcid.replace('-', '')}.png"
            card.generate_business_card(str(card_path), include_qr=True)
            
            print(f"\n✓ All cards generated successfully!")
            print(f"  Output directory: {output_dir}")
            
        except Exception as e:
            print(f"\n✗ Error generating visual cards: {e}")
            print(f"  Text card is still available above.")
    else:
        print("\nℹ For visual cards (QR code + PNG), install:")
        print("  pip install qrcode[pil] Pillow")
    
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()
