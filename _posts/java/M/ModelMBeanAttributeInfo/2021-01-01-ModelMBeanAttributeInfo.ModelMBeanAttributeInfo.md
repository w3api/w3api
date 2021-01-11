---
title: ModelMBeanAttributeInfo.ModelMBeanAttributeInfo()
permalink: Java/ModelMBeanAttributeInfo/ModelMBeanAttributeInfo
date: 2021-01-11
key: JavaJava.M.ModelMBeanAttributeInfo
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanAttributeInfo.constructores valor="ModelMBeanAttributeInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModelMBeanAttributeInfo(String name, String description, Method getter, Method setter) throws IntrospectionException
public ModelMBeanAttributeInfo(String name, String description, Method getter, Method setter, Descriptor descriptor) throws IntrospectionException
public ModelMBeanAttributeInfo(String name, String type, String description, boolean isReadable, boolean isWritable, boolean isIs)
public ModelMBeanAttributeInfo(String name, String type, String description, boolean isReadable, boolean isWritable, boolean isIs, Descriptor descriptor)
public ModelMBeanAttributeInfo(ModelMBeanAttributeInfo inInfo)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **boolean isReadable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isReadable" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor descriptor" %}
* **Method getter**,  {% include w3api/param_description.html metodo=_dato parametro="Method getter" %}
* **ModelMBeanAttributeInfo inInfo**,  {% include w3api/param_description.html metodo=_dato parametro="ModelMBeanAttributeInfo inInfo" %}
* **boolean isWritable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isWritable" %}
* **Method setter**,  {% include w3api/param_description.html metodo=_dato parametro="Method setter" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
* **boolean isIs**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isIs" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/), [IntrospectionException](/Java/IntrospectionException/)

## Clase Padre
[ModelMBeanAttributeInfo](/Java/ModelMBeanAttributeInfo/)

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
