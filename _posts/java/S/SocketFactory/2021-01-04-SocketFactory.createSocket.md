---
title: SocketFactory.createSocket()
permalink: Java/SocketFactory/createSocket
date: 2021-01-04
key: JavaJava.S.SocketFactory
category: java
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
* **String host**,  {% include w3api/param_description.html metodo=_data parametro="String host" %}
* **InetAddress localAddress**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress localAddress" %}
* **int localPort**,  {% include w3api/param_description.html metodo=_data parametro="int localPort" %}
* **InetAddress localHost**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress localHost" %}
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **InetAddress host**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress host" %}
* **InetAddress address**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress address" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnknownHostException](/Java/UnknownHostException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[SocketFactory](/Java/SocketFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SocketFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
