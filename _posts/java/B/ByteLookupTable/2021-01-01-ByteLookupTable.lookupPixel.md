---
title: ByteLookupTable.lookupPixel()
permalink: Java/ByteLookupTable/lookupPixel
date: 2021-01-11
key: JavaJava.B.ByteLookupTable
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteLookupTable.metodos valor="lookupPixel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public byte[] lookupPixel(byte[] src, byte[] dst)
public int[] lookupPixel(int[] src, int[] dst)
~~~

## Parámetros
* **int[] src**,  {% include w3api/param_description.html metodo=_dato parametro="int[] src" %}
* **byte[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] dst" %}
* **byte[] src**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] src" %}
* **int[] dst**,  {% include w3api/param_description.html metodo=_dato parametro="int[] dst" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[ByteLookupTable](/Java/ByteLookupTable/)

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
