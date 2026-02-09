from products.models import Product, Category

print("=" * 60)
print("🚀 BULK PRODUCT IMPORT SCRIPT")
print("=" * 60)

# ============================================
# CREATE CATEGORIES
# ============================================
print("\n📁 Creating categories...")
categories_to_create = [
    ('3d_tattoos', '3D Tattoos'),
    ('traditional_tattoos', 'Traditional Tattoos'),
    ('piercings', 'Piercings'),
    ('sleeve_tattoos', 'Sleeve Tattoos'),
    ('activewear', 'Activewear'),
]

for name, friendly in categories_to_create:
    cat, created = Category.objects.get_or_create(
        name=name,
        defaults={'friendly_name': friendly}
    )
    if created:
        print(f"  ✅ Created: {friendly}")
    else:
        print(f"  ℹ️  Already exists: {friendly}")

# ============================================
# PRODUCT DATA
# ============================================
print("\n📦 Creating products...")

products_data = [
    # 3D TATTOOS
    {
        'category': '3d_tattoos',
        'sku': '3D-001',
        'name': '3D Dragon Tattoo Design',
        'description': 'Stunning 3D dragon tattoo design with incredible depth and detail. Perfect for arm or back placement.',
        'price': 1500.00,
        'image': '1599676534_A0ADA70C-3B3E-47C9-B2D3-A57D683A9C62.jpeg'
    },
    {
        'category': '3d_tattoos',
        'sku': '3D-002',
        'name': '3D Skull Tattoo for Men',
        'description': 'Bold 3D skull tattoo design with realistic shading and detail. Makes a powerful statement.',
        'price': 1800.00,
        'image': '3d-skull-tattoo-for-men-stylendesigns.jpg'
    },
    {
        'category': '3d_tattoos',
        'sku': '3D-003',
        'name': '3D Tattoo Collection Part 1',
        'description': 'Amazing collection of 3D tattoo designs featuring optical illusions and depth.',
        'price': 1200.00,
        'image': '3d-tattoos-pt_-1.jpg'
    },
    {
        'category': '3d_tattoos',
        'sku': '3D-004',
        'name': 'Amazing 3D Tattoo Designs',
        'description': '70 amazing 3D tattoo design concepts. Cutting-edge tattoo artistry.',
        'price': 1600.00,
        'image': '70-amazing-3d-tattoo-designs-cuded.jpg'
    },
    {
        'category': '3d_tattoos',
        'sku': '3D-005',
        'name': 'Best 3D Spider Tattoo',
        'description': 'Incredibly realistic 3D spider tattoo that looks like it\'s crawling on your skin.',
        'price': 1400.00,
        'image': 'best-spider-tattoo-idea 3d.jpg'
    },
    {
        'category': '3d_tattoos',
        'sku': '3D-006',
        'name': '3D Portrait Tattoo Design',
        'description': 'Beautiful 3D face portrait tattoo with stunning realism and detail.',
        'price': 2000.00,
        'image': 'face-beautiful-girl-tattoo.jpg'
    },
    {
        'category': '3d_tattoos',
        'sku': '3D-007',
        'name': '3D Artistic Tattoo',
        'description': 'Unique 3D tattoo design combining realism with artistic flair.',
        'price': 1700.00,
        'image': 'ca97346b85829f98374169f758db41d9.jpg'
    },
    
    # SLEEVE TATTOOS
    {
        'category': 'sleeve_tattoos',
        'sku': 'SLEEVE-001',
        'name': 'Best Sleeve Tattoo Ideas',
        'description': 'Complete sleeve tattoo design with intricate details and flowing composition.',
        'price': 3500.00,
        'image': 'sleeve-tattoos-for-men--best-sleeve-tattoo-ideas-and-designs.jpg'
    },
    {
        'category': 'sleeve_tattoos',
        'sku': 'SLEEVE-002',
        'name': 'Premium Sleeve Tattoo Design',
        'description': 'Full sleeve tattoo design featuring elaborate patterns and storytelling elements.',
        'price': 3800.00,
        'image': 'sleeve-tattoos-for-men-–-best-sleeve-tattoo-ideas-and-designs.jpg'
    },
    
    # TRADITIONAL/TEXT TATTOOS
    {
        'category': 'traditional_tattoos',
        'sku': 'TRAD-001',
        'name': 'Words and Phrases Tattoo',
        'description': 'Elegant typography and meaningful words tattoo designs. Express yourself through text.',
        'price': 800.00,
        'image': 'Words-and-Phrases-Tattoos-1-1024x1024.jpg'
    },
    
    # PIERCINGS
    {
        'category': 'piercings',
        'sku': 'PIER-001',
        'name': 'Surface Piercing',
        'description': 'Professional surface piercing service. Modern and stylish body modification.',
        'price': 600.00,
        'image': 'Oberflaechenpiercing_IMGP8092-2.jpg'
    },
    
    # ARTISTIC/LIFESTYLE IMAGES (Can be used for shop ambiance/apparel)
    {
        'category': 'activewear',
        'sku': 'AMB-001',
        'name': 'Tattoo Studio Lifestyle',
        'description': 'Premium tattoo studio experience. Professional artists and clean environment.',
        'price': 0.00,  # Display item
        'image': 'alicia-petresc-BciCcl8tjVU-unsplash.jpg'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-002',
        'name': 'Tattoo Artist at Work',
        'description': 'Behind the scenes of professional tattoo artistry.',
        'price': 0.00,
        'image': 'anomaly-WWesmHEgXDs-unsplash.jpg'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-003',
        'name': 'Tattoo Culture',
        'description': 'Experience the art and culture of modern tattooing.',
        'price': 0.00,
        'image': 'christian-bolt-VW5VjskNXZ8-unsplash.jpg'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-004',
        'name': 'Tattoo Studio Atmosphere',
        'description': 'Step into our professional tattoo studio.',
        'price': 0.00,
        'image': 'faith-yarn-Wr0TpKqf26s-unsplash.jpg'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-005',
        'name': 'Artist Portfolio',
        'description': 'Browse our artists\' incredible portfolio.',
        'price': 0.00,
        'image': 'garin-chadwick-WJ4268yaPyQ-unsplash.jpg'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-006',
        'name': 'Tattoo Equipment',
        'description': 'Professional-grade tattoo equipment and supplies.',
        'price': 0.00,
        'image': 'kilian-seiler-ZMYkPSNrb8I-unsplash.jpg'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-007',
        'name': 'Studio Environment',
        'description': 'Clean, professional tattoo studio environment.',
        'price': 0.00,
        'image': 'lautaro-andreani-6FaY0OJmYG4-unsplash.jpg'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-008',
        'name': 'Tattoo Lifestyle',
        'description': 'Embrace the tattoo lifestyle and culture.',
        'price': 0.00,
        'image': 'matheus-ferrero-RBsrv4yV5KY-unsplash.jpg'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-009',
        'name': 'Artist at Work',
        'description': 'Watch our skilled artists create masterpieces.',
        'price': 0.00,
        'image': 'miguel-bruna-z_ogAl0oWb4-unsplash.jpg'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-010',
        'name': 'Tattoo Session',
        'description': 'Professional tattoo session in progress.',
        'price': 0.00,
        'image': 'philipp-lansing-REOoETloFqE-unsplash.jpg'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-011',
        'name': 'Tattoo Care',
        'description': 'Professional tattoo aftercare and maintenance.',
        'price': 0.00,
        'image': 'stories-ink-tattoo-care-kZuIc5Jtmfc-unsplash.jpg'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-012',
        'name': 'Master Tattoo Artist',
        'description': 'Meet our master tattoo artists from Sankt Petersburg.',
        'price': 0.00,
        'image': 'tatu-master-andrej-popov-g_-sankt-peterburg-rossiya.png'
    },
    {
        'category': 'activewear',
        'sku': 'AMB-013',
        'name': 'Tattoo Gallery',
        'description': 'Browse our extensive tattoo design gallery.',
        'price': 0.00,
        'image': 'yoal-desurmont-NscHnjdTOsE-unsplash.jpg'
    },
]

# ============================================
# CREATE PRODUCTS
# ============================================
created_count = 0
error_count = 0

for data in products_data:
    try:
        # Check if SKU already exists
        if Product.objects.filter(sku=data['sku']).exists():
            print(f"  ⚠️  Skipped (exists): {data['sku']} - {data['name']}")
            continue
        
        category = Category.objects.get(name=data['category'])
        
        product = Product.objects.create(
            category=category,
            sku=data['sku'],
            name=data['name'],
            description=data['description'],
            price=data['price'],
            image=data['image']
        )
        
        print(f"  ✅ {product.sku}: {product.name}")
        created_count += 1
        
    except Category.DoesNotExist:
        print(f"  ❌ Category not found for: {data['sku']}")
        error_count += 1
    except Exception as e:
        print(f"  ❌ Error with {data.get('sku', 'unknown')}: {e}")
        error_count += 1

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 60)
print("📊 IMPORT SUMMARY")
print("=" * 60)
print(f"✅ Successfully created: {created_count} products")
print(f"❌ Errors: {error_count}")
print(f"📦 Total products in database: {Product.objects.count()}")
print(f"\n🔗 View your products at:")
print(f"   https://swahili-bob-tattoo.onrender.com/products/")
print("=" * 60)
