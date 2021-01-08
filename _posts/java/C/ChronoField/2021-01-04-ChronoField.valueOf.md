---
title: ChronoField.valueOf()
permalink: Java/ChronoField/valueOf
date: 2021-01-04
key: JavaJava.C.ChronoField
category: java
tags: ['java se', 'java.time.temporal', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoField.metodos valor="valueOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ChronoField valueOf(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ChronoField](/Java/ChronoField/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChronoField.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
