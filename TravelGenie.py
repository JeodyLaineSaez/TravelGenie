import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Travel Genie")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the position to center the window
x = (screen_width - 600) // 2
y = (screen_height - 600) // 2

# Set the window position and size
window.geometry(f"600x600+{x}+{y}")
# Set background color
window.configure(bg="#E6CCFF")

# Load the logo image and resize it
logo_image = tk.PhotoImage(file="C:/Users/user/Downloads/TravelGenie1.png")
logo_image = logo_image.subsample(3)  # Resize to 1/5 of the original size for 2x2

# Create a frame to hold the logo and login components
frame = tk.Frame(window, bg="#E6CCFF")
frame.pack(pady=30)  # Add padding at the top

# Create a label to display the logo image
logo_label = tk.Label(frame, image=logo_image, bg="#E6CCFF")
logo_label.image = logo_image  # Keep a reference to the image
logo_label.pack()  # Pack the logo label

# Add padding between the logo and login components
tk.Label(window, text=" ", bg="#E6CCFF").pack()

username_frame = tk.Frame(window, bg="#E6CCFF")
username_label = tk.Label(username_frame, text="Username", font=('Arial', 14), bg="#E6CCFF")
username_label.pack(side='left')
username_entry = tk.Entry(username_frame)
username_entry.pack(side='right')
username_frame.pack()

# Add padding between the username and password fields
tk.Label(window, text=" ", bg="#E6CCFF").pack()

password_frame = tk.Frame(window, bg="#E6CCFF")
password_label = tk.Label(password_frame, text="Password", font=('Arial', 14), bg="#E6CCFF")
password_label.pack(side='left')
password_entry = tk.Entry(password_frame, show="*")
password_entry.pack(side='right')
password_frame.pack()

# Add padding between the password field and login button
tk.Label(window, text=" ", bg="#E6CCFF").pack()

login_button = tk.Button(window, text="Login", bg='#805AD5', fg='#FFFFFF')
login_button.pack()  # Added missing parentheses


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == 'JeodyLaineSaez' and password == 'HelloWorld123':
        print(f"Username: {username}, Password: {password}")
        messagebox.showinfo("Success", "Successfully logged in")
        clear_entries()
        open_surigao_window()
    else:
        messagebox.showerror("Error", "Incorrect username or password")
        clear_entries()


def clear_entries():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


username_entry.focus()

login_button.config(command=login)  # Configured login button command


