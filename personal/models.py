from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone


class Styles(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Types(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('RestaurantProfile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('FoodOrdering:edit_categories', kwargs={'pk': self.pk})


class Allergen(models.Model):
    allergen = models.CharField(max_length=50)

    def __str__(self):
        return self.allergen


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class CustomerProfile(Profile):
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)


class CourierProfile(Profile):
    divident = models.IntegerField
    phone_number = models.CharField(max_length=10)
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()


class RestaurantProfile(Profile):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    style = models.ForeignKey('Styles', on_delete=models.CASCADE, blank=True, null=True)
    open_from = models.TimeField(max_length=50)
    open_to = models.TimeField(max_length=50)

    def is_open(self, time=timezone.now().time()):
        return self.open_from < time < self.open_to


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    type = models.ForeignKey('Types', on_delete=models.CASCADE)
    style = models.ForeignKey('Styles', on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()
    restaurant = models.ForeignKey('RestaurantProfile', on_delete=models.CASCADE)
    discount_price = models.IntegerField(blank=True, null=True)
    discount_start_date = models.DateField(blank=True, null=True)
    discount_end_date = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to='dishes/')
    allergen = models.ManyToManyField('Allergen', blank=True)

    available_from = models.DateTimeField(null=True, blank=True)
    available_to = models.DateTimeField(null=True, blank=True)

    def get_price(self):
        if self.discount_price is None:
            return self.price
        now = timezone.datetime.date(timezone.now())
        # Akciós időszak
        if self.discount_start_date < now < self.discount_end_date:
            return self.discount_price
        return self.price

    def is_orderable(self, date_time=timezone.now()):
        if self.available_from is None and self.available_to is None:
            return True
        if self.available_from is not None and self.available_to is None:
            return self.available_from < date_time
        if self.available_from is None and self.available_to is not None:
            return date_time < self.available_to
        return self.available_from < date_time < self.available_to

    def __str__(self):
        return self.name


class DishToCart(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class Cart(models.Model):
    class MultipleRestaurantInCartError(Exception):
        pass

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)
    session = models.CharField(max_length=254, null=True, blank=True)
    items = models.ManyToManyField(Dish, blank=True, through=DishToCart)
    is_ordered = models.BooleanField(default=False)

    restaurant = models.ForeignKey('RestaurantProfile', on_delete=models.SET_NULL, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.user is None and self.session is None:
            raise ValueError('Cart must have a user or a session!')
        super().save(force_insert, force_update, using, update_fields)

    def add_dish(self, dish: Dish, quantity=1):
        if self.pk is None:
            raise ValueError('Cart must be saved before adding items to it!')

        if self.restaurant is None:
            self.restaurant = dish.restaurant
            self.save()

        if self.restaurant != dish.restaurant:
            raise Cart.MultipleRestaurantInCartError()

        if quantity is None:
            quantity = 1

        cart_o, created = DishToCart.objects.get_or_create(cart=self, dish=dish)
        cart_o.quantity += quantity
        cart_o.save()

    def set_ordered(self):
        self.is_ordered = True
        self.save()

    @staticmethod
    def get_cart(user=None, session=None):
        if (user is None or not user.is_authenticated) and session is None:
            raise ValueError('User or session must be provided to get a cart')

        if user.is_authenticated:
            try:
                cart = Cart.objects.exclude(is_ordered=True).prefetch_related('items').get(user=user)
            except Cart.DoesNotExist:
                cart = Cart(user=user)
        else:
            try:
                cart = Cart.objects.exclude(is_ordered=True).prefetch_related('items').get(session=session)
            except Cart.DoesNotExist:
                cart = Cart(session=session)
        if cart.pk is None:
            cart.save()

        return cart


class OrderStatus(models.Choices):
    Ordered = 1
    UnderDelivery = 2
    Delivered = 3


class Order(models.Model):
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=OrderStatus.choices, default=1)
    amount = models.FloatField(default=0)


class Payments(models.Model):
    courier = models.ForeignKey(CourierProfile, on_delete=models.CASCADE)
    money = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
