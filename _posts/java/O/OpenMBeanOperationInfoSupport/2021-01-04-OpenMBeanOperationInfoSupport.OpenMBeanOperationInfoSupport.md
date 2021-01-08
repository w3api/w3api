---
title: OpenMBeanOperationInfoSupport.OpenMBeanOperationInfoSupport()
permalink: Java/OpenMBeanOperationInfoSupport/OpenMBeanOperationInfoSupport
date: 2021-01-04
key: JavaJava.O.OpenMBeanOperationInfoSupport
category: java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OpenMBeanOperationInfoSupport.constructores valor="OpenMBeanOperationInfoSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OpenMBeanOperationInfoSupport(String name, String description, OpenMBeanParameterInfo[] signature, OpenType<?> returnOpenType, int impact)
public OpenMBeanOperationInfoSupport(String name, String description, OpenMBeanParameterInfo[] signature, OpenType<?> returnOpenType, int impact, Descriptor descriptor)
~~~

## Parámetros
* **OpenMBeanParameterInfo[] signature**,  {% include w3api/param_description.html metodo=_data parametro="OpenMBeanParameterInfo[] signature" %}
* **int impact**,  {% include w3api/param_description.html metodo=_data parametro="int impact" %}
* **String description**,  {% include w3api/param_description.html metodo=_data parametro="String description" %}
* **Descriptor descriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor descriptor" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **OpenType&lt;?&gt; returnOpenType**,  {% include w3api/param_description.html metodo=_data parametro="OpenType<?> returnOpenType" %}

## Excepciones
[ArrayStoreException](/Java/ArrayStoreException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[OpenMBeanOperationInfoSupport](/Java/OpenMBeanOperationInfoSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OpenMBeanOperationInfoSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
