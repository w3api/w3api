---
title: SocketImpl.listen()
permalink: /Java/SocketImpl/listen/
date: 2021-01-11
key: Java.S.SocketImpl
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketImpl.metodos valor="listen" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void listen(int backlog) throws IOException
~~~

## Parámetros
* **int backlog**,  {% include w3api/param_description.html metodo=_dato parametro="int backlog" %}

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
