class HelpDeskTicket:
    ticket_counter = 2000
    open_tickets = 0
    resolved_tickets = 0
    tickets = []

    def __init__(self, creator_name, staff_id, contact_email, description):
        HelpDeskTicket.ticket_counter += 1
        self.ticket_number = HelpDeskTicket.ticket_counter
        self.creator_name = creator_name
        self.staff_id = staff_id
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        HelpDeskTicket.open_tickets += 1
        HelpDeskTicket.tickets.append(self)

    def respond(self, response):
        self.response = response
        self.status = "Closed"
        HelpDeskTicket.open_tickets -= 1
        HelpDeskTicket.resolved_tickets += 1

    def reopen(self):
        self.response = "Not Yet Provided"
        self.status = "Reopened"
        HelpDeskTicket.open_tickets += 1
        HelpDeskTicket.resolved_tickets -= 1

    def resolve_password_change(self):
        new_password = self.staff_id[:2] + self.creator_name[:3]
        self.response = f"New password generated: {new_password}"
        self.status = "Closed"
        HelpDeskTicket.open_tickets -= 1
        HelpDeskTicket.resolved_tickets += 1

    def display(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}\n")

    @classmethod
    def ticket_stats(cls):
        print("\nDisplaying Ticket Statistics\n")
        print(f"Tickets Created: {cls.ticket_counter - 2000}")
        print(f"Tickets Resolved: {cls.resolved_tickets}")
        print(f"Tickets To Solve: {cls.open_tickets}\n")


def main():
    while True:
        print("\nOptions:")
        print("1. Submit Ticket")
        print("2. Display Tickets")
        print("3. Display Ticket Statistics")
        print("4. Close Ticket")
        print("5. Reopen Ticket")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if len(HelpDeskTicket.tickets) < 5:
                creator_name = input("Enter your name: ")
                staff_id = input("Enter your Staff ID: ")
                contact_email = input("Enter your email address: ")
                description = input("Enter the description of the issue: ")

                ticket = HelpDeskTicket(creator_name, staff_id, contact_email, description)
                print("Ticket submitted successfully.")
            else:
                print("You can only create up to 5 tickets.")

        elif choice == '2':
            for ticket in HelpDeskTicket.tickets:
                ticket.display()

        elif choice == '3':
            HelpDeskTicket.ticket_stats()

        elif choice == '4':
            ticket_number = input("Enter the ticket number to close: ")
            for ticket in HelpDeskTicket.tickets:
                if str(ticket.ticket_number) == ticket_number and ticket.status == "Open":
                    ticket.respond(input("Enter your response: "))
                    print(f"Ticket {ticket_number} closed successfully.")
                    break
            else:
                print(f"Ticket {ticket_number} not found or already closed.")

        elif choice == '5':
            ticket_number = input("Enter the ticket number to reopen: ")
            for ticket in HelpDeskTicket.tickets:
                if str(ticket.ticket_number) == ticket_number and ticket.status == "Closed":
                    ticket.reopen()
                    print(f"Ticket {ticket_number} reopened successfully.")
                    break
            else:
                print(f"Ticket {ticket_number} not found or cannot be reopened.")

        elif choice == '6':
            print("Exiting the ticketing system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
