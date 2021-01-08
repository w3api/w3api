---
title: WebSocket.sendText()
permalink: Java/WebSocket/sendText
date: 2021-01-04
key: JavaJava.W.WebSocket
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebSocket.metodos valor="sendText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletableFuture<WebSocket> sendText(CharSequence message, boolean isLast)
~~~

## Parámetros
* **CharSequence message**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence message" %}
* **boolean isLast**,  {% include w3api/param_description.html metodo=_data parametro="boolean isLast" %}

## Clase Padre
[WebSocket](/Java/WebSocket/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WebSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
