from prac_08.taxi import Taxi


def main():
    """Test Taxi class."""
    my_taxi = Taxi("Prius 1", 100, Taxi.price_per_km)
    my_taxi.drive(10)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    my_taxi.get_fare()
    print(my_taxi)


main()