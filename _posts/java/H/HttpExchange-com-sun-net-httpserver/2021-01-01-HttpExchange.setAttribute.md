---
title: HttpExchange.setAttribute()
permalink: Java/HttpExchange-com-sun-net-httpserver/setAttribute
date: 2021-01-11
key: JavaJava.H.HttpExchange-com-sun-net-httpserver
category: java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpExchange-com-sun-net-httpserver.metodos valor="setAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setAttribute(String name, Object value)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[HttpExchange](/Java/HttpExchange-com-sun-net-httpserver/)

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
