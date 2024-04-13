---
title: HttpServerProvider.createHttpsServer()
permalink: /Java/HttpServerProvider/createHttpsServer/
date: 2021-01-11
key: Java.H.HttpServerProvider
category: Java
tags: ['java se', 'com.sun.net.httpserver.spi', 'jdk.httpserver', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpServerProvider.metodos valor="createHttpsServer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract HttpsServer createHttpsServer(InetSocketAddress addr, int backlog) throws IOException
~~~

## Parámetros
* **int backlog**,  {% include w3api/param_description.html metodo=_dato parametro="int backlog" %}
* **InetSocketAddress addr**,  {% include w3api/param_description.html metodo=_dato parametro="InetSocketAddress addr" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[HttpServerProvider](/Java/HttpServerProvider/)

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
