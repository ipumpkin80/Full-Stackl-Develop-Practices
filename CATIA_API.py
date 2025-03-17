import win32com.client

class CatiaSimulationAPI:
    def __init__(self):
        try:
            self.catia = win32com.client.Dispatch("CATIA.Application")
            self.catia.Visible = True
        except Exception as e:
            print("Error connecting to CATIA: ", e)

    def open_document(self, file_path):
        """Open an existing CATIA document."""
        try:
            self.document = self.catia.Documents.Open(file_path)
            print(f"Document {file_path} opened successfully.")
        except Exception as e:
            print(f"Error opening document: {e}")

    def setup_simulation(self):
        """Setup basic simulation."""
        try:
            # Assuming you have an active document and simulation setup
            self.product_document = self.catia.ActiveDocument
            self.product = self.product_document.Product
            
            # Access the Simulation Workbench
            self.simulation_workbench = self.product.GetWorkbench("SimulationWorkbench")

            # Example: Configure some simulation parameters (dummy values used)
            self.simulation = self.simulation_workbench.Simulations.Add()
            self.simulation.Name = "NewSimulation"
            self.simulation.Duration = 10  # 10 seconds simulation
            
            print("Simulation setup complete.")
        except Exception as e:
            print(f"Error setting up simulation: {e}")

    def run_simulation(self):
        """Run the simulation."""
        try:
            if self.simulation:
                self.simulation.Run()
                print("Simulation is running.")
        except Exception as e:
            print(f"Error running simulation: {e}")

    def save_document(self, output_path):
        """Save the CATIA document."""
        try:
            self.document.SaveAs(output_path)
            print(f"Document saved as {output_path}.")
        except Exception as e:
            print(f"Error saving document: {e}")

# Example of using the API
if __name__ == "__main__":
    catia_api = CatiaSimulationAPI()

    # Path to the CATIA document to simulate
    catia_api.open_document("C:\\path\\to\\your\\catia_document.CATProduct")
    
    # Setup and run simulation
    catia_api.setup_simulation()
    catia_api.run_simulation()

    # Save the updated document
    catia_api.save_document("C:\\path\\to\\save\\simulated_document.CATProduct")
