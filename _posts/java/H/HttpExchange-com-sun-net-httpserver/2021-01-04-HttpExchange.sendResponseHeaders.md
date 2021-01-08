---
title: HttpExchange.sendResponseHeaders()
permalink: Java/HttpExchange-com-sun-net-httpserver/sendResponseHeaders
date: 2021-01-04
key: JavaJava.H.HttpExchange-com-sun-net-httpserver
category: java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpExchange-com-sun-net-httpserver.metodos valor="sendResponseHeaders" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void sendResponseHeaders(int rCode, long responseLength) throws IOException
~~~

## Parámetros
* **long responseLength**,  {% include w3api/param_description.html metodo=_data parametro="long responseLength" %}
* **int rCode**,  {% include w3api/param_description.html metodo=_data parametro="int rCode" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[HttpExchange](/Java/HttpExchange-com-sun-net-httpserver/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpExchange-com-sun-net-httpserver.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
