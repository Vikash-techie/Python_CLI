# Python_CLI
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/vikash-sunil-91174518b/)



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Python CLI Tool</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot](https://drive.google.com/uc?export=view&id=1HhmPrvFrLsMUIToE6HX3BKaR6rUOiYYK)](https://drive.google.com/file/d/1HhmPrvFrLsMUIToE6HX3BKaR6rUOiYYK/view?usp=sharing)

This is a simple **Command Line Interface Tool purely made in Python**.  
The given tool has three basic user options which are -h, -i and -update.  
The **-h** option shortly describes the tool and the available options.  
The **-i** option will read an input csv file and a dependency@version and accordingly it will produce an output csv file.  
The output csv file will contain the version number and also true or false to indicate whether the given version in input is less or greater than the current version number.  
The **-update** option is similar to -i but through this option the user also creates a Pull Request if the current version of the dependency is less than the input version.  
Hence this is a CLI tool that can help a user for release process related work.  

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python3](https://python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python should be installed on your machine.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/dyte-submissions/dyte-vit-2022-Vikash-techie.git
   ```
2. Run the python code
   ```py
   python Vikash_SDK_Tool.py
   ```
3. Run the help function
   ```py
   python Vikash_SDK_Tool.py -h
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
[![image](https://drive.google.com/uc?export=view&id=1M4VbETXo1eqH1iFB8o4Jt485ucykvacN)](https://drive.google.com/file/d/1M4VbETXo1eqH1iFB8o4Jt485ucykvacN/view?usp=sharing)  
* To run the -i option the user should type python Vikash_SDK_Tool.py -i input.csv dependency@version_number  

[![image](https://drive.google.com/uc?export=view&id=18u20puMD60m-1pY7_GOOxIzqD7lI72mt)](https://drive.google.com/file/d/18u20puMD60m-1pY7_GOOxIzqD7lI72mt/view?usp=sharing)
* To run the -update option the user should type python Vikash_SDK_Tool.py -update -i input.csv dependency@version_number  
[![image](https://drive.google.com/uc?export=view&id=1M4VbETXo1eqH1iFB8o4Jt485ucykvacN)](https://drive.google.com/file/d/1M4VbETXo1eqH1iFB8o4Jt485ucykvacN/view?usp=sharing)  
* To run the -i option the user should type python Vikash_SDK_Tool.py -i input.csv dependency@version_number 
[![image](https://drive.google.com/uc?export=view&id=1g9asgmK7BFC8HJpkfok1t34qzfX0ThBS)](https://drive.google.com/file/d/1g9asgmK7BFC8HJpkfok1t34qzfX0ThBS/view?usp=sharing)  
* This is what a user's input file will look like.  

[![image](https://drive.google.com/uc?export=view&id=1IJ-zycx0iifLUEo2-8eKJQYoS_cDX9wi)](https://drive.google.com/file/d/1IJ-zycx0iifLUEo2-8eKJQYoS_cDX9wi/view?usp=sharing)  
* This is what a user's output file will look like after running the update option.  

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Vikash Sunil -  vikashsunil01@gmail.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
