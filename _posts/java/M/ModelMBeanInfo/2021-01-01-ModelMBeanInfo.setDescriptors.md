---
title: ModelMBeanInfo.setDescriptors()
permalink: Java/ModelMBeanInfo/setDescriptors
date: 2021-01-11
key: JavaJava.M.ModelMBeanInfo
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanInfo.metodos valor="setDescriptors" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setDescriptors(Descriptor[] inDescriptors) throws MBeanException, RuntimeOperationsException
~~~

## Parámetros
* **Descriptor[] inDescriptors**,  {% include w3api/param_description.html metodo=_dato parametro="Descriptor[] inDescriptors" %}

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
