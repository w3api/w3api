---
title: CompositeType.CompositeType()
permalink: Java/CompositeType/CompositeType
date: 2021-01-04
key: JavaJava.C.CompositeType
category: java
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
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **String typeName**,  {% include w3api/param_description.html metodo=_data parametro="String typeName" %}
* **String[] itemNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] itemNames" %}
* **String[] itemDescriptions**,  {% include w3api/param_description.html metodo=_data parametro="String[] itemDescriptions" %}
* **OpenType&lt;?&gt;[] itemTypes**,  {% include w3api/param_description.html metodo=_data parametro="OpenType<?>[] itemTypes" %}

## Excepciones
[OpenDataException](/Java/OpenDataException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CompositeType](/Java/CompositeType/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompositeType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
