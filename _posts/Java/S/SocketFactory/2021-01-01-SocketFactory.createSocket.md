---
title: SocketFactory.createSocket()
permalink: /Java/SocketFactory/createSocket/
date: 2021-01-11
key: Java.S.SocketFactory
category: Java
tags: ['java se', 'javax.net', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketFactory.metodos valor="createSocket" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Socket createSocket() throws IOException
public abstract Socket createSocket(String host, int port) throws IOException, UnknownHostException
public abstract Socket createSocket(String host, int port, InetAddress localHost, int localPort) throws IOException, UnknownHostException
public abstract Socket createSocket(InetAddress host, int port) throws IOException
public abstract Socket createSocket(InetAddress address, int port, InetAddress localAddress, int localPort) throws IOException
~~~

## Parámetros
* **InetAddress localHost**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress localHost" %}
* **int localPort**,  {% include w3api/param_description.html metodo=_dato parametro="int localPort" %}
* **InetAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress address" %}
* **InetAddress localAddress**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress localAddress" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}
* **InetAddress host**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress host" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [UnknownHostException](/Java/UnknownHostException/)

## Clase Padre
[SocketFactory](/Java/SocketFactory/)

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
