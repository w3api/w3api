---
title: SctpChannel
permalink: /Java/SctpChannel/
date: 2021-01-11
key: Java.S.SctpChannel
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SctpChannel.description }}

## Sintaxis
~~~java
public abstract class SctpChannel extends AbstractSelectableChannel
~~~

## Constructores
* [SctpChannel()](/Java/SctpChannel/SctpChannel/)

## Métodos
* [association()](/Java/SctpChannel/association)
* [bind()](/Java/SctpChannel/bind)
* [bindAddress()](/Java/SctpChannel/bindAddress)
* [connect()](/Java/SctpChannel/connect)
* [finishConnect()](/Java/SctpChannel/finishConnect)
* [getAllLocalAddresses()](/Java/SctpChannel/getAllLocalAddresses)
* [getOption()](/Java/SctpChannel/getOption)
* [getRemoteAddresses()](/Java/SctpChannel/getRemoteAddresses)
* [isConnectionPending()](/Java/SctpChannel/isConnectionPending)
* [open()](/Java/SctpChannel/open)
* [receive()](/Java/SctpChannel/receive)
* [send()](/Java/SctpChannel/send)
* [setOption()](/Java/SctpChannel/setOption)
* [shutdown()](/Java/SctpChannel/shutdown)
* [supportedOptions()](/Java/SctpChannel/supportedOptions)
* [unbindAddress()](/Java/SctpChannel/unbindAddress)
* [validOps()](/Java/SctpChannel/validOps)

## Ejemplo
~~~java
{{ site.data.Java.S.SctpChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SctpChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
