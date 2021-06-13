---
title: ByteLookupTable.ByteLookupTable()
permalink: /Java/ByteLookupTable/ByteLookupTable/
date: 2021-01-11
key: Java.B.ByteLookupTable
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.ByteLookupTable.constructores valor="ByteLookupTable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ByteLookupTable(int offset, byte[] data)
public ByteLookupTable(int offset, byte[][] data)
~~~

## Parámetros
* **byte[] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] data" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **byte[][] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[][] data" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
