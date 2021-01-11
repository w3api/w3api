---
title: SocketImpl.connect()
permalink: Java/SocketImpl/connect
date: 2021-01-11
key: JavaJava.S.SocketImpl
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketImpl.metodos valor="connect" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void connect(String host, int port) throws IOException
protected abstract void connect(InetAddress address, int port) throws IOException
protected abstract void connect(SocketAddress address, int timeout) throws IOException
~~~

## Parámetros
* **int timeout**,  {% include w3api/param_description.html metodo=_dato parametro="int timeout" %}
* **InetAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress address" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **SocketAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress address" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[SocketImpl](/Java/SocketImpl/)

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
