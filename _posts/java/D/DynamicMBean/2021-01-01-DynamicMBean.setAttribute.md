---
title: DynamicMBean.setAttribute()
permalink: Java/DynamicMBean/setAttribute
date: 2021-01-11
key: JavaJava.D.DynamicMBean
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DynamicMBean.metodos valor="setAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setAttribute(Attribute attribute) throws AttributeNotFoundException, InvalidAttributeValueException, MBeanException, ReflectionException
~~~

## Parámetros
* **Attribute attribute**,  {% include w3api/param_description.html metodo=_dato parametro="Attribute attribute" %}

## Excepciones
[ReflectionException](/Java/ReflectionException/), [MBeanException](/Java/MBeanException/), [InvalidAttributeValueException](/Java/InvalidAttributeValueException/), [AttributeNotFoundException](/Java/AttributeNotFoundException/)

## Clase Padre
[DynamicMBean](/Java/DynamicMBean/)

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
