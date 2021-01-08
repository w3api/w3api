---
title: SSLSocket.SSLSocket()
permalink: Java/SSLSocket/SSLSocket
date: 2021-01-04
key: JavaJava.S.SSLSocket
category: java
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
* **String host**,  {% include w3api/param_description.html metodo=_data parametro="String host" %}
* **InetAddress clientAddress**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress clientAddress" %}
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **int clientPort**,  {% include w3api/param_description.html metodo=_data parametro="int clientPort" %}
* **InetAddress address**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress address" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnknownHostException](/Java/UnknownHostException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[SSLSocket](/Java/SSLSocket/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
