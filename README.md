# Digital-File-Sharing-System-Design
We designed a communication system consisting of a transmitter and a receiver utilizing GNU Radio  and bladeRF 2.0 micro xA9 hardware to transmit and receive a text file, an image and an audio file.

The main task was to transmit a text, image and audio file from one laptop to another using the bladeRF while chanigng the distance to understand the effect of noise and other parameters like attenuation, distortion and other enviromental impacts. I chose the modulation scheme as QPSK. While the simulation which could be done in the same computer using both the recceiver and the transmitter in the same laptop. 

But when I tested this out using an RTL SDR the noise and other envirmental parameters were too large for an audio file to be sucsessfully transmitted while the text and image files were received but the impact of noise was visible.  Hence, I deemed that the BER was too high and the design should be further refined using techniques like implementing a better encryption method.
![Screenshot 2024-05-20 145207](https://github.com/javin-5/Digital-File-Sharing-System-Design/assets/121782593/7cb5e898-6abc-44be-a497-c3ef3f5c4cea)
Above is the complete design including the blocks to define the parameters in the system, the transmitter part and the receiver part.
