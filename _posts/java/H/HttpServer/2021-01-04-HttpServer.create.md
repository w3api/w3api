---
title: HttpServer.create()
permalink: Java/HttpServer/create
date: 2021-01-04
key: JavaJava.H.HttpServer
category: java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpServer.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static HttpServer create() throws IOException
public static HttpServer create(InetSocketAddress addr, int backlog) throws IOException
~~~

## Parámetros
* **InetSocketAddress addr**,  {% include w3api/param_description.html metodo=_data parametro="InetSocketAddress addr" %}
* **int backlog**,  {% include w3api/param_description.html metodo=_data parametro="int backlog" %}

## Excepciones
[BindException](/Java/BindException/), [IOException](/Java/IOException/)

## Clase Padre
[HttpServer](/Java/HttpServer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
