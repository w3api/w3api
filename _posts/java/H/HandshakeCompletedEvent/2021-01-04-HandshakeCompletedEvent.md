---
title: HandshakeCompletedEvent
permalink: Java/HandshakeCompletedEvent
date: 2021-01-04
key: JavaJava.H.HandshakeCompletedEvent
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HandshakeCompletedEvent.description }}

## Sintaxis
~~~java
public class HandshakeCompletedEvent extends EventObject
~~~

## Constructores
* [HandshakeCompletedEvent()](/Java/HandshakeCompletedEvent/HandshakeCompletedEvent/)

## Métodos
* [getCipherSuite()](/Java/HandshakeCompletedEvent/getCipherSuite)
* [getLocalCertificates()](/Java/HandshakeCompletedEvent/getLocalCertificates)
* [getLocalPrincipal()](/Java/HandshakeCompletedEvent/getLocalPrincipal)
* [getPeerCertificateChain()](/Java/HandshakeCompletedEvent/getPeerCertificateChain)
* [getPeerCertificates()](/Java/HandshakeCompletedEvent/getPeerCertificates)
* [getPeerPrincipal()](/Java/HandshakeCompletedEvent/getPeerPrincipal)
* [getSession()](/Java/HandshakeCompletedEvent/getSession)
* [getSocket()](/Java/HandshakeCompletedEvent/getSocket)

## Ejemplo
~~~java
{{ site.data.Java.H.HandshakeCompletedEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HandshakeCompletedEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
