---
title: ServerSocket
permalink: Java/ServerSocket
date: 2021-01-04
key: JavaJava.S.ServerSocket
category: java
tags: ['java se', 'java.net', 'java.base', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ServerSocket.description }}

## Sintaxis
~~~java
public class ServerSocket extends Object implements Closeable
~~~

## Constructores
* [ServerSocket()](/Java/ServerSocket/ServerSocket/)

## Métodos
* [accept()](/Java/ServerSocket/accept)
* [bind()](/Java/ServerSocket/bind)
* [close()](/Java/ServerSocket/close)
* [getChannel()](/Java/ServerSocket/getChannel)
* [getInetAddress()](/Java/ServerSocket/getInetAddress)
* [getLocalPort()](/Java/ServerSocket/getLocalPort)
* [getLocalSocketAddress()](/Java/ServerSocket/getLocalSocketAddress)
* [getOption()](/Java/ServerSocket/getOption)
* [getReceiveBufferSize()](/Java/ServerSocket/getReceiveBufferSize)
* [getReuseAddress()](/Java/ServerSocket/getReuseAddress)
* [getSoTimeout()](/Java/ServerSocket/getSoTimeout)
* [implAccept()](/Java/ServerSocket/implAccept)
* [isBound()](/Java/ServerSocket/isBound)
* [isClosed()](/Java/ServerSocket/isClosed)
* [setOption()](/Java/ServerSocket/setOption)
* [setPerformancePreferences()](/Java/ServerSocket/setPerformancePreferences)
* [setReceiveBufferSize()](/Java/ServerSocket/setReceiveBufferSize)
* [setReuseAddress()](/Java/ServerSocket/setReuseAddress)
* [setSocketFactory()](/Java/ServerSocket/setSocketFactory)
* [setSoTimeout()](/Java/ServerSocket/setSoTimeout)
* [supportedOptions()](/Java/ServerSocket/supportedOptions)
* [toString()](/Java/ServerSocket/toString)

## Ejemplo
~~~java
{{ site.data.Java.S.ServerSocket.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServerSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
