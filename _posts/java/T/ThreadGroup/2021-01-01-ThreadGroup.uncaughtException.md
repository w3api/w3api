---
title: ThreadGroup.uncaughtException()
permalink: Java/ThreadGroup/uncaughtException
date: 2021-01-11
key: JavaJava.T.ThreadGroup
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadGroup.metodos valor="uncaughtException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void uncaughtException(Thread t, Throwable e)
~~~

## Parámetros
* **Throwable e**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable e" %}
* **Thread t**,  {% include w3api/param_description.html metodo=_dato parametro="Thread t" %}

## Clase Padre
[ThreadGroup](/Java/ThreadGroup/)

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
