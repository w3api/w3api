---
title: ByteLookupTable.lookupPixel()
permalink: Java/ByteLookupTable/lookupPixel
date: 2021-01-04
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
* **int[] dst**,  {% include w3api/param_description.html metodo=_data parametro="int[] dst" %}
* **int[] src**,  {% include w3api/param_description.html metodo=_data parametro="int[] src" %}
* **byte[] dst**,  {% include w3api/param_description.html metodo=_data parametro="byte[] dst" %}
* **byte[] src**,  {% include w3api/param_description.html metodo=_data parametro="byte[] src" %}

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
{%- for _ldc in site.data.Java.B.ByteLookupTable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
