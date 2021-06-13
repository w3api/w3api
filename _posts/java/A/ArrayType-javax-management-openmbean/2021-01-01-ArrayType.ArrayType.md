---
title: ArrayType.ArrayType()
permalink: /Java/ArrayType-javax-management-openmbean/ArrayType/
date: 2021-01-11
key: Java.A.ArrayType-javax-management-openmbean
category: Java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayType-javax-management-openmbean.constructores valor="ArrayType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ArrayType(int dimension, OpenType<?> elementType) throws OpenDataException
public ArrayType(SimpleType<?> elementType, boolean primitiveArray) throws OpenDataException
~~~

## Parámetros
* **SimpleType&lt;?&gt; elementType**,  {% include w3api/param_description.html metodo=_dato parametro="SimpleType<?> elementType" %}
* **int dimension**,  {% include w3api/param_description.html metodo=_dato parametro="int dimension" %}
* **OpenType&lt;?&gt; elementType**,  {% include w3api/param_description.html metodo=_dato parametro="OpenType<?> elementType" %}
* **boolean primitiveArray**,  {% include w3api/param_description.html metodo=_dato parametro="boolean primitiveArray" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [OpenDataException](/Java/OpenDataException/)

## Clase Padre
[ArrayType](/Java/ArrayType-javax-management-openmbean/)

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
