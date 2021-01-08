---
title: SctpServerChannel
permalink: Java/SctpServerChannel
date: 2021-01-04
key: JavaJava.S.SctpServerChannel
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SctpServerChannel.description }}

## Sintaxis
~~~java
public abstract class SctpServerChannel extends AbstractSelectableChannel
~~~

## Constructores
* [SctpServerChannel()](/Java/SctpServerChannel/SctpServerChannel/)

## Métodos
* [accept()](/Java/SctpServerChannel/accept)
* [bind()](/Java/SctpServerChannel/bind)
* [bindAddress()](/Java/SctpServerChannel/bindAddress)
* [getAllLocalAddresses()](/Java/SctpServerChannel/getAllLocalAddresses)
* [getOption()](/Java/SctpServerChannel/getOption)
* [open()](/Java/SctpServerChannel/open)
* [setOption()](/Java/SctpServerChannel/setOption)
* [supportedOptions()](/Java/SctpServerChannel/supportedOptions)
* [unbindAddress()](/Java/SctpServerChannel/unbindAddress)
* [validOps()](/Java/SctpServerChannel/validOps)

## Ejemplo
~~~java
{{ site.data.Java.S.SctpServerChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SctpServerChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
