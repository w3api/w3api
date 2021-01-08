---
title: ModelMBeanInfo.setDescriptor()
permalink: Java/ModelMBeanInfo/setDescriptor
date: 2021-01-04
key: JavaJava.M.ModelMBeanInfo
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanInfo.metodos valor="setDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setDescriptor(Descriptor inDescriptor, String inDescriptorType) throws MBeanException, RuntimeOperationsException
~~~

## Parámetros
* **String inDescriptorType**,  {% include w3api/param_description.html metodo=_data parametro="String inDescriptorType" %}
* **Descriptor inDescriptor**,  {% include w3api/param_description.html metodo=_data parametro="Descriptor inDescriptor" %}

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
{%- for _ldc in site.data.Java.M.ModelMBeanInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
