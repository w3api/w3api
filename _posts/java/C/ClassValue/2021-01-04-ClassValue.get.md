---
title: ClassValue.get()
permalink: Java/ClassValue/get
date: 2021-01-04
key: JavaJava.C.ClassValue
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassValue.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public T get(Class<?> type)
~~~

## Parámetros
* **Class&lt;?&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> type" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ClassValue](/Java/ClassValue/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassValue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
