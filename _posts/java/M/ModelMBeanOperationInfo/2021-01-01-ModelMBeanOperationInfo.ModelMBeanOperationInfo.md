---
title: ModelMBeanOperationInfo.ModelMBeanOperationInfo()
permalink: /Java/ModelMBeanOperationInfo/ModelMBeanOperationInfo/
date: 2021-01-11
key: Java.M.ModelMBeanOperationInfo
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanOperationInfo.constructores valor="ModelMBeanOperationInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModelMBeanOperationInfo(String description, Method operationMethod)
public ModelMBeanOperationInfo(String description, Method operationMethod, Descriptor descriptor)
public ModelMBeanOperationInfo(String name, String description, MBeanParameterInfo[] signature, String type, int impact)
public ModelMBeanOperationInfo(String name, String description, MBeanParameterInfo[] signature, String type, int impact, Descriptor descriptor)
public ModelMBeanOperationInfo(ModelMBeanOperationInfo inInfo)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **int impact**,  {% include w3api/param_description.html metodo=_dato parametro="int impact" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor descriptor" %}
* **ModelMBeanOperationInfo inInfo**,  {% include w3api/param_description.html metodo=_dato parametro="ModelMBeanOperationInfo inInfo" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
* **Method operationMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Method operationMethod" %}
* **MBeanParameterInfo[] signature**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanParameterInfo[] signature" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ModelMBeanOperationInfo](/Java/ModelMBeanOperationInfo/)

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
