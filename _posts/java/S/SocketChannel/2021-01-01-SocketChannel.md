---
title: SocketChannel
permalink: /Java/SocketChannel/
date: 2021-01-11
key: Java.S.SocketChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SocketChannel.description }}

## Sintaxis
~~~java
public abstract class SocketChannel extends AbstractSelectableChannel implements ByteChannel, ScatteringByteChannel, GatheringByteChannel, NetworkChannel
~~~

## Constructores
* [SocketChannel()](/Java/SocketChannel/SocketChannel/)

## Métodos
* [bind()](/Java/SocketChannel/bind)
* [connect()](/Java/SocketChannel/connect)
* [finishConnect()](/Java/SocketChannel/finishConnect)
* [getLocalAddress()](/Java/SocketChannel/getLocalAddress)
* [getRemoteAddress()](/Java/SocketChannel/getRemoteAddress)
* [isConnected()](/Java/SocketChannel/isConnected)
* [isConnectionPending()](/Java/SocketChannel/isConnectionPending)
* [open()](/Java/SocketChannel/open)
* [read()](/Java/SocketChannel/read)
* [setOption()](/Java/SocketChannel/setOption)
* [shutdownInput()](/Java/SocketChannel/shutdownInput)
* [shutdownOutput()](/Java/SocketChannel/shutdownOutput)
* [socket()](/Java/SocketChannel/socket)
* [validOps()](/Java/SocketChannel/validOps)
* [write()](/Java/SocketChannel/write)

## Ejemplo
~~~java
{{ site.data.Java.S.SocketChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SocketChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
