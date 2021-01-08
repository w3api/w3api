---
title: Instrumentation.removeTransformer()
permalink: Java/Instrumentation/removeTransformer
date: 2021-01-04
key: JavaJava.I.Instrumentation
category: java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Instrumentation.metodos valor="removeTransformer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean removeTransformer(ClassFileTransformer transformer)
~~~

## Parámetros
* **ClassFileTransformer transformer**,  {% include w3api/param_description.html metodo=_data parametro="ClassFileTransformer transformer" %}

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
{%- for _ldc in site.data.Java.I.Instrumentation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
