---
title: SendFailedNotification
permalink: Java/SendFailedNotification
date: 2021-01-11
key: JavaJava.S.SendFailedNotification
category: java
tags: ['java se', 'com.sun.nio.sctp', 'jdk.sctp', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SendFailedNotification.description }}

## Sintaxis
~~~java
public abstract class SendFailedNotification extends Object implements Notification
~~~

## Constructores
* [SendFailedNotification()](/Java/SendFailedNotification/SendFailedNotification/)

## Métodos
* [address()](/Java/SendFailedNotification/address)
* [association()](/Java/SendFailedNotification/association)
* [buffer()](/Java/SendFailedNotification/buffer)
* [errorCode()](/Java/SendFailedNotification/errorCode)
* [streamNumber()](/Java/SendFailedNotification/streamNumber)

## Ejemplo
~~~java
{{ site.data.Java.S.SendFailedNotification.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SendFailedNotification.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
