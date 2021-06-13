---
title: WebSocket.Builder.buildAsync()
permalink: /Java/WebSocket/Builder/buildAsync/
date: 2021-01-11
key: Java.W.WebSocket.Builder
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebSocket.Builder.metodos valor="buildAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletableFuture<WebSocket> buildAsync(URI uri, WebSocket.Listener listener)
~~~

## Parámetros
* **URI uri**,  {% include w3api/param_description.html metodo=_dato parametro="URI uri" %}
* **WebSocket.Listener listener**,  {% include w3api/param_description.html metodo=_dato parametro="WebSocket.Listener listener" %}

## Clase Padre
[WebSocket.Builder](/Java/WebSocket/Builder/)

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
