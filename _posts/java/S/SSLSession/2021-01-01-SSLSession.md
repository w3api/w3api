---
title: SSLSession
permalink: Java/SSLSession
date: 2021-01-11
key: JavaJava.S.SSLSession
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SSLSession.description }}

## Sintaxis
~~~java
public interface SSLSession
~~~

## Métodos
* [getApplicationBufferSize()](/Java/SSLSession/getApplicationBufferSize)
* [getCipherSuite()](/Java/SSLSession/getCipherSuite)
* [getCreationTime()](/Java/SSLSession/getCreationTime)
* [getId()](/Java/SSLSession/getId)
* [getLastAccessedTime()](/Java/SSLSession/getLastAccessedTime)
* [getLocalCertificates()](/Java/SSLSession/getLocalCertificates)
* [getLocalPrincipal()](/Java/SSLSession/getLocalPrincipal)
* [getPacketBufferSize()](/Java/SSLSession/getPacketBufferSize)
* [getPeerCertificateChain()](/Java/SSLSession/getPeerCertificateChain)
* [getPeerCertificates()](/Java/SSLSession/getPeerCertificates)
* [getPeerHost()](/Java/SSLSession/getPeerHost)
* [getPeerPort()](/Java/SSLSession/getPeerPort)
* [getPeerPrincipal()](/Java/SSLSession/getPeerPrincipal)
* [getProtocol()](/Java/SSLSession/getProtocol)
* [getSessionContext()](/Java/SSLSession/getSessionContext)
* [getValue()](/Java/SSLSession/getValue)
* [getValueNames()](/Java/SSLSession/getValueNames)
* [invalidate()](/Java/SSLSession/invalidate)
* [isValid()](/Java/SSLSession/isValid)
* [putValue()](/Java/SSLSession/putValue)
* [removeValue()](/Java/SSLSession/removeValue)

## Ejemplo
~~~java
{{ site.data.Java.S.SSLSession.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLSession.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
