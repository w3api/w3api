---
title: ThreadInfo.from()
permalink: /Java/ThreadInfo/from/
date: 2021-01-11
key: Java.T.ThreadInfo
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadInfo.metodos valor="from" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ThreadInfo from(CompositeData cd)
~~~

## Parámetros
* **CompositeData cd**,  {% include w3api/param_description.html metodo=_dato parametro="CompositeData cd" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ThreadInfo](/Java/ThreadInfo/)

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
