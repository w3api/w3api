---
title: SSLSocket
permalink: /Java/SSLSocket/
date: 2021-01-11
key: Java.S.SSLSocket
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SSLSocket.description }}

## Sintaxis
~~~java
public abstract class SSLSocket extends Socket
~~~

## Constructores
* [SSLSocket()](/Java/SSLSocket/SSLSocket/)

## Métodos
* [addHandshakeCompletedListener()](/Java/SSLSocket/addHandshakeCompletedListener)
* [getApplicationProtocol()](/Java/SSLSocket/getApplicationProtocol)
* [getEnabledCipherSuites()](/Java/SSLSocket/getEnabledCipherSuites)
* [getEnabledProtocols()](/Java/SSLSocket/getEnabledProtocols)
* [getEnableSessionCreation()](/Java/SSLSocket/getEnableSessionCreation)
* [getHandshakeApplicationProtocol()](/Java/SSLSocket/getHandshakeApplicationProtocol)
* [getHandshakeApplicationProtocolSelector()](/Java/SSLSocket/getHandshakeApplicationProtocolSelector)
* [getHandshakeSession()](/Java/SSLSocket/getHandshakeSession)
* [getNeedClientAuth()](/Java/SSLSocket/getNeedClientAuth)
* [getSession()](/Java/SSLSocket/getSession)
* [getSSLParameters()](/Java/SSLSocket/getSSLParameters)
* [getSupportedCipherSuites()](/Java/SSLSocket/getSupportedCipherSuites)
* [getSupportedProtocols()](/Java/SSLSocket/getSupportedProtocols)
* [getUseClientMode()](/Java/SSLSocket/getUseClientMode)
* [getWantClientAuth()](/Java/SSLSocket/getWantClientAuth)
* [removeHandshakeCompletedListener()](/Java/SSLSocket/removeHandshakeCompletedListener)
* [setEnabledCipherSuites()](/Java/SSLSocket/setEnabledCipherSuites)
* [setEnabledProtocols()](/Java/SSLSocket/setEnabledProtocols)
* [setEnableSessionCreation()](/Java/SSLSocket/setEnableSessionCreation)
* [setHandshakeApplicationProtocolSelector()](/Java/SSLSocket/setHandshakeApplicationProtocolSelector)
* [setNeedClientAuth()](/Java/SSLSocket/setNeedClientAuth)
* [setSSLParameters()](/Java/SSLSocket/setSSLParameters)
* [setUseClientMode()](/Java/SSLSocket/setUseClientMode)
* [setWantClientAuth()](/Java/SSLSocket/setWantClientAuth)
* [startHandshake()](/Java/SSLSocket/startHandshake)

## Ejemplo
~~~java
{{ site.data.Java.S.SSLSocket.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
