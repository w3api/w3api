---
title: Instrumentation.addTransformer()
permalink: /Java/Instrumentation/addTransformer/
date: 2021-01-11
key: Java.I.Instrumentation
category: Java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Instrumentation.metodos valor="addTransformer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addTransformer(ClassFileTransformer transformer)
void addTransformer(ClassFileTransformer transformer, boolean canRetransform)
~~~

## Parámetros
* **ClassFileTransformer transformer**,  {% include w3api/param_description.html metodo=_dato parametro="ClassFileTransformer transformer" %}
* **boolean canRetransform**,  {% include w3api/param_description.html metodo=_dato parametro="boolean canRetransform" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

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
