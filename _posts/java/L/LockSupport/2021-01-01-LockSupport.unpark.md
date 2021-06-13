---
title: LockSupport.unpark()
permalink: Java/LockSupport/unpark
date: 2021-01-11
key: Java.L.LockSupport
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LockSupport.metodos valor="unpark" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void unpark(Thread thread)
~~~

## Parámetros
* **Thread thread**,  {% include w3api/param_description.html metodo=_dato parametro="Thread thread" %}

## Clase Padre
[LockSupport](/Java/LockSupport/)

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
