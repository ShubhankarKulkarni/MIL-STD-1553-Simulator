# MIL-STD-1553-Simulator

MIL-STD-1553 is a serial communication protocol that is used in spacecrafts for internal communication. A spacecraft consists of various components like main computer, star tracker, fly wheel, temperature sensor, cameras (also called as Remote Terminals) etc. The main computer needs to communicate with all the other peripherals to get the data and send it to ground station for further processing. This internal communication is done by a serial bus called MIL-STD-1553. This repository contains a simulation for this protocol. It can be used to create any space applications by importing the simulator into your code.

MIL-STD-1553 has Bus Controller that orchestrates the transmission and reception of data on the serial bus. It always initiates the communication and commands Remote Terminal for sending or receiving data. Only one node or Remote Terminal can send data on the bus at a given moment when ordered by the Bus Controller. The details of the protocol can be found in [MIL-STD-1553 Tutorial and Reference](https://www.altadt.com/download/mil-std-1553-tutorial-and-reference/) document by Alta dt.   

## About This Repository:

This repository segregated based on various components that are described in the MIL-STD-1553 standard. Two of the most important components are Bus Controller and Remote Terminals. For a small network, one serial bus can handle up to 31 remote terminals and one bus controller. This repository is divided into two parts. Bus Controller Simulator and Remote Terminal Simulator. Both the components have separate set of functionalities.

* [Bus Controller Simulator](./Bus_Controller/BC_Simulator.py) : This simulator is responsible to understand the requirements from the Flight Software or Spacecraft computer and send commands and data to Remote Terminal.

* [Remote Terminal Simulator](./Remote_Terminal/RT_Simulator.py) : This simulator is responsible for understanding the commands or data comming from the Bus Controller and send status and data based on the requirements sent by the Bus Controller. 

## How To Use This Simulator

This simulator uses ethernet communication instead of the actual physical communication that is mentioned in the standars. The standard is developed taking harsh and noisy conditions into account. The simulator majorly focuses on data layer of the standard. Based on this, you can either deploy both the simulators on the same machine and test it over the local loopback or you can deploy separate simulators on separate machines in a single subnet or same network. 
  
You can run the following commands to run the simulators

* python BC_Simulator.py
* python RT_Simulator.py
* python Simulator.py

Or you can uncomment a section of code in Simulator.py that creates threads for Bus Controller Simulator and Remote Terminal Simulator and then run the following command

* python Simulator.py

Simulator.py only provides an example of how you can use BC and RT simulators. You can replace Simulator.py by any space application that needs to transfer any data using MIL-STD-1553. Apart from that, this whole repository is developed as a module. So, you can simply clone the repository into your application and can import it.
