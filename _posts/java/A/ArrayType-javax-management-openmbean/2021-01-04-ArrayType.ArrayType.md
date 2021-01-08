---
title: ArrayType.ArrayType()
permalink: Java/ArrayType-javax-management-openmbean/ArrayType
date: 2021-01-04
key: JavaJava.A.ArrayType-javax-management-openmbean
category: java
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
* **SimpleType&lt;?&gt; elementType**,  {% include w3api/param_description.html metodo=_data parametro="SimpleType<?> elementType" %}
* **int dimension**,  {% include w3api/param_description.html metodo=_data parametro="int dimension" %}
* **boolean primitiveArray**,  {% include w3api/param_description.html metodo=_data parametro="boolean primitiveArray" %}
* **OpenType&lt;?&gt; elementType**,  {% include w3api/param_description.html metodo=_data parametro="OpenType<?> elementType" %}

## Excepciones
[OpenDataException](/Java/OpenDataException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ArrayType](/Java/ArrayType-javax-management-openmbean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ArrayType-javax-management-openmbean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
