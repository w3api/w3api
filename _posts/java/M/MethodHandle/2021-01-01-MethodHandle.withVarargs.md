---
title: MethodHandle.withVarargs()
permalink: /Java/MethodHandle/withVarargs/
date: 2021-01-11
key: Java.M.MethodHandle
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodHandle.metodos valor="withVarargs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodHandle withVarargs(boolean makeVarargs)
~~~

## Parámetros
* **boolean makeVarargs**,  {% include w3api/param_description.html metodo=_dato parametro="boolean makeVarargs" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MethodHandle](/Java/MethodHandle/)

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
