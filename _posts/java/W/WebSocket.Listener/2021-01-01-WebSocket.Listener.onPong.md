---
title: WebSocket.Listener.onPong()
permalink: /Java/WebSocket/Listener/onPong/
date: 2021-01-11
key: Java.W.WebSocket.Listener
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebSocket.Listener.metodos valor="onPong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default CompletionStage<?> onPong(WebSocket webSocket, ByteBuffer message)
~~~

## Parámetros
* **WebSocket webSocket**,  {% include w3api/param_description.html metodo=_dato parametro="WebSocket webSocket" %}
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
