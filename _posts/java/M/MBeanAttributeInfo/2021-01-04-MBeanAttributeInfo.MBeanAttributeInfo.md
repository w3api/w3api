---
title: MBeanAttributeInfo.MBeanAttributeInfo()
permalink: Java/MBeanAttributeInfo/MBeanAttributeInfo
date: 2021-01-04
key: JavaJava.M.MBeanAttributeInfo
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanAttributeInfo.constructores valor="MBeanAttributeInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanAttributeInfo(String name, String description, Method getter, Method setter) throws IntrospectionException
public MBeanAttributeInfo(String name, String type, String description, boolean isReadable, boolean isWritable, boolean isIs)
public MBeanAttributeInfo(String name, String type, String description, boolean isReadable, boolean isWritable, boolean isIs, Descriptor descriptor)
~~~

## Parámetros
* **boolean isReadable**,  {% include w3api/param_description.html metodo=_data parametro="boolean isReadable" %}
* **boolean isWritable**,  {% include w3api/param_description.html metodo=_data parametro="boolean isWritable" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **Method getter**,  {% include w3api/param_description.html metodo=_data parametro="Method getter" %}
* **boolean isIs**,  {% include w3api/param_description.html metodo=_data parametro="boolean isIs" %}
* **Method setter**,  {% include w3api/param_description.html metodo=_data parametro="Method setter" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[IntrospectionException](/Java/IntrospectionException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MBeanAttributeInfo](/Java/MBeanAttributeInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanAttributeInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
