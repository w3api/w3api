---
title: ServerSocketFactory.createServerSocket()
permalink: /Java/ServerSocketFactory/createServerSocket/
date: 2021-01-11
key: Java.S.ServerSocketFactory
category: Java
tags: ['java se', 'javax.net', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServerSocketFactory.metodos valor="createServerSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ServerSocket createServerSocket() throws IOException
public abstract ServerSocket createServerSocket(int port) throws IOException
public abstract ServerSocket createServerSocket(int port, int backlog) throws IOException
public abstract ServerSocket createServerSocket(int port, int backlog, InetAddress ifAddress) throws IOException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **int backlog**,  {% include w3api/param_description.html metodo=_dato parametro="int backlog" %}
* **InetAddress ifAddress**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress ifAddress" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[ServerSocketFactory](/Java/ServerSocketFactory/)

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
