---
title: DatagramChannel
permalink: Java/DatagramChannel
date: 2021-01-11
key: JavaJava.D.DatagramChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DatagramChannel.description }}

## Sintaxis
~~~java
public abstract class DatagramChannel extends AbstractSelectableChannel implements ByteChannel, ScatteringByteChannel, GatheringByteChannel, MulticastChannel
~~~

## Constructores
* [DatagramChannel()](/Java/DatagramChannel/DatagramChannel/)

## Métodos
* [bind()](/Java/DatagramChannel/bind)
* [connect()](/Java/DatagramChannel/connect)
* [disconnect()](/Java/DatagramChannel/disconnect)
* [getLocalAddress()](/Java/DatagramChannel/getLocalAddress)
* [getRemoteAddress()](/Java/DatagramChannel/getRemoteAddress)
* [isConnected()](/Java/DatagramChannel/isConnected)
* [open()](/Java/DatagramChannel/open)
* [read()](/Java/DatagramChannel/read)
* [receive()](/Java/DatagramChannel/receive)
* [send()](/Java/DatagramChannel/send)
* [setOption()](/Java/DatagramChannel/setOption)
* [socket()](/Java/DatagramChannel/socket)
* [validOps()](/Java/DatagramChannel/validOps)
* [write()](/Java/DatagramChannel/write)

## Ejemplo
~~~java
{{ site.data.Java.D.DatagramChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatagramChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
