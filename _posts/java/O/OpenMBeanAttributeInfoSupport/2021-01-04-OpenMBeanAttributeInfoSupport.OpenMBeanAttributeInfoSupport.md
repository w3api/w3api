---
title: OpenMBeanAttributeInfoSupport.OpenMBeanAttributeInfoSupport()
permalink: Java/OpenMBeanAttributeInfoSupport/OpenMBeanAttributeInfoSupport
date: 2021-01-04
key: JavaJava.O.OpenMBeanAttributeInfoSupport
category: java
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
* **Comparable&lt;T&gt; maxValue**,  {% include w3api/param_description.html metodo=_data parametro="Comparable<T> maxValue" %}
* **boolean isWritable**,  {% include w3api/param_description.html metodo=_data parametro="boolean isWritable" %}
* **boolean isReadable**,  {% include w3api/param_description.html metodo=_data parametro="boolean isReadable" %}
* **T defaultValue**,  {% include w3api/param_description.html metodo=_data parametro="T defaultValue" %}
* **Comparable&lt;T&gt; minValue**,  {% include w3api/param_description.html metodo=_data parametro="Comparable<T> minValue" %}
* **OpenType&lt;T&gt; openType**,  {% include w3api/param_description.html metodo=_data parametro="OpenType<T> openType" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}
* **boolean isIs**,  {% include w3api/param_description.html metodo=_data parametro="boolean isIs" %}
* **T[] legalValues**,  {% include w3api/param_description.html metodo=_data parametro="T[] legalValues" %}
* **OpenType&lt;?&gt; openType**,  {% include w3api/param_description.html metodo=_data parametro="OpenType<?> openType" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[OpenDataException](/Java/OpenDataException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[OpenMBeanAttributeInfoSupport](/Java/OpenMBeanAttributeInfoSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OpenMBeanAttributeInfoSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
