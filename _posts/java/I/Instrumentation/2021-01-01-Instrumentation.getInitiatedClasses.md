---
title: Instrumentation.getInitiatedClasses()
permalink: Java/Instrumentation/getInitiatedClasses
date: 2021-01-11
key: JavaJava.I.Instrumentation
category: java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Instrumentation.metodos valor="getInitiatedClasses" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Class[] getInitiatedClasses(ClassLoader loader)
~~~

## Parámetros
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}

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
