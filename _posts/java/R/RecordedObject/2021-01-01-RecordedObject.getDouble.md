---
title: RecordedObject.getDouble()
permalink: Java/RecordedObject/getDouble
date: 2021-01-11
key: JavaJava.R.RecordedObject
category: java
tags: ['java se', 'jdk.jfr.consumer', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RecordedObject.metodos valor="getDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final double getDouble(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RecordedObject](/Java/RecordedObject/)

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