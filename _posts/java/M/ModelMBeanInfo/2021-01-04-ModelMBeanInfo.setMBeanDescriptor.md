---
title: ModelMBeanInfo.setMBeanDescriptor()
permalink: Java/ModelMBeanInfo/setMBeanDescriptor
date: 2021-01-04
key: JavaJava.M.ModelMBeanInfo
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanInfo.metodos valor="setMBeanDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setMBeanDescriptor(Descriptor inDescriptor) throws MBeanException, RuntimeOperationsException
~~~

## Parámetros
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
