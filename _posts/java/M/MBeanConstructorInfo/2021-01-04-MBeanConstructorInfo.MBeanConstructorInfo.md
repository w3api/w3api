---
title: MBeanConstructorInfo.MBeanConstructorInfo()
permalink: Java/MBeanConstructorInfo/MBeanConstructorInfo
date: 2021-01-04
key: JavaJava.M.MBeanConstructorInfo
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MBeanConstructorInfo.constructores valor="MBeanConstructorInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MBeanConstructorInfo(String description, Constructor<?> constructor)
public MBeanConstructorInfo(String name, String description, MBeanParameterInfo[] signature)
public MBeanConstructorInfo(String name, String description, MBeanParameterInfo[] signature, Descriptor descriptor)
~~~

## Parámetros
* **Constructor&lt;?&gt; constructor**,  {% include w3api/param_description.html metodo=_data parametro="Constructor<?> constructor" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}
* **MBeanParameterInfo[] signature**,  {% include w3api/param_description.html metodo=_data parametro="MBeanParameterInfo[] signature" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Clase Padre
[MBeanConstructorInfo](/Java/MBeanConstructorInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MBeanConstructorInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
