from django.db import models

class Service(models.Model):
    VEHICLE_BRANDS = [
        ('Ford', 'Ford'),
        ('Chevrolet', 'Chevrolet'),
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Volkswagen', 'Volkswagen'),
        ('Fiat', 'Fiat'),
        ('Hyundai', 'Hyundai'),
    ]

    brand = models.CharField(max_length=50, choices=VEHICLE_BRANDS)
    model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=10)
    year = models.PositiveIntegerField()
    owner_name = models.CharField(max_length=100)
    owner_phone = models.CharField(max_length=20)
    problem_description = models.TextField()
    service_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.license_plate}"

class Part(models.Model):
    part_name = models.CharField(max_length=100, verbose_name="Nome da Peça")
    part_code = models.CharField(max_length=50, unique=True, verbose_name="Código da Peça")
    manufacturer = models.CharField(max_length=100, verbose_name="Fabricante")
    vehicle_compatibility = models.CharField(max_length=200, verbose_name="Compatibilidade com Veículos")
    quantity = models.PositiveIntegerField(verbose_name="Quantidade em Estoque")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Unitário")
    supplier = models.CharField(max_length=100, verbose_name="Fornecedor")
    purchase_date = models.DateField(verbose_name="Data de Aquisição")
    additional_info = models.TextField(blank=True, null=True, verbose_name="Informações Adicionais")

    class Meta:
        verbose_name = "Peça"
        verbose_name_plural = "Peças"
        ordering = ['part_name']

    def __str__(self):
        return f"{self.part_name} ({self.part_code})"