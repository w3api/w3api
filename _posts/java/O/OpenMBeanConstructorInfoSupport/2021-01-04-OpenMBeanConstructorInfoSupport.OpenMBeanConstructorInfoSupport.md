---
title: OpenMBeanConstructorInfoSupport.OpenMBeanConstructorInfoSupport()
permalink: Java/OpenMBeanConstructorInfoSupport/OpenMBeanConstructorInfoSupport
date: 2021-01-04
key: JavaJava.O.OpenMBeanConstructorInfoSupport
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OpenMBeanConstructorInfoSupport.constructores valor="OpenMBeanConstructorInfoSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OpenMBeanConstructorInfoSupport(String name, String description, OpenMBeanParameterInfo[] signature)
public OpenMBeanConstructorInfoSupport(String name, String description, OpenMBeanParameterInfo[] signature, Descriptor descriptor)
~~~

## Parámetros
* **OpenMBeanParameterInfo[] signature**,  {% include w3api/param_description.html metodo=_data parametro="OpenMBeanParameterInfo[] signature" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}

## Excepciones
[ArrayStoreException](/Java/ArrayStoreException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[OpenMBeanConstructorInfoSupport](/Java/OpenMBeanConstructorInfoSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OpenMBeanConstructorInfoSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
