---
title: ModelMBeanOperationInfo.ModelMBeanOperationInfo()
permalink: Java/ModelMBeanOperationInfo/ModelMBeanOperationInfo
date: 2021-01-04
key: JavaJava.M.ModelMBeanOperationInfo
category: java
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
* **Method operationMethod**,  {% include w3api/param_description.html metodo=_data parametro="Method operationMethod" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}
* **ModelMBeanOperationInfo inInfo**,  {% include w3api/param_description.html metodo=_data parametro="ModelMBeanOperationInfo inInfo" %}
* **int impact**,  {% include w3api/param_description.html metodo=_data parametro="int impact" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}
* **MBeanParameterInfo[] signature**,  {% include w3api/param_description.html metodo=_data parametro="MBeanParameterInfo[] signature" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

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
{%- for _ldc in site.data.Java.M.ModelMBeanOperationInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
