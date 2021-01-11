---
title: SocketImpl.bind()
permalink: Java/SocketImpl/bind
date: 2021-01-11
key: JavaJava.S.SocketImpl
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketImpl.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void bind(InetAddress host, int port) throws IOException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **InetAddress host**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress host" %}

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
