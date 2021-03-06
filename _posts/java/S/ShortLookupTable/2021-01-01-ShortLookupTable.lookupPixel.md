---
title: ShortLookupTable.lookupPixel()
permalink: /Java/ShortLookupTable/lookupPixel/
date: 2021-01-11
key: Java.S.ShortLookupTable
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ShortLookupTable.metodos valor="lookupPixel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int[] lookupPixel(int[] src, int[] dst)
public short[] lookupPixel(short[] src, short[] dst)
~~~

## Parámetros
* **short[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="short[] dst" %}
* **int[] src**,  {% include w3api/param_description.html metodo=_dato parametro="int[] src" %}
* **int[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="int[] dst" %}
* **short[] src**,  {% include w3api/param_description.html metodo=_dato parametro="short[] src" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[ShortLookupTable](/Java/ShortLookupTable/)

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
