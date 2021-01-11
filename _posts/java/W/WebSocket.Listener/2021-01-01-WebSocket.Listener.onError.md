---
title: WebSocket.Listener.onError()
permalink: Java/WebSocket/Listener/onError
date: 2021-01-11
key: JavaJava.W.WebSocket.Listener
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebSocket.Listener.metodos valor="onError" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void onError(WebSocket webSocket, Throwable error)
~~~

## Parámetros
* **Throwable error**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable error" %}
* **WebSocket webSocket**,  {% include w3api/param_description.html metodo=_dato parametro="WebSocket webSocket" %}

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
