---
title: WebSocket.Listener.onBinary()
permalink: Java/WebSocket/Listener/onBinary
date: 2021-01-11
key: JavaJava.W.WebSocket.Listener
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebSocket.Listener.metodos valor="onBinary" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default CompletionStage<?> onBinary(WebSocket webSocket, ByteBuffer message, WebSocket.MessagePart part)
~~~

## Parámetros
* **WebSocket webSocket**,  {% include w3api/param_description.html metodo=_dato parametro="WebSocket webSocket" %}
* **WebSocket.MessagePart part**,  {% include w3api/param_description.html metodo=_dato parametro="WebSocket.MessagePart part" %}
* **ByteBuffer message**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer message" %}

## Clase Padre
[WebSocket.Listener](/Java/WebSocket/Listener/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
