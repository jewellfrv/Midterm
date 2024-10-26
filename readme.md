Project Overview
  This project creates a sophisticated, expandable calculator that can dynamically load plugins. In order to improve code readability, scalability, and maintainability, the calculator uses a number of design patterns and supports a variety of math operations. Additionally, it uses a professional logging strategy to effectively track operations, exceptions, and application flow.

 Design Patterns
  1. Factory Method Pattern: Using the specified command name, the CommandFactory class creates command objects. Following the Open/Closed Principle, this pattern enables the addition of new operations without changing the Calculator's fundamental logic.

     Impact: By separating the instantiation logic, this design makes the code extensible and maintainable, making it easier to add new commands (plugins) without changing the existing code. 

  2. Command Pattern: A command class (such as AddCommand or SubtractCommand) describes each arithmetic operation. These classes implement the execute method to carry out their particular tasks, deriving from a common Command interface.

     Impact: The ability to manage requests with flexibility is made possible by this encapsulation of operations, which also makes it possible to add features like undo/redo later on. 
  
  3. Strategy Pattern: Without changing the client code, each command can be used interchangeably since it implements a different strategy for carrying out arithmetic operations. The command classes' implementation of a common execute method allowed for this to be accomplished.

      Impact: The Strategy pattern makes it easier to add new operation strategies and allows for dynamic behavior changes in the calculator's operations at runtime.

  4. Facade Pattern: By offering a streamlined interface for interacting with command creation, execution, and history management, the Calculator class acts as a facade.

        Impact: It provides a clear platform for interacting with the calculator while concealing from the user the intricacy of command instantiation and plugin loading. 

Features

   Plugin Architecture: By dynamically loading plugins from the plugins folder, plugin architectures are used. Every plugin implements a standardized execute method from the Plugin interface, representing an arithmetic operation.

        Impact: Without changing the core classes, this structure allows the system to be expanded. The Open/Closed Principle allows for the easy addition of new operations as plugins.

    Logging Methodology: Python's logging module is used to implement a professional logging strategy. Logging is set up to record events at various levels (INFO, WARNING, ERROR), guaranteeing that all important actions and mistakes are accurately documented.    

        Impact: By offering thorough logs, this all-inclusive logging approach facilitates debugging, improves project maintainability, and aids in monitoring the behavior of the application during runtime.
