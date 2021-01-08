---
title: ServerSocketFactory.createServerSocket()
permalink: Java/ServerSocketFactory/createServerSocket
date: 2021-01-04
key: JavaJava.S.ServerSocketFactory
category: java
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
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **InetAddress ifAddress**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress ifAddress" %}
* **int backlog**,  {% include w3api/param_description.html metodo=_data parametro="int backlog" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[ServerSocketFactory](/Java/ServerSocketFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServerSocketFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
