# SpyGlass
SpyGlass, the all in one tool for a kickass api.

SpyGlass in use:
![](https://github.com/oldkingcone/SpyGlass/blob/main/images/dashboard.png?raw=true)

# Greetz

J5 && Root.

# Details

- To install, you will need ![pycryptodome](https://www.pycryptodome.org/src/installation) (https://www.pycryptodome.org/src/installation), I would strongly advise looking over the instructions for that. 
- depends on the requests module.
- designed to be modular, with the end user in mind. Still working on the plugins portion, but once thats complete this will support dynamic loading of custom plugins.
- requires a pre-shared API key to use. (This api key is for purchase.)

# What is CloudGaze?

Cloudgaze is the end all be all, think shodan + google + leakix in one database. This(CloudGaze) tool crawls the greater internet of everything. Basically, a DB full of over 45 million unique ip addresses that have been crawled and indexed(this primarily focuses on web ports, more will be added in the future. I hear it now, "But where are they sourced?" 

I am very glad you asked that, I have a honeypot running that I log all requests made to it. This has helped me build up a very lengthy list of very obviously malicious ranges. Once confirmed through some Threat Intel and OSINT sources, they get added into the rotation and are crawled storing all historical data that I can find about the servers from the first time scanned, and appending it to the data collected by the next pass made over that specific server. Think of it as a better censys without all the reputation, because unlike those companies, I crawl the endpoints... And store that data to be returned to you the end user whenever it makes a malicious request or action against your servers/w.e it is that triggers the issue. In this single API I return to you more information about malicious domains than you can currently get, without having to do much leg work yourself.

Although the screenshots just show example usage and not actual data, please understand these screenshots represent the capability of this tool and not the actual database itself, it is rich with information.

There is no GUI on the website. This is designed from the ground up to be utilized in the terminal.

Utilizing this tool, it streamlines the whole process. You can tap into the database looking for a single ip address, or multiple addresses. The choice is entirely yours as shown below:
![](https://github.com/oldkingcone/SpyGlass/blob/main/images/multi_call.png?raw=true)
![](https://github.com/oldkingcone/SpyGlass/blob/main/images/data_returned_by_cg.png?raw=true)

# Future editions
- Will include SSL fingerprints, and search by SSL key (fingerprints, etc).
- Will include DNS information, and the ability to search by domain name.
- (the above are already written, i just need to add them to the crawler rotation and as a call within the api itself.)


# Addendum
I am in no way responsible for misuse of this product or the information contained within it. This tool is released for educational value, and for other legitimate means. Do not under any circumstance misuse this tool or the information obtained from the API key and the database. Please ensure you are abiding by the laws in the country of which you reside.


