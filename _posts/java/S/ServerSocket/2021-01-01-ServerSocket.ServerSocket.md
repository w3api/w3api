---
title: ServerSocket.ServerSocket()
permalink: /Java/ServerSocket/ServerSocket/
date: 2021-01-11
key: Java.S.ServerSocket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerSocket.constructores valor="ServerSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ServerSocket() throws IOException
public ServerSocket(int port) throws IOException
public ServerSocket(int port, int backlog) throws IOException
public ServerSocket(int port, int backlog, InetAddress bindAddr) throws IOException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **int backlog**,  {% include w3api/param_description.html metodo=_dato parametro="int backlog" %}
* **InetAddress bindAddr**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress bindAddr" %}

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
