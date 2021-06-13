---
title: OpenMBeanAttributeInfoSupport.OpenMBeanAttributeInfoSupport()
permalink: /Java/OpenMBeanAttributeInfoSupport/OpenMBeanAttributeInfoSupport/
date: 2021-01-11
key: Java.O.OpenMBeanAttributeInfoSupport
category: Java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OpenMBeanAttributeInfoSupport.constructores valor="OpenMBeanAttributeInfoSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OpenMBeanAttributeInfoSupport(String name, String description, OpenType<?> openType, boolean isReadable, boolean isWritable, boolean isIs)
public OpenMBeanAttributeInfoSupport(String name, String description, OpenType<?> openType, boolean isReadable, boolean isWritable, boolean isIs, Descriptor descriptor)
public OpenMBeanAttributeInfoSupport(String name, String description, OpenType<T> openType, boolean isReadable, boolean isWritable, boolean isIs, T defaultValue) throws OpenDataException
public OpenMBeanAttributeInfoSupport(String name, String description, OpenType<T> openType, boolean isReadable, boolean isWritable, boolean isIs, T defaultValue, Comparable<T> minValue, Comparable<T> maxValue) throws OpenDataException
public OpenMBeanAttributeInfoSupport(String name, String description, OpenType<T> openType, boolean isReadable, boolean isWritable, boolean isIs, T defaultValue, T[] legalValues) throws OpenDataException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **OpenType&lt;?&gt; openType**,  {% include w3api/param_description.html metodo=_dato parametro="OpenType<?> openType" %}
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **boolean isReadable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isReadable" %}
* **T defaultValue**,  {% include w3api/param_description.html metodo=_dato parametro="T defaultValue" %}
* **Comparable&lt;T&gt; minValue**,  {% include w3api/param_description.html metodo=_dato parametro="Comparable<T> minValue" %}
* **T[] legalValues**,  {% include w3api/param_description.html metodo=_dato parametro="T[] legalValues" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor descriptor" %}
* **boolean isWritable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isWritable" %}
* **Comparable&lt;T&gt; maxValue**,  {% include w3api/param_description.html metodo=_dato parametro="Comparable<T> maxValue" %}
* **boolean isIs**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isIs" %}
* **OpenType&lt;T&gt; openType**,  {% include w3api/param_description.html metodo=_dato parametro="OpenType<T> openType" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [OpenDataException](/Java/OpenDataException/)

## Clase Padre
[OpenMBeanAttributeInfoSupport](/Java/OpenMBeanAttributeInfoSupport/)

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
