---
title: HttpServer.stop()
permalink: Java/HttpServer/stop
date: 2021-01-11
key: JavaJava.H.HttpServer
category: java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpServer.metodos valor="stop" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void stop(int delay)
~~~

## Parámetros
* **int delay**,  {% include w3api/param_description.html metodo=_dato parametro="int delay" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[HttpServer](/Java/HttpServer/)

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
