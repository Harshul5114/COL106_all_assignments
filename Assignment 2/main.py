from gcms import GCMS
from object import Color
from exceptions import NoBinFoundException

def print_separator():
    print("\n" + "-"*80 + "\n")

if __name__ == "__main__":
    # Initialize GCMS
    gcms = GCMS()
    
    # Adding an initial set of bins with varying capacities
    initial_bin_data = [
        (1001, 100), (1002, 75), (1003, 120), (1004, 80), (1005, 90),
        (1006, 110), (1007, 85), (1008, 95), (1009, 70), (1010, 130),
        (1011, 115), (1012, 105), (1013, 125), (1014, 65), (1015, 135)
    ]
    
    print("Adding Initial Bins:")
    for bin_id, capacity in initial_bin_data:
        gcms.add_bin(bin_id, capacity)
        print(f"Added Bin ID: {bin_id}, Capacity: {capacity}")
    
    print_separator()
    
    # Adding an initial set of objects with varying sizes and colors
    initial_object_data = [
        (2001, 30, Color.RED), (2002, 25, Color.YELLOW), (2003, 20, Color.BLUE),
        (2004, 35, Color.GREEN), (2005, 40, Color.RED), (2006, 15, Color.YELLOW),
        (2007, 18, Color.BLUE), (2008, 32, Color.GREEN), (2009, 45, Color.BLUE),
        (2010, 50, Color.RED), (2011, 22, Color.YELLOW), (2012, 28, Color.GREEN),
        (2013, 17, Color.BLUE), (2014, 38, Color.RED), (2015, 26, Color.YELLOW),
        (2016, 33, Color.GREEN), (2017, 19, Color.BLUE), (2018, 42, Color.RED),
        (2019, 23, Color.YELLOW), (2020, 36, Color.GREEN)
    ]
    
    print("Adding Initial Objects:")
    for obj_id, size, color in initial_object_data:
        try:
            gcms.add_object(obj_id, size, color)
            print(f"Added Object ID: {obj_id}, Size: {size}, Color: {color.name}")
        except NoBinFoundException:
            print(f"Failed to add Object ID: {obj_id}, Size: {size}, Color: {color.name} - No suitable bin found")
    
    print_separator()
    
    # Displaying bin information after initial additions
    print("Bin Information After Adding Initial Objects:")
    for bin_id, _ in initial_bin_data:
        try:
            remaining_capacity, objects_in_bin = gcms.bin_info(bin_id)
            print(f"Bin ID: {bin_id}, Remaining Capacity: {remaining_capacity}, Objects: {objects_in_bin}")
        except Exception as e:
            print(f"Error retrieving info for Bin ID: {bin_id} - {str(e)}")
    
    print_separator()
    
    # Displaying object information after initial additions
    print("Object Information After Adding Initial Objects:")
    for obj_id, _, _ in initial_object_data:
        try:
            assigned_bin = gcms.object_info(obj_id)
            print(f"Object ID: {obj_id} is assigned to Bin ID: {assigned_bin}")
        except Exception as e:
            print(f"Error retrieving info for Object ID: {obj_id} - {str(e)}")
    
    print_separator()
    
    # Adding additional bins after some objects have been placed
    additional_bin_data = [
        (1016, 140), (1017, 95), (1018, 110), (1019, 120), (1020, 85)
    ]
    
    print("Adding Additional Bins:")
    for bin_id, capacity in additional_bin_data:
        gcms.add_bin(bin_id, capacity)
        print(f"Added Bin ID: {bin_id}, Capacity: {capacity}")
    
    print_separator()
    
    # Adding additional objects after new bins have been added
    additional_object_data = [
        (2021, 35, Color.GREEN), (2022, 24, Color.YELLOW), (2023, 19, Color.BLUE),
        (2024, 60, Color.RED), (2025, 43, Color.YELLOW), (2026, 22, Color.GREEN),
        (2027, 17, Color.BLUE), (2028, 29, Color.RED), (2029, 38, Color.YELLOW),
        (2030, 21, Color.BLUE), (2031, 47, Color.GREEN), (2032, 31, Color.RED),
        (2033, 26, Color.YELLOW), (2034, 16, Color.BLUE), (2035, 39, Color.GREEN)
    ]
    
    print("Adding Additional Objects:")
    for obj_id, size, color in additional_object_data:
        try:
            gcms.add_object(obj_id, size, color)
            print(f"Added Object ID: {obj_id}, Size: {size}, Color: {color.name}")
        except NoBinFoundException:
            print(f"Failed to add Object ID: {obj_id}, Size: {size}, Color: {color.name} - No suitable bin found")
    
    print_separator()
    
    # Displaying bin information after adding additional objects
    print("Bin Information After Adding Additional Objects:")
    for bin_id, _ in initial_bin_data + additional_bin_data:
        try:
            remaining_capacity, objects_in_bin = gcms.bin_info(bin_id)
            print(f"Bin ID: {bin_id}, Remaining Capacity: {remaining_capacity}, Objects: {objects_in_bin}")
        except Exception as e:
            print(f"Error retrieving info for Bin ID: {bin_id} - {str(e)}")
    
    print_separator()
    
    # Displaying object information after adding additional objects
    print("Object Information After Adding Additional Objects:")
    for obj_id, _, _ in initial_object_data + additional_object_data:
        try:
            assigned_bin = gcms.object_info(obj_id)
            print(f"Object ID: {obj_id} is assigned to Bin ID: {assigned_bin}")
        except Exception as e:
            print(f"Object ID: {obj_id} has been deleted or does not exist - {str(e)}")
    
    print_separator()
    
    # Deleting some objects
    objects_to_delete = [2003, 2005, 2010, 2015, 2018, 2019, 2022, 2025, 2028, 2031]
    print("Deleting Objects:")
    for obj_id in objects_to_delete:
        try:
            gcms.delete_object(obj_id)
            print(f"Deleted Object ID: {obj_id}")
        except Exception as e:
            print(f"Failed to delete Object ID: {obj_id} - {str(e)}")
    
    print_separator()
    
    # Displaying bin information after deletions
    print("Bin Information After Deleting Objects:")
    for bin_id, _ in initial_bin_data + additional_bin_data:
        try:
            remaining_capacity, objects_in_bin = gcms.bin_info(bin_id)
            print(f"Bin ID: {bin_id}, Remaining Capacity: {remaining_capacity}, Objects: {objects_in_bin}")
        except Exception as e:
            print(f"Error retrieving info for Bin ID: {bin_id} - {str(e)}")
    
    print_separator()
    
    # Displaying object information after deletions
    print("Object Information After Deleting Objects:")
    current_items = initial_object_data + additional_object_data
    current_items = [elt for elt in current_items if elt[0] not in objects_to_delete]
    for obj_id, _, _ in current_items:
        try:
            assigned_bin = gcms.object_info(obj_id)
            print(f"Object ID: {obj_id} is assigned to Bin ID: {assigned_bin}")
        except Exception as e:
            print(f"Object ID: {obj_id} has been deleted or does not exist - {str(e)}")
    
    print_separator()
    
    # Attempting to add objects that cannot fit into any bin
    print("Adding Objects That Cannot Fit into Any Bin:")
    oversized_objects = [
        (2036, 150, Color.BLUE),
        (2037, 200, Color.GREEN),
        (2038, 180, Color.YELLOW)
    ]
    for obj_id, size, color in oversized_objects:
        try:
            gcms.add_object(obj_id, size, color)
            print(f"Added Object ID: {obj_id}, Size: {size}, Color: {color.name}")
        except NoBinFoundException:
            print(f"Failed to add Object ID: {obj_id}, Size: {size}, Color: {color.name} - No suitable bin found")
    
    print_separator()
    
    # Final bin information
    print("Final Bin Information:")
    for bin_id, _ in initial_bin_data + additional_bin_data:
        try:
            remaining_capacity, objects_in_bin = gcms.bin_info(bin_id)
            print(f"Bin ID: {bin_id}, Remaining Capacity: {remaining_capacity}, Objects: {objects_in_bin}")
        except Exception as e:
            print(f"Error retrieving info for Bin ID: {bin_id} - {str(e)}")
    
    print_separator()
    
    print("All enhanced tests completed.")