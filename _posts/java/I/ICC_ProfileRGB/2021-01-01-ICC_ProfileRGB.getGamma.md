---
title: ICC_ProfileRGB.getGamma()
permalink: /Java/ICC_ProfileRGB/getGamma/
date: 2021-01-11
key: Java.I.ICC_ProfileRGB
category: Java
tags: ['java se', 'java.awt.color', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ICC_ProfileRGB.metodos valor="getGamma" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public float getGamma(int component)
~~~

## Parámetros
* **int component**,  {% include w3api/param_description.html metodo=_dato parametro="int component" %}

## Excepciones
[ProfileDataException](/Java/ProfileDataException/)

## Clase Padre
[ICC_ProfileRGB](/Java/ICC_ProfileRGB/)

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
