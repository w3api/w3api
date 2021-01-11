---
title: SSLEngine
permalink: Java/SSLEngine
date: 2021-01-11
key: JavaJava.S.SSLEngine
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SSLEngine.description }}

## Sintaxis
~~~java
public abstract class SSLEngine extends Object
~~~

## Constructores
* [SSLEngine()](/Java/SSLEngine/SSLEngine/)

## Métodos
* [beginHandshake()](/Java/SSLEngine/beginHandshake)
* [closeInbound()](/Java/SSLEngine/closeInbound)
* [closeOutbound()](/Java/SSLEngine/closeOutbound)
* [getApplicationProtocol()](/Java/SSLEngine/getApplicationProtocol)
* [getDelegatedTask()](/Java/SSLEngine/getDelegatedTask)
* [getEnabledCipherSuites()](/Java/SSLEngine/getEnabledCipherSuites)
* [getEnabledProtocols()](/Java/SSLEngine/getEnabledProtocols)
* [getEnableSessionCreation()](/Java/SSLEngine/getEnableSessionCreation)
* [getHandshakeApplicationProtocol()](/Java/SSLEngine/getHandshakeApplicationProtocol)
* [getHandshakeApplicationProtocolSelector()](/Java/SSLEngine/getHandshakeApplicationProtocolSelector)
* [getHandshakeSession()](/Java/SSLEngine/getHandshakeSession)
* [getHandshakeStatus()](/Java/SSLEngine/getHandshakeStatus)
* [getNeedClientAuth()](/Java/SSLEngine/getNeedClientAuth)
* [getPeerHost()](/Java/SSLEngine/getPeerHost)
* [getPeerPort()](/Java/SSLEngine/getPeerPort)
* [getSession()](/Java/SSLEngine/getSession)
* [getSSLParameters()](/Java/SSLEngine/getSSLParameters)
* [getSupportedCipherSuites()](/Java/SSLEngine/getSupportedCipherSuites)
* [getSupportedProtocols()](/Java/SSLEngine/getSupportedProtocols)
* [getUseClientMode()](/Java/SSLEngine/getUseClientMode)
* [getWantClientAuth()](/Java/SSLEngine/getWantClientAuth)
* [isInboundDone()](/Java/SSLEngine/isInboundDone)
* [isOutboundDone()](/Java/SSLEngine/isOutboundDone)
* [setEnabledCipherSuites()](/Java/SSLEngine/setEnabledCipherSuites)
* [setEnabledProtocols()](/Java/SSLEngine/setEnabledProtocols)
* [setEnableSessionCreation()](/Java/SSLEngine/setEnableSessionCreation)
* [setHandshakeApplicationProtocolSelector()](/Java/SSLEngine/setHandshakeApplicationProtocolSelector)
* [setNeedClientAuth()](/Java/SSLEngine/setNeedClientAuth)
* [setSSLParameters()](/Java/SSLEngine/setSSLParameters)
* [setUseClientMode()](/Java/SSLEngine/setUseClientMode)
* [setWantClientAuth()](/Java/SSLEngine/setWantClientAuth)
* [unwrap()](/Java/SSLEngine/unwrap)
* [wrap()](/Java/SSLEngine/wrap)

## Ejemplo
~~~java
{{ site.data.Java.S.SSLEngine.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLEngine.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
