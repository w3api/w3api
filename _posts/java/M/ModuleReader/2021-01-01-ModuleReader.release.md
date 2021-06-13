---
title: ModuleReader.release()
permalink: /Java/ModuleReader/release/
date: 2021-01-11
key: Java.M.ModuleReader
category: Java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleReader.metodos valor="release" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void release(ByteBuffer bb)
~~~

## Parámetros
* **ByteBuffer bb**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer bb" %}

## Clase Padre
[ModuleReader](/Java/ModuleReader/)

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
