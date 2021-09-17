"""Net Functions.

The following functions give you access to interact with http services.
"""


__all__ = [
    "getExternalIpAddress",
    "getHostName",
    "getIpAddress",
    "getRemoteServers",
    "httpDelete",
    "httpGet",
    "httpPost",
    "httpPut",
    "openURL",
    "sendEmail",
]

import pprint
import socket


def getExternalIpAddress():
    """Returns the client's IP address, as it is detected by the
    Gateway.

    This means that this call will communicate with the Gateway, and the
    Gateway will tell the client what IP address its incoming traffic is
    coming from. If you have a client behind a NAT router, then this
    address will be the WAN address of the router instead of the LAN
    address of the client, which is what you'd get with
    system.net.getIpAddress.

    Returns:
        str: A text representation of the client's IP address, as
            detected by the Gateway.
    """
    return "52.52.32.221"


def getHostName():
    """Returns the host name of the computer that the script was ran
    on.

    When run in the Gateway scope, returns the Gateway hostname. When
    run in the Client scope, returns the Client hostname. On Windows,
    this is typically the "computer name". For example, might return
    EAST_WING_WORKSTATION or bobs-laptop.

    Returns:
        str: The hostname of the local machine.
    """
    return socket.gethostname()


def getIpAddress():
    """Returns the IP address of the computer the client is running on,
    as it appears to the client.

    See also: system.net.getExternalIpAddress().

    Returns:
        str: Returns the IP address of the local machine, as it sees it.
    """
    return "127.0.0.1"


def getRemoteServers(runningOnly=True):
    """This function returns a List of Gateway Network servers that are
    visible from the local Gateway.

    Args:
        runningOnly (bool): If set to True, only servers on the Gateway
            Network that are running will be returned. Servers that have
            lost contact with the Gateway Network will be filtered out.
            Optional.

    Returns:
        list[str]: A List of Strings representing Gateway Network server
            ids.
    """
    pprint.pprint(runningOnly)
    return []


def httpDelete(
    url,
    contentType=None,
    connectTimeout=10000,
    readTimeout=60000,
    username=None,
    password=None,
    headerValues=None,
    bypassCertValidation=True,
):
    """Performs an HTTP DELETE to the given URL.

    Args:
        url (str): The URL to send the request to.
        contentType (str): The MIME type used in the HTTP 'Content-type'
            header. Optional.
        connectTimeout (int): The timeout for connecting to the URL in
            milliseconds. Default is 10,000. Optional.
        readTimeout (int): The read timeout for the operation in
            milliseconds. Default is 60,000. Optional.
        username (str): If specified, the call will attempt to
            authenticate with basic HTTP authentication. Optional.
        password (str): The password used for basic HTTP authentication,
            if the username parameter is also present. Optional.
        headerValues (dict): A dictionary of name/value pairs that will
            be set in the HTTP header. Optional.
        bypassCertValidation (bool): If the target address in an HTTPS
            address, and this parameter is TRUE, the system will bypass
            all SSL certificate validation. This is not recommended,
            though is sometimes necessary for self-signed certificates.
            Optional.

    Returns:
        object: The content returned for the DELETE operation.
    """
    pprint.pprint(
        [
            url,
            contentType,
            connectTimeout,
            readTimeout,
            username,
            password,
            headerValues,
            bypassCertValidation,
        ]
    )
    return object


def httpGet(
    url,
    connectTimeout=10000,
    readTimeout=60000,
    username=None,
    password=None,
    headerValues=None,
    bypassCertValidation=None,
    useCaches=True,
    throwOnError=True,
):
    """Retrieves the document at the given URL using the HTTP GET
    protocol.

    The document is returned as a string. For example, if you use the
    URL of a website, you'll get the same thing you'd get by going to
    that website in a browser and using the browser's "View Source"
    function.

    Args:
        url (str): The URL to retrieve.
        connectTimeout (int): The timeout for connecting to the URL. In
            milliseconds. Default is 10,000. Optional.
        readTimeout (int): The read timeout for the get operation. In
            milliseconds. Default is 60,000. Optional.
        username (str): If specified, the call will attempt to
            authenticate with basic HTTP authentication. Optional.
        password (str): The password used for basic HTTP authentication,
            if the username parameter is also present. Optional.
        headerValues (dict): A dictionary of name/value pairs that will
            be set in the HTTP header. Optional.
        bypassCertValidation (bool): If the target address is an HTTPS
            address, and this parameter is True, the system will bypass
            all SSL certificate validation. This is not recommended,
            though is sometimes necessary for self-signed certificates.
            Optional.
        useCaches (bool): Will cache the information returned by the
            httpGet call. If using this for something that constantly
            updates like an rss feed, it would be better to set this to
            False. Default is True. Optional.
        throwOnError (bool): Set to False if you wish to get the error
            body rather than a Python exception if the GET request
            returns an error code (non-200 responsive). Default is True.
            Optional.

    Returns:
        str: The content found at the given URL.
    """
    pprint.pprint(
        [
            url,
            connectTimeout,
            readTimeout,
            username,
            password,
            headerValues,
            bypassCertValidation,
            useCaches,
            throwOnError,
        ]
    )
    return ""


