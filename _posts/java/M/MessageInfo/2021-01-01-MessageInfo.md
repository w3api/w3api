---
title: MessageInfo
permalink: /Java/MessageInfo/
date: 2021-01-11
key: Java.M.MessageInfo
category: Java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MessageInfo.description }}

## Sintaxis
~~~java
public abstract class MessageInfo extends Object
~~~

## Constructores
* [MessageInfo()](/Java/MessageInfo/MessageInfo/)

## Métodos
* [address()](/Java/MessageInfo/address)
* [association()](/Java/MessageInfo/association)
* [bytes()](/Java/MessageInfo/bytes)
* [complete()](/Java/MessageInfo/complete)
* [createOutgoing()](/Java/MessageInfo/createOutgoing)
* [isComplete()](/Java/MessageInfo/isComplete)
* [isUnordered()](/Java/MessageInfo/isUnordered)
* [payloadProtocolID()](/Java/MessageInfo/payloadProtocolID)
* [streamNumber()](/Java/MessageInfo/streamNumber)
* [timeToLive()](/Java/MessageInfo/timeToLive)
* [unordered()](/Java/MessageInfo/unordered)

## Ejemplo
~~~java
{{ site.data.Java.M.MessageInfo.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MessageInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
