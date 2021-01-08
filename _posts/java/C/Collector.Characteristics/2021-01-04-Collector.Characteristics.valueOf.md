---
title: Collector.Characteristics.valueOf()
permalink: Java/Collector/Characteristics/valueOf
date: 2021-01-04
key: JavaJava.C.Collector.Characteristics
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collector.Characteristics.metodos valor="valueOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Collector.Characteristics valueOf(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Collector.Characteristics](/Java/Collector/Characteristics/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Collector.Characteristics.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
