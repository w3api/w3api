---
title: MBeanParameterInfo.MBeanParameterInfo()
permalink: Java/MBeanParameterInfo/MBeanParameterInfo
date: 2021-01-04
key: JavaJava.M.MBeanParameterInfo
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanParameterInfo.constructores valor="MBeanParameterInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanParameterInfo(String name, String type, String description)
public MBeanParameterInfo(String name, String type, String description, Descriptor descriptor)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}

## Clase Padre
[MBeanParameterInfo](/Java/MBeanParameterInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanParameterInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
