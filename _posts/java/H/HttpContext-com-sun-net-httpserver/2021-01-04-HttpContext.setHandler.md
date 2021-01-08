---
title: HttpContext.setHandler()
permalink: Java/HttpContext-com-sun-net-httpserver/setHandler
date: 2021-01-04
key: JavaJava.H.HttpContext-com-sun-net-httpserver
category: java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpContext-com-sun-net-httpserver.metodos valor="setHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setHandler(HttpHandler h)
~~~

## Parámetros
* **HttpHandler h**,  {% include w3api/param_description.html metodo=_data parametro="HttpHandler h" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[HttpContext](/Java/HttpContext-com-sun-net-httpserver/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpContext-com-sun-net-httpserver.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
