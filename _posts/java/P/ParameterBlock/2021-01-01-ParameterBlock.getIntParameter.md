---
title: ParameterBlock.getIntParameter()
permalink: /Java/ParameterBlock/getIntParameter/
date: 2021-01-11
key: Java.P.ParameterBlock
category: Java
tags: ['java se', 'java.awt.image.renderable', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ParameterBlock.metodos valor="getIntParameter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getIntParameter(int index)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ParameterBlock](/Java/ParameterBlock/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
