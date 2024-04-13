---
title: SSLSocket.SSLSocket()
permalink: /Java/SSLSocket/SSLSocket/
date: 2021-01-11
key: Java.S.SSLSocket
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLSocket.constructores valor="SSLSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected SSLSocket()
protected SSLSocket(String host, int port) throws IOException, UnknownHostException
protected SSLSocket(String host, int port, InetAddress clientAddress, int clientPort) throws IOException, UnknownHostException
protected SSLSocket(InetAddress address, int port) throws IOException
protected SSLSocket(InetAddress address, int port, InetAddress clientAddress, int clientPort) throws IOException
~~~

## Parámetros
* **InetAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress address" %}
* **int clientPort**,  {% include w3api/param_description.html metodo=_dato parametro="int clientPort" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **InetAddress clientAddress**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress clientAddress" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [UnknownHostException](/Java/UnknownHostException/)

## Clase Padre
[SSLSocket](/Java/SSLSocket/)

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
