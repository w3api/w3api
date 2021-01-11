---
title: ThreadGroup.ThreadGroup()
permalink: Java/ThreadGroup/ThreadGroup
date: 2021-01-11
key: JavaJava.T.ThreadGroup
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadGroup.constructores valor="ThreadGroup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ThreadGroup(String name)
public ThreadGroup(ThreadGroup parent, String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **ThreadGroup parent**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadGroup parent" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

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
