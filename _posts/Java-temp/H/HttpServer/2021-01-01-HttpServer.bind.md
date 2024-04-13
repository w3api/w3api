---
title: HttpServer.bind()
permalink: /Java/HttpServer/bind/
date: 2021-01-11
key: Java.H.HttpServer
category: Java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpServer.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void bind(InetSocketAddress addr, int backlog) throws IOException
~~~

## Parámetros
* **int backlog**,  {% include w3api/param_description.html metodo=_dato parametro="int backlog" %}
* **InetSocketAddress addr**,  {% include w3api/param_description.html metodo=_dato parametro="InetSocketAddress addr" %}

## Excepciones
[IOException](/Java/IOException/), [NullPointerException](/Java/NullPointerException/), [BindException](/Java/BindException/)

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
