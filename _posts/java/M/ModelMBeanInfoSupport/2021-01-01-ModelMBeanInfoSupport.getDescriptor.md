---
title: ModelMBeanInfoSupport.getDescriptor()
permalink: Java/ModelMBeanInfoSupport/getDescriptor
date: 2021-01-11
key: JavaJava.M.ModelMBeanInfoSupport
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanInfoSupport.metodos valor="getDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Descriptor getDescriptor()
public Descriptor getDescriptor(String inDescriptorName) throws MBeanException, RuntimeOperationsException
~~~

## Parámetros
* **String inDescriptorName**,  {% include w3api/param_description.html metodo=_dato parametro="String inDescriptorName" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ModelMBeanInfoSupport](/Java/ModelMBeanInfoSupport/)

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
