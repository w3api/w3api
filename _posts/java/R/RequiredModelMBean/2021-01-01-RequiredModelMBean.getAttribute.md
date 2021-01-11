---
title: RequiredModelMBean.getAttribute()
permalink: Java/RequiredModelMBean/getAttribute
date: 2021-01-11
key: JavaJava.R.RequiredModelMBean
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RequiredModelMBean.metodos valor="getAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getAttribute(String attrName) throws AttributeNotFoundException, MBeanException, ReflectionException
~~~

## Parámetros
* **String attrName**,  {% include w3api/param_description.html metodo=_dato parametro="String attrName" %}

## Excepciones
[ReflectionException](/Java/ReflectionException/), [MBeanException](/Java/MBeanException/), [AttributeNotFoundException](/Java/AttributeNotFoundException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[RequiredModelMBean](/Java/RequiredModelMBean/)

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
