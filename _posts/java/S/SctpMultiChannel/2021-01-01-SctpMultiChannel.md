---
title: SctpMultiChannel
permalink: Java/SctpMultiChannel
date: 2021-01-11
key: JavaJava.S.SctpMultiChannel
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SctpMultiChannel.description }}

## Sintaxis
~~~java
public abstract class SctpMultiChannel extends AbstractSelectableChannel
~~~

## Constructores
* [SctpMultiChannel()](/Java/SctpMultiChannel/SctpMultiChannel/)

## Métodos
* [associations()](/Java/SctpMultiChannel/associations)
* [bind()](/Java/SctpMultiChannel/bind)
* [bindAddress()](/Java/SctpMultiChannel/bindAddress)
* [branch()](/Java/SctpMultiChannel/branch)
* [getAllLocalAddresses()](/Java/SctpMultiChannel/getAllLocalAddresses)
* [getOption()](/Java/SctpMultiChannel/getOption)
* [getRemoteAddresses()](/Java/SctpMultiChannel/getRemoteAddresses)
* [open()](/Java/SctpMultiChannel/open)
* [receive()](/Java/SctpMultiChannel/receive)
* [send()](/Java/SctpMultiChannel/send)
* [setOption()](/Java/SctpMultiChannel/setOption)
* [shutdown()](/Java/SctpMultiChannel/shutdown)
* [supportedOptions()](/Java/SctpMultiChannel/supportedOptions)
* [unbindAddress()](/Java/SctpMultiChannel/unbindAddress)
* [validOps()](/Java/SctpMultiChannel/validOps)

## Ejemplo
~~~java
{{ site.data.Java.S.SctpMultiChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SctpMultiChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
