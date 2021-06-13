---
title: WebSocket.sendBinary()
permalink: /Java/WebSocket/sendBinary/
date: 2021-01-11
key: Java.W.WebSocket
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebSocket.metodos valor="sendBinary" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletableFuture<WebSocket> sendBinary(ByteBuffer message, boolean isLast)
~~~

## Parámetros
* **boolean isLast**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isLast" %}
* **ByteBuffer message**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer message" %}

## Clase Padre
[WebSocket](/Java/WebSocket/)

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
