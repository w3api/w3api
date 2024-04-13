---
title: Instrumentation.isModifiableClass()
permalink: /Java/Instrumentation/isModifiableClass/
date: 2021-01-11
key: Java.I.Instrumentation
category: Java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Instrumentation.metodos valor="isModifiableClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isModifiableClass(Class<?> theClass)
~~~

## Parámetros
* **Class&lt;?&gt; theClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> theClass" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Instrumentation](/Java/Instrumentation/)

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