def httpPost(url, *args):
    """Retrieves the document at the given URL using the HTTP POST
    protocol.

    If a parameter dictionary argument is specified, the entries in the
    dictionary will encoded in "application/x-www-form-urlencoded"
    format, and then posted. You can post arbitrary data as well, but
    you'll need to specify the MIME type. The document is then returned
    as a string.

    Args:
        url (str): The URL to post to.
        *args: Variable length argument list.

    Returns:
        str: The content returned for the POST operation.
    """
    pprint.pprint([url, args])
    return ""


def httpPut(url, *args, **kwargs):
    """Performs an HTTP PUT to the given URL.

    Encodes the given dictionary of parameters using
    "applications/x-www-form-urlencoded" format.

    Args:
        url (str): The URL to send the request to.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        str: The content returned by the PUT operation.
    """
    pprint.pprint([url, args, kwargs])
    return ""


def openURL(url, useApplet=False):
    """Opens the given URL or URI scheme outside of the currently
    running Client in whatever application the host operating system
    deems appropriate.

    Args:
        url (str): The URL to open in a web browser.
        useApplet (bool): If set to True (1), and the client is running
            as an Applet, then the browser instance that launched the
            applet will be used to open the URL. Optional.
    """
    pprint.pprint([url, useApplet])


def sendEmail(
    smtp,
    fromAddr,
    subject,
    body,
    html,
    to,
    attachmentNames=None,
    attachmentData=None,
    timeout=300000,
    username=None,
    password=None,
    priority="3",
    smtpProfile=None,
    cc=None,
    bcc=None,
    retries=0,
    replyTo=None,
):
    """Sends an email through the given SMTP server.

    Note that this email is relayed first through the Gateway - the
    client host machine doesn't need network access to the SMTP server.

    Args:
        smtp (str): The address of an SMTP server to send the email
            through, like "mail.example.com". A port can be specified,
            like "mail.example.com:25". SSL can also be forced, like
            "mail.example.com:25:tls".
        fromAddr (str): An email address to have the email come from.
        subject (str): The subject line for the email.
        body (str): The body text of the email.
        html (bool): A flag indicating whether or not to send the email
            as an HTML email. Will auto-detect if omitted.
        to (list[str]): A list of email addresses to send to.
        attachmentNames (list[str]): A list of attachment names.
            Attachment names must have the correct extension for the
            file type or an error will occur.
        attachmentData (list[object]): A list of attachment data, in
            binary format.
        timeout (int): A timeout for the email, specified in
            milliseconds. Defaults to 5 minutes (60,000*5). Optional.
        username (str): If specified, will be used to authenticate with
            the SMTP host. Optional.
        password (str): If specified, will be used to authenticate with
            the SMTP host. Optional.
        priority (str): Priority for the message, from "1" to "5", with
            "1" being highest priority. Defaults to "3" (normal)
            priority. Optional.
        smtpProfile (str): If specified, the named SMTP profile defined
            in the Gateway will be used. If this keyword is present, the
            smtp, username, and password keywords will be ignored.
            Optional.
        cc (list[str]): A list of email addresses to carbon copy. Only
            available if a smtpProfile is used. Optional.
        bcc (list[str]): A list of email addresses to blind carbon copy.
            Only available if a smtpProfile is used. Optional.
        retries (int): The number of additional times to retry sending
            on failure. Defaults to 0. Only available if a smtpProfile
            is used. Optional.
        replyTo (list[str]): An optional list of addresses to have the
            recipients reply to. If omitted, this defaults to the from
            address. Optional.
    """
    pprint.pprint(
        [
            smtp,
            fromAddr,
            subject,
            body,
            html,
            to,
            attachmentNames,
            attachmentData,
            timeout,
            username,
            password,
            priority,
            smtpProfile,
            cc,
            bcc,
            retries,
            replyTo,
        ]
    )
