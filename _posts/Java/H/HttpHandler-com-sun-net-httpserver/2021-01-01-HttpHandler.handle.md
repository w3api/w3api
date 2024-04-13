---
title: HttpHandler.handle()
permalink: /Java/HttpHandler-com-sun-net-httpserver/handle/
date: 2021-01-11
key: Java.H.HttpHandler-com-sun-net-httpserver
category: Java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpHandler-com-sun-net-httpserver.metodos valor="handle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void handle(HttpExchange exchange) throws IOException
~~~

## Parámetros
* **HttpExchange exchange**,  {% include w3api/param_description.html metodo=_dato parametro="HttpExchange exchange" %}

## Excepciones
[IOException](/Java/IOException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[HttpHandler](/Java/HttpHandler-com-sun-net-httpserver/)

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