def open_surigao_window():
    # Destroy any existing Surigao window
    for widget in window.winfo_children():
        widget.destroy()
    surigao_window = tk.Toplevel(window)
    surigao_window.title("Tourist Destinations in Surigao del Norte")

    # Calculate the position to center the window
    window_width = 600
    window_height = 600
    screen_width = surigao_window.winfo_screenwidth()
    screen_height = surigao_window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    surigao_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    surigao_window.configure(bg="#E6CCFF")  # Set background color

    destinations_info = {
        "Mabua Pebble Beach": {
            "info": """Mabua Pebble Beach is a unique natural attraction located in Surigao City, Philippines. Unlike typical sandy beaches, Mabua Pebble Beach is covered in smooth, rounded stones of various sizes and colors, giving it a distinct and picturesque appearance. These stones, polished over time by the waves of the Pacific Ocean, create a stunning contrast against the azure waters.

Towards the water, on the right, is a rock formation. It is simple to ascend the rocks but exercise additional caution because some of the rocks have slick edges. The stones are exceptionally white here, especially in the summer, and the waters are crystal pure. Because certain areas on our feet are related to our internal organs, strolling barefoot on smooth stones has an effect on the body, making this beach both beautiful and restorative.""",
            "image": "C:/Users/user/Downloads/pebble-beach.png",  # Update with actual image path
            "get_there": "From Surigao Integrated Bus Terminal, take a motorcycle or a tricycle (motorized three-wheeled vehicle) from the trike terminal to Mabua located along Sarvida St. just beside Palma Trade Center. The tricycle will then take you straight to Mabua Beach with 30 minutes travel time.",
            "activities": """Visitors to Mabua Pebble Beach can enjoy activities such as beachcombing, photography, picnicking, and simply taking in the breathtaking scenery. The sound of the waves rolling over the pebbles adds to the serene ambiance of the place, making it a popular destination for relaxation and unwinding.

Additionally, Mabua Pebble Beach offers opportunities for swimming and snorkeling, although the presence of pebbles instead of sand underfoot may require some adjustment for those accustomed to traditional sandy beaches.""",
            "delicacy": "Sayongsong is a traditional Filipino delicacy, particularly popular in Surigao del Norte, where Mabua Pebble Beach is located. It is a sweet and sticky dessert made from glutinous rice flour, coconut milk, and sugar, then wrapped in cone-shaped banana leaves and steamed until cooked."
        },
        "Day-asan Floating Village": {
            "info": "Day-asan Floating Village is a unique and picturesque community located in Barangay Day-asan, Surigao City, Philippines. What sets it apart from typical villages is that it is built entirely on water, with houses standing on stilts above the sea. This floating village is home to a vibrant community of fishermen and their families, who have adapted to a lifestyle intricately connected to the surrounding waters. Interestingly, because of the similar features/nature the humble village got its tag as the “little Venice of Surigao City",
            "image": "C:/Users/user/Downloads/Day-asan-Floating_Village.png",  # Update with actual image path
            "get_there": "Day-Asan is accessible either by land or by sea. Motorized boats going to the village are docked in the City Wharf while habal-habal/ motorcycles for hire are stationed near the City public market. Fare ranges from 25 to 50 pesos. Travel time is around 15 to 30 minutes.",
            "activities": """Visitors to Day-asan Floating Village can immerse themselves in the culture and daily activities of the residents, experiencing firsthand how they navigate their homes and livelihoods on the water.

Aside from observing the daily life of the community, tourists can engage in various activities during their visit to Day-asan Floating Village. These activities may include boat tours around the village, kayaking through the tranquil waters, interacting with locals to learn about their customs and traditions, and enjoying fresh seafood delicacies prepared by local eateries. The floating village also presents excellent opportunities for photography enthusiasts, with its scenic backdrop of colorful houses standing against the vast expanse of the sea.""",
            "delicacy": """Kinilaw is a popular Filipino dish similar to ceviche, where raw seafood, typically fish or shrimp, is marinated in vinegar, citrus juice, onions, chili peppers, and spices. It's a refreshing and flavorful appetizer commonly enjoyed in coastal regions like Surigao.

Adobong Saang is a traditional Filipino dish made from saang or spider conch, a type of shellfish commonly found in coastal areas. The saang meat is cooked in adobo-style, simmered in a mixture of vinegar, soy sauce, garlic, onions, and spices until tender and flavorful.

Day-asan Floating Village is also renowned for its abundance of fresh seafood, and visitors can indulge in a variety of sizzling seafood dishes prepared to order. From succulent shrimp and flavorful fish to tender squid and juicy shellfish, the options are diverse and tantalizing."""
        },
        "Silop Cave": {
            "info": """Silop Cave is known for its stunning limestone formations and crystal-clear underground rivers with 6 cave system. When you enter the cave, you're greeted by a cool breeze and the sound of dripping water echoing through the chambers. The cave is home to various species of bats and swiftlets, adding to its mystique.
An entrance fee of P100/head is allocated for the safety gears you'll need for spelunking. So after the registration process, we started taking the path to the entrance of one of the caves, but before reaching the cave, we have to survive the muddy and slippery trail route to the entrance of the recently opened cave 7. The entrance of cave 7 is very narrow that you have to crawl to be able to enter the cave. Amazement comes after entering our first cave.""",
            "image": "C:/Users/user/Downloads/Silop-Cave.png",  # Update with actual image path
            "get_there": "Silop Cave is located at Brgy. Silop, Surigao City. It is a 20 minutes ride from the city center. You can either take a jeep bound to arellano then alight at the barangay Silop junction or you can hail a habal-habal that would take you directly to Silop Barangay Hall where the registration process takes place.",
            "activities" : "One of the main attractions is exploring the cave system, which offers an adventure-filled experience. Inside the cave, visitors can marvel at the mesmerizing stalactites and stalagmites formed over thousands of years. The cool breeze and the sound of dripping water create a mystical ambiance as tourists venture deeper into the cave's chambers. Additionally, Silop Cave provides opportunities for spelunking, allowing adventurers to navigate through narrow passages and crawl through tight spaces, adding to the thrill of exploration. For nature enthusiasts, observing the diverse bat and swiftlet populations that call the cave home can be a fascinating experience.""",
            "delicacy": """One of the distinctive delicacies found in the area is "tamilok," which are woodworms harvested from decaying mangrove trees. Despite its appearance, tamilok is considered a delicacy and is typically eaten raw or marinated in vinegar and spices. It offers a unique flavor profile, often described as salty and slightly acidic, with a chewy texture.

Additionally, visitors to Silop Cave might encounter other local delicacies such as "kinilaw," a traditional Filipino dish made from raw fish marinated in vinegar, calamansi juice, onions, ginger, and chili peppers. Kinilaw showcases the freshness of seafood and highlights the flavors of the region. Another delicacy to try is "tinolang isda," a fish soup cooked with ginger, garlic, onions, and various local vegetables, providing a comforting and hearty dining experience. """
        },
        "Basul Island": {
            "info": """Basul Island, located off the coast of Surigao City in the Philippines, is a breathtaking destination known for its pristine beaches and crystal-clear waters. It's a small island, but it packs a punch when it comes to natural beauty. The powdery white sand beaches are perfect for sunbathing and relaxation, while the surrounding turquoise waters offer great opportunities for swimming, snorkeling, and diving. You can explore the colorful coral reefs teeming with marine life, or simply enjoy the tranquil atmosphere and stunning views. Basul Island is also home to lush greenery and coconut palm trees, providing shady spots to escape the heat. There are no rooms available on the island but there are several open-air cottages that are for rent. There's an entrance fee of 50 pesos per person plus 100 pesos boat docking fee being collected by the islands' caretaker. There are also no stores on the island so better bring your own food if you plan on going there. You can also stay overnight but you need to bring your own tent. There is no electricity on the island but globe signal is strong.""",
            "image": "C:/Users/user/Downloads/Basul-Island.png",  # Update with actual image path
            "get_there": """From the airport, take a tricycle or multicab to reach the port. At the port, you'll find boats or ferries that offer trips to various islands, including Basul Island. Depending on the boat schedule, you may need to wait for the next available trip to Basul Island. Once you've found a boat, arrange for your transport and purchase tickets. Prices and schedules may vary, so be sure to confirm details with the boat operator. The travel time from Surigao City Port to Basul Island is 20-30 minutes.""",
            "activities": """For those craving a leisurely day by the sea, the island's pristine beaches beckon with soft, powdery sands and tranquil waters perfect for swimming and sunbathing. Snorkeling enthusiasts can explore vibrant coral reefs teeming with colorful marine life, while diving enthusiasts can delve deeper into the underwater world, discovering hidden treasures beneath the waves. Adventurous souls can embark on island-hopping excursions to nearby islets, discovering secluded coves and untouched landscapes. Hiking trails meander through the island's lush interior, providing opportunities to immerse oneself in nature and soak in panoramic views of the surrounding seascape. Kayaking and paddleboarding are also popular activities, allowing visitors to navigate the island's pristine coastline at their own pace.""",
            "delicacy": "One of the delicacies that you might find on Basul Island is fresh seafood, caught daily by local fishermen. Grilled fish, shrimp, and squid are commonly enjoyed dishes, cooked simply with local herbs and spices, showcasing the natural flavors of the sea. Another delicacy you might encounter is coconut-based dishes, such as kinilaw na lato (seaweed salad) made with fresh seaweed harvested from the surrounding waters and seasoned with coconut vinegar and spices. Additionally, you may come across traditional Filipino snacks like bibingka (rice cake) or suman (sticky rice cooked in banana leaves), which are often enjoyed as treats during gatherings or special occasions."
        },
        "San Nicolas de Tolentino Cathedral": {
            "info": "San Nicolas de Tolentino Cathedral, a beautiful mid-17th-century church located in the center of the city. The church was originally built in 1754 by the Order of Augustinian Recollects. It was damaged by bombing during WWII and was reconstructed in 1988. Today, it is considered the biggest Augustinian cathedral in the Surigao Region and a place for reflection and rest among the locals.",
            "image": "C:/Users/user/Downloads/San-Nicolas-de-Tolentino-Cathedral.png",  # Update with actual image path
            "get_there": "To get to the cathedral, one can use public transportation like buses or tricycles, or opt for private vehicles or taxis. The church is centrally located in Surigao City, making it easily accessible to both locals and tourists. Additionally, visitors can explore the surrounding area, which may include historical landmarks, parks, and local markets, adding to the overall experience of visiting the cathedral and the city.",
            "activities": "Apart from attending regular religious services like Mass, people can participate in special events such as weddings, baptisms, and religious celebrations. The church also hosts community gatherings and outreach programs to help those in need.",
            "delicacy": """Balut is a fertilized duck egg with a partially developed embryo inside, boiled and eaten as a snack.

Taho is a  sweet Filipino snack made of fresh soft/silken tofu, arnibal (sweet syrup), and sago pearls (similar to tapioca pearls).

Banana Cue is a deep-fried banana coated in caramelized brown sugar, skewered on a stick.

Fish Balls is a  deep-fried balls made from fish paste, served with a sweet and tangy sauce.

Salvaro is a  A traditional delicacy made from pounded, sun-dried, and fried cassava. It is often shaped into thin, round discs and fried until crispy. The process of pounding and drying the cassava gives salvaro a unique texture that is crunchy yet slightly chewy. It is usually seasoned with salt or sugar, depending on personal preference.

Bibingka is a type of rice cake made from ground rice, coconut milk, sugar, and sometimes eggs. It is traditionally cooked in clay pots lined with banana leaves over hot coals, giving it a distinct flavor and aroma. Bibingka sa Delicacy is often served warm, topped with butter, grated coconut, and sometimes salted eggs or cheese for added richness."""
        },

    }

    scrollbar = tk.Scrollbar(surigao_window, bg="#6A0DAD")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Set a fixed width for the list box
    destination_listbox = tk.Listbox(surigao_window, yscrollcommand=scrollbar.set, width=30)

    for destination in destinations_info.keys():
        destination_listbox.insert(tk.END, destination)

    destination_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    # Configure list box to adjust its height based on the number of items
    destination_listbox.config(height=len(destinations_info))

    scrollbar.config(command=destination_listbox.yview)

    def show_destination_info():
        selected_index = destination_listbox.curselection()
        if selected_index:
            selected_destination = destination_listbox.get(selected_index)
            info = destinations_info[selected_destination]["info"]
            get_there = destinations_info[selected_destination]["get_there"]
            activities = destinations_info[selected_destination]["activities"]
            delicacy = destinations_info[selected_destination]["delicacy"]
            image_path = destinations_info[selected_destination]["image"]  # Get image path

            # Create a new window to display detailed information
            detail_window = tk.Toplevel(window)
            detail_window.title(selected_destination)

            # Calculate the position to center the window
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            detail_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
            detail_window.configure(bg="#E6CCFF")  # Set background color

            # Load and resize the image
            image = tk.PhotoImage(file=image_path)
            image = image.subsample(2)  # Resize the image
            image_label = tk.Label(detail_window, image=image, bg="#E6CCFF")
            image_label.image = image  # Keep a reference to the image
            image_label.pack()

            # Create a frame to hold the scrollable text
            text_frame = tk.Frame(detail_window, bg="#E6CCFF")
            text_frame.pack(fill=tk.BOTH, expand=True)

            # Create a scrollbar for the text
            scroll_y = tk.Scrollbar(text_frame, orient="vertical")
            scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

            # Create a Text widget for displaying information
            info_text = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=scroll_y.set, bg="#E6CCFF")
            info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Configure the scrollbar
            scroll_y.config(command=info_text.yview)

            # Insert information into the Text widget
            info_text.insert(tk.END, "Overview\n" + info + "\n\n")
            info_text.insert(tk.END, "How to get there:\n" + get_there + "\n\n")
            info_text.insert(tk.END, "Activities:\n" + activities + "\n\n")
            info_text.insert(tk.END, "Local Delicacy:\n" + delicacy + "\n\n")


    destination_info_button = tk.Button(surigao_window, text="Show Details", command=show_destination_info,
                                        bg="#805AD5", fg="#FFFFFF")
    destination_info_button.pack(pady=10)


window.mainloop()
