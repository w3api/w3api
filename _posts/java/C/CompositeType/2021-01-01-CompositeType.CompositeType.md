---
title: CompositeType.CompositeType()
permalink: /Java/CompositeType/CompositeType/
date: 2021-01-11
key: Java.C.CompositeType
category: Java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeType.constructores valor="CompositeType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CompositeType(String typeName, String description, String[] itemNames, String[] itemDescriptions, OpenType<?>[] itemTypes) throws OpenDataException
~~~

## Parámetros
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **OpenType&lt;?&gt;[] itemTypes**,  {% include w3api/param_description.html metodo=_dato parametro="OpenType<?>[] itemTypes" %}
* **String[] itemNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] itemNames" %}
* **String[] itemDescriptions**,  {% include w3api/param_description.html metodo=_dato parametro="String[] itemDescriptions" %}
* **String typeName**,  {% include w3api/param_description.html metodo=_dato parametro="String typeName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [OpenDataException](/Java/OpenDataException/)

## Clase Padre
[CompositeType](/Java/CompositeType/)

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
