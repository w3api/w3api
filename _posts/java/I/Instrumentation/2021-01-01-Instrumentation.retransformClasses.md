---
title: Instrumentation.retransformClasses()
permalink: Java/Instrumentation/retransformClasses
date: 2021-01-11
key: JavaJava.I.Instrumentation
category: java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Instrumentation.metodos valor="retransformClasses" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void retransformClasses(Class<?>... classes) throws UnmodifiableClassException
~~~

## Parámetros
* **Class&lt;?&gt;... classes**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>... classes" %}

## Excepciones
[UnmodifiableClassException](/Java/UnmodifiableClassException/), [NullPointerException](/Java/NullPointerException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
