---
title: WebSocket
permalink: /Java/WebSocket/
date: 2021-01-11
key: Java.W.WebSocket
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WebSocket.description }}

## Sintaxis
~~~java
public interface WebSocket
~~~

## Campos
* [NORMAL_CLOSURE](/Java/WebSocket/NORMAL_CLOSURE/)

## Métodos
* [abort()](/Java/WebSocket/abort/)
* [getSubprotocol()](/Java/WebSocket/getSubprotocol/)
* [isInputClosed()](/Java/WebSocket/isInputClosed/)
* [isOutputClosed()](/Java/WebSocket/isOutputClosed/)
* [request()](/Java/WebSocket/request/)
* [sendBinary()](/Java/WebSocket/sendBinary/)
* [sendClose()](/Java/WebSocket/sendClose/)
* [sendPing()](/Java/WebSocket/sendPing/)
* [sendPong()](/Java/WebSocket/sendPong/)
* [sendText()](/Java/WebSocket/sendText/)

## Ejemplo
~~~java
{{ site.data.Java.W.WebSocket.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
