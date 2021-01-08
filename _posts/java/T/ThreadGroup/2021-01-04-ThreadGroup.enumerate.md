---
title: ThreadGroup.enumerate()
permalink: Java/ThreadGroup/enumerate
date: 2021-01-04
key: JavaJava.T.ThreadGroup
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadGroup.metodos valor="enumerate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int enumerate(Thread[] list)
public int enumerate(Thread[] list, boolean recurse)
public int enumerate(ThreadGroup[] list)
public int enumerate(ThreadGroup[] list, boolean recurse)
~~~

## Parámetros
* **boolean recurse**,  {% include w3api/param_description.html metodo=_data parametro="boolean recurse" %}
* **Thread[] list**,  {% include w3api/param_description.html metodo=_data parametro="Thread[] list" %}
* **ThreadGroup[] list**,  {% include w3api/param_description.html metodo=_data parametro="ThreadGroup[] list" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[ThreadGroup](/Java/ThreadGroup/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadGroup.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
