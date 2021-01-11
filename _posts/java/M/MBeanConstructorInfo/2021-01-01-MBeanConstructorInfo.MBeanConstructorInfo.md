---
title: MBeanConstructorInfo.MBeanConstructorInfo()
permalink: Java/MBeanConstructorInfo/MBeanConstructorInfo
date: 2021-01-11
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
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Constructor&lt;?&gt; constructor**,  {% include w3api/param_description.html metodo=_dato parametro="Constructor<?> constructor" %}
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor descriptor" %}
* **MBeanParameterInfo[] signature**,  {% include w3api/param_description.html metodo=_dato parametro="MBeanParameterInfo[] signature" %}

## Clase Padre
[MBeanConstructorInfo](/Java/MBeanConstructorInfo/)

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
