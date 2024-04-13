---
title: OpenMBeanParameterInfoSupport.OpenMBeanParameterInfoSupport()
permalink: /Java/OpenMBeanParameterInfoSupport/OpenMBeanParameterInfoSupport/
date: 2021-01-11
key: Java.O.OpenMBeanParameterInfoSupport
category: Java
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
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **OpenType&lt;?&gt; openType**,  {% include w3api/param_description.html metodo=_dato parametro="OpenType<?> openType" %}
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **T defaultValue**,  {% include w3api/param_description.html metodo=_dato parametro="T defaultValue" %}
* **Comparable&lt;T&gt; minValue**,  {% include w3api/param_description.html metodo=_dato parametro="Comparable<T> minValue" %}
* **T[] legalValues**,  {% include w3api/param_description.html metodo=_dato parametro="T[] legalValues" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor descriptor" %}
* **Comparable&lt;T&gt; maxValue**,  {% include w3api/param_description.html metodo=_dato parametro="Comparable<T> maxValue" %}
* **OpenType&lt;T&gt; openType**,  {% include w3api/param_description.html metodo=_dato parametro="OpenType<T> openType" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [OpenDataException](/Java/OpenDataException/)

## Clase Padre
[OpenMBeanParameterInfoSupport](/Java/OpenMBeanParameterInfoSupport/)

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
