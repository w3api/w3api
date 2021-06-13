---
title: MBeanAttributeInfo.MBeanAttributeInfo()
permalink: Java/MBeanAttributeInfo/MBeanAttributeInfo
date: 2021-01-11
key: JavaJava.M.MBeanAttributeInfo
category: Java
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
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **boolean isReadable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isReadable" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor descriptor" %}
* **Method getter**,  {% include w3api/param_description.html metodo=_dato parametro="Method getter" %}
* **boolean isWritable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isWritable" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
* **Method setter**,  {% include w3api/param_description.html metodo=_dato parametro="Method setter" %}
* **boolean isIs**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isIs" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IntrospectionException](/Java/IntrospectionException/)

## Clase Padre
[MBeanAttributeInfo](/Java/MBeanAttributeInfo/)

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
