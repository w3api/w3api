---
title: SSLServerSocket.SSLServerSocket()
permalink: /Java/SSLServerSocket/SSLServerSocket/
date: 2021-01-11
key: Java.S.SSLServerSocket
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLServerSocket.constructores valor="SSLServerSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected SSLServerSocket() throws IOException
protected SSLServerSocket(int port) throws IOException
protected SSLServerSocket(int port, int backlog) throws IOException
protected SSLServerSocket(int port, int backlog, InetAddress address) throws IOException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **int backlog**,  {% include w3api/param_description.html metodo=_dato parametro="int backlog" %}
* **InetAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress address" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[SSLServerSocket](/Java/SSLServerSocket/)

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
