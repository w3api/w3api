---
title: HttpsServer.create()
permalink: Java/HttpsServer/create
date: 2021-01-11
key: JavaJava.H.HttpsServer
category: java
tags: ['java se', 'com.sun.net.httpserver', 'jdk.httpserver', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpsServer.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static HttpsServer create() throws IOException
public static HttpsServer create(InetSocketAddress addr, int backlog) throws IOException
~~~

## Parámetros
* **int backlog**,  {% include w3api/param_description.html metodo=_dato parametro="int backlog" %}
* **InetSocketAddress addr**,  {% include w3api/param_description.html metodo=_dato parametro="InetSocketAddress addr" %}

## Excepciones
[BindException](/Java/BindException/), [IOException](/Java/IOException/)

## Clase Padre
[HttpsServer](/Java/HttpsServer/)

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
