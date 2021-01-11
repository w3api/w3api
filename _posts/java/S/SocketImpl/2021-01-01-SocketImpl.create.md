---
title: SocketImpl.create()
permalink: Java/SocketImpl/create
date: 2021-01-11
key: JavaJava.S.SocketImpl
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketImpl.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void create(boolean stream) throws IOException
~~~

## Parámetros
* **boolean stream**,  {% include w3api/param_description.html metodo=_dato parametro="boolean stream" %}

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
