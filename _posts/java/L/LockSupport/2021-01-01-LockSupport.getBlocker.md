---
title: LockSupport.getBlocker()
permalink: Java/LockSupport/getBlocker
date: 2021-01-11
key: JavaJava.L.LockSupport
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LockSupport.metodos valor="getBlocker" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Object getBlocker(Thread t)
~~~

## Parámetros
* **Thread t**,  {% include w3api/param_description.html metodo=_dato parametro="Thread t" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
