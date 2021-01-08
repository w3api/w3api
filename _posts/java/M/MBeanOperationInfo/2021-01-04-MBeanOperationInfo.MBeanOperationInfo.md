---
title: MBeanOperationInfo.MBeanOperationInfo()
permalink: Java/MBeanOperationInfo/MBeanOperationInfo
date: 2021-01-04
key: JavaJava.M.MBeanOperationInfo
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanOperationInfo.constructores valor="MBeanOperationInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanOperationInfo(String description, Method method)
public MBeanOperationInfo(String name, String description, MBeanParameterInfo[] signature, String type, int impact)
public MBeanOperationInfo(String name, String description, MBeanParameterInfo[] signature, String type, int impact, Descriptor descriptor)
~~~

## Parámetros
* **Method method**,  {% include w3api/param_description.html metodo=_data parametro="Method method" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}
* **int impact**,  {% include w3api/param_description.html metodo=_data parametro="int impact" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}
* **MBeanParameterInfo[] signature**,  {% include w3api/param_description.html metodo=_data parametro="MBeanParameterInfo[] signature" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MBeanOperationInfo](/Java/MBeanOperationInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanOperationInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
