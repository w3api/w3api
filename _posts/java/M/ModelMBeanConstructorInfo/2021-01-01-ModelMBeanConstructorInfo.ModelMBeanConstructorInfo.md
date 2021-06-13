---
title: ModelMBeanConstructorInfo.ModelMBeanConstructorInfo()
permalink: /Java/ModelMBeanConstructorInfo/ModelMBeanConstructorInfo/
date: 2021-01-11
key: Java.M.ModelMBeanConstructorInfo
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanConstructorInfo.constructores valor="ModelMBeanConstructorInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModelMBeanConstructorInfo(String description, Constructor<?> constructorMethod)
public ModelMBeanConstructorInfo(String description, Constructor<?> constructorMethod, Descriptor descriptor)
public ModelMBeanConstructorInfo(String name, String description, MBeanParameterInfo[] signature)
public ModelMBeanConstructorInfo(String name, String description, MBeanParameterInfo[] signature, Descriptor descriptor)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor descriptor" %}
* **Constructor&lt;?&gt; constructorMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Constructor<?> constructorMethod" %}
* **MBeanParameterInfo[] signature**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanParameterInfo[] signature" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ModelMBeanConstructorInfo](/Java/ModelMBeanConstructorInfo/)

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
