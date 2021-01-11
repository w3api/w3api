---
title: ServerSocket.bind()
permalink: Java/ServerSocket/bind
date: 2021-01-11
key: JavaJava.S.ServerSocket
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerSocket.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void bind(SocketAddress endpoint) throws IOException
public void bind(SocketAddress endpoint, int backlog) throws IOException
~~~

## Parámetros
* **SocketAddress endpoint**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress endpoint" %}
* **int backlog**,  {% include w3api/param_description.html metodo=_dato parametro="int backlog" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[ServerSocket](/Java/ServerSocket/)

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
