</head>
  <body>
    <h1>Website Blocker Script</h1>
    <p>This is a simple Python script that allows you to block or unblock websites on your computer.</p>
    <h2>Prerequisites</h2>
    <ul>
      <li>Python 3 installed on your computer</li>
      <li>A text editor to modify the code</li>
      <li>Administrator privileges to edit the hosts file</li>
    </ul>
    <h2>How to Use the Code</h2>
    <ol>
      <li>Clone or download the code from this repository.</li>
      <li>Open the `website_blocker.py` file in a text editor.</li>
      <li>Define the websites you want to block by adding or removing elements from the `websites` list.</li>
      <li>Save and run the code by using the command `python website_blocker.py` in the terminal or command prompt.</li>
      <li>Follow the prompts to choose whether you want to block or unblock websites.</li>
    </ol>
    <h2>How the Code Works</h2>
    <ul>
      <li>The script defines the path to the `hosts` file, which is used to map hostnames to IP addresses on your computer.</li>
      <li>It also defines a list of websites that you want to block or unblock.</li>
      <li>When you run the code, it will prompt you to choose whether you want to block or unblock websites.</li>
      <li>If you choose to block websites, the script will add the IP address `127.0.0.1` to the hosts file for each of the websites in the `websites` list. This will make it so that when you try to access one of these websites, your computer will be redirected to the local IP address, effectively blocking the website.</li>
      <li>If you choose to unblock websites, the script will remove the entries from the hosts file that were added when you blocked the websites.</li>
    </ul>
    <h2>Note</h2>
    <ul>
      <li>Make sure to run the script with administrator privileges, as the hosts file is protected and can only be modified by an administrator.</li>
      <li>This code is intended for Windows systems and may not work on other operating systems.</li>
    </ul>
  </body>
</html>
