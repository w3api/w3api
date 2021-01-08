---
title: ModelMBeanAttributeInfo.ModelMBeanAttributeInfo()
permalink: Java/ModelMBeanAttributeInfo/ModelMBeanAttributeInfo
date: 2021-01-04
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
* **ModelMBeanAttributeInfo inInfo**,  {% include w3api/param_description.html metodo=_data parametro="ModelMBeanAttributeInfo inInfo" %}
* **boolean isReadable**,  {% include w3api/param_description.html metodo=_data parametro="boolean isReadable" %}
* **boolean isWritable**,  {% include w3api/param_description.html metodo=_data parametro="boolean isWritable" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **Method getter**,  {% include w3api/param_description.html metodo=_data parametro="Method getter" %}
* **Method setter**,  {% include w3api/param_description.html metodo=_data parametro="Method setter" %}
* **boolean isIs**,  {% include w3api/param_description.html metodo=_data parametro="boolean isIs" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[IntrospectionException](/Java/IntrospectionException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ModelMBeanAttributeInfo](/Java/ModelMBeanAttributeInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModelMBeanAttributeInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
