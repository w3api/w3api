---
title: WebSocket.Listener
permalink: Java/WebSocket/Listener
date: 2021-01-04
key: JavaJava.W.WebSocket.Listener
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WebSocket.Listener.description }}

## Sintaxis
~~~java
public static interface WebSocket.Listener
~~~

## Métodos
* [onBinary()](/Java/WebSocket/Listener/onBinary)
* [onClose()](/Java/WebSocket/Listener/onClose)
* [onError()](/Java/WebSocket/Listener/onError)
* [onOpen()](/Java/WebSocket/Listener/onOpen)
* [onPing()](/Java/WebSocket/Listener/onPing)
* [onPong()](/Java/WebSocket/Listener/onPong)
* [onText()](/Java/WebSocket/Listener/onText)

## Ejemplo
~~~java
{{ site.data.Java.W.WebSocket.Listener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebSocket.Listener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
