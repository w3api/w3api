---
title: WebSocket.Listener.onBinary()
permalink: Java/WebSocket/Listener/onBinary
date: 2021-01-04
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
* **WebSocket.MessagePart part**,  {% include w3api/param_description.html metodo=_data parametro="WebSocket.MessagePart part" %}
* **WebSocket webSocket**,  {% include w3api/param_description.html metodo=_data parametro="WebSocket webSocket" %}
* **ByteBuffer message**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer message" %}

## Clase Padre
[WebSocket.Listener](/Java/WebSocket/Listener/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebSocket.Listener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
