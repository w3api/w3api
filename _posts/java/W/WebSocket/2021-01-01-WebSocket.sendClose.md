---
title: WebSocket.sendClose()
permalink: /Java/WebSocket/sendClose/
date: 2021-01-11
key: Java.W.WebSocket
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebSocket.metodos valor="sendClose" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletableFuture<WebSocket> sendClose(int statusCode, String reason)
~~~

## Parámetros
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **int statusCode**,  {% include w3api/param_description.html metodo=_dato parametro="int statusCode" %}

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
