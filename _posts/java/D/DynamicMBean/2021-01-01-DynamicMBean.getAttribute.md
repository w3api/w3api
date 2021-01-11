---
title: DynamicMBean.getAttribute()
permalink: Java/DynamicMBean/getAttribute
date: 2021-01-11
key: JavaJava.D.DynamicMBean
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DynamicMBean.metodos valor="getAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getAttribute(String attribute) throws AttributeNotFoundException, MBeanException, ReflectionException
~~~

## Parámetros
* **String attribute**,  {% include w3api/param_description.html metodo=_dato parametro="String attribute" %}

## Excepciones
[ReflectionException](/Java/ReflectionException/), [MBeanException](/Java/MBeanException/), [AttributeNotFoundException](/Java/AttributeNotFoundException/)

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
