---
title: ThreadLocal.set()
permalink: /Java/ThreadLocal/set/
date: 2021-01-11
key: Java.T.ThreadLocal
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadLocal.metodos valor="set" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void set(T value)
~~~

## Parámetros
* **T value**,  {% include w3api/param_description.html metodo=_dato parametro="T value" %}

## Clase Padre
[ThreadLocal](/Java/ThreadLocal/)

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
