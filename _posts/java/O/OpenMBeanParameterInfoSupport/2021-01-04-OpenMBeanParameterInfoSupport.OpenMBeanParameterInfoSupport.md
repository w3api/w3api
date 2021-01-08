---
title: OpenMBeanParameterInfoSupport.OpenMBeanParameterInfoSupport()
permalink: Java/OpenMBeanParameterInfoSupport/OpenMBeanParameterInfoSupport
date: 2021-01-04
key: JavaJava.O.OpenMBeanParameterInfoSupport
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OpenMBeanParameterInfoSupport.constructores valor="OpenMBeanParameterInfoSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OpenMBeanParameterInfoSupport(String name, String description, OpenType<?> openType)
public OpenMBeanParameterInfoSupport(String name, String description, OpenType<?> openType, Descriptor descriptor)
public OpenMBeanParameterInfoSupport(String name, String description, OpenType<T> openType, T defaultValue) throws OpenDataException
public OpenMBeanParameterInfoSupport(String name, String description, OpenType<T> openType, T defaultValue, Comparable<T> minValue, Comparable<T> maxValue) throws OpenDataException
public OpenMBeanParameterInfoSupport(String name, String description, OpenType<T> openType, T defaultValue, T[] legalValues) throws OpenDataException
~~~

## Parámetros
* **Comparable&lt;T&gt; maxValue**,  {% include w3api/param_description.html metodo=_data parametro="Comparable<T> maxValue" %}
* **Comparable&lt;T&gt; minValue**,  {% include w3api/param_description.html metodo=_data parametro="Comparable<T> minValue" %}
* **T defaultValue**,  {% include w3api/param_description.html metodo=_data parametro="T defaultValue" %}
* **OpenType&lt;T&gt; openType**,  {% include w3api/param_description.html metodo=_data parametro="OpenType<T> openType" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **T[] legalValues**,  {% include w3api/param_description.html metodo=_data parametro="T[] legalValues" %}
* **OpenType&lt;?&gt; openType**,  {% include w3api/param_description.html metodo=_data parametro="OpenType<?> openType" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[OpenDataException](/Java/OpenDataException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[OpenMBeanParameterInfoSupport](/Java/OpenMBeanParameterInfoSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OpenMBeanParameterInfoSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
