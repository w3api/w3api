---
title: SocketImpl.accept()
permalink: Java/SocketImpl/accept
date: 2021-01-11
key: JavaJava.S.SocketImpl
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketImpl.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void accept(SocketImpl s) throws IOException
~~~

## Parámetros
* **SocketImpl s**,  {% include w3api/param_description.html metodo=_dato parametro="SocketImpl s" %}

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
