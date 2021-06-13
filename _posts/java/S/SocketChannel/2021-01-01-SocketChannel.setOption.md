---
title: SocketChannel.setOption()
permalink: /Java/SocketChannel/setOption/
date: 2021-01-11
key: Java.S.SocketChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketChannel.metodos valor="setOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <T> SocketChannel setOption(SocketOption<T> name, T value)
~~~

## Parámetros
* **SocketOption&lt;T&gt; name**,  {% include w3api/param_description.html metodo=_dato parametro="SocketOption<T> name" %}
* **T value**,  {% include w3api/param_description.html metodo=_dato parametro="T value" %}

## Clase Padre
[SocketChannel](/Java/SocketChannel/)

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
