---
title: ModelMBeanInfo.getDescriptor()
permalink: Java/ModelMBeanInfo/getDescriptor
date: 2021-01-11
key: JavaJava.M.ModelMBeanInfo
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanInfo.metodos valor="getDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Descriptor getDescriptor(String inDescriptorName, String inDescriptorType) throws MBeanException, RuntimeOperationsException
~~~

## Parámetros
* **String inDescriptorName**,  {% include w3api/param_description.html metodo=_dato parametro="String inDescriptorName" %}
* **String inDescriptorType**,  {% include w3api/param_description.html metodo=_dato parametro="String inDescriptorType" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ModelMBeanInfo](/Java/ModelMBeanInfo/)

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