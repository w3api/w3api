---
title: LookupTable.lookupPixel()
permalink: /Java/LookupTable/lookupPixel/
date: 2021-01-11
key: Java.L.LookupTable
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LookupTable.metodos valor="lookupPixel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int[] lookupPixel(int[] src, int[] dest)
~~~

## Parámetros
* **int[] src**,  {% include w3api/param_description.html metodo=_dato parametro="int[] src" %}
* **int[] dest**,  {% include w3api/param_description.html metodo=_dato parametro="int[] dest" %}

## Clase Padre
[LookupTable](/Java/LookupTable/)

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
