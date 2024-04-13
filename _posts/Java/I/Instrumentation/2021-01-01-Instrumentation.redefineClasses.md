---
title: Instrumentation.redefineClasses()
permalink: /Java/Instrumentation/redefineClasses/
date: 2021-01-11
key: Java.I.Instrumentation
category: Java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Instrumentation.metodos valor="redefineClasses" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void redefineClasses(ClassDefinition... definitions) throws ClassNotFoundException, UnmodifiableClassException
~~~

## Parámetros
* **ClassDefinition... definitions**,  {% include w3api/param_description.html metodo=_dato parametro="ClassDefinition... definitions" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [UnmodifiableClassException](/Java/UnmodifiableClassException/), [NullPointerException](/Java/NullPointerException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
