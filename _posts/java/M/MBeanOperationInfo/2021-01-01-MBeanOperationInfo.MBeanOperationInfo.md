---
title: MBeanOperationInfo.MBeanOperationInfo()
permalink: Java/MBeanOperationInfo/MBeanOperationInfo
date: 2021-01-11
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
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **int impact**,  {% include w3api/param_description.html metodo=_dato parametro="int impact" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor descriptor" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
* **Method method**,  {% include w3api/param_description.html metodo=_dato parametro="Method method" %}
* **MBeanParameterInfo[] signature**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanParameterInfo[] signature" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
