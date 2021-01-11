---
title: AsynchronousServerSocketChannel.setOption()
permalink: Java/AsynchronousServerSocketChannel/setOption
date: 2021-01-11
key: JavaJava.A.AsynchronousServerSocketChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AsynchronousServerSocketChannel.metodos valor="setOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <T> AsynchronousServerSocketChannel setOption(SocketOption<T> name, T value)
~~~

## Parámetros
* **SocketOption&lt;T&gt; name**,  {% include w3api/param_description.html metodo=_dato parametro="SocketOption<T> name" %}
* **T value**,  {% include w3api/param_description.html metodo=_dato parametro="T value" %}

## Clase Padre
[AsynchronousServerSocketChannel](/Java/AsynchronousServerSocketChannel/)

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
