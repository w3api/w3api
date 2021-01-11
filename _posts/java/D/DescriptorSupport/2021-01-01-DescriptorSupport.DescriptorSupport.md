---
title: DescriptorSupport.DescriptorSupport()
permalink: Java/DescriptorSupport/DescriptorSupport
date: 2021-01-11
key: JavaJava.D.DescriptorSupport
category: java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DescriptorSupport.constructores valor="DescriptorSupport" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DescriptorSupport()
public DescriptorSupport(int initNumFields) throws MBeanException, RuntimeOperationsException
public DescriptorSupport(String inStr) throws MBeanException, RuntimeOperationsException, XMLParseException
public DescriptorSupport(String... fields)
public DescriptorSupport(String[] fieldNames, Object[] fieldValues) throws RuntimeOperationsException
public DescriptorSupport(DescriptorSupport inDescr)
~~~

## Parámetros
* **String[] fieldNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] fieldNames" %}
* **Object[] fieldValues**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] fieldValues" %}
* **int initNumFields**,  {% include w3api/param_description.html metodo=_dato parametro="int initNumFields" %}
* **DescriptorSupport inDescr**,  {% include w3api/param_description.html metodo=_dato parametro="DescriptorSupport inDescr" %}
* **String... fields**,  {% include w3api/param_description.html metodo=_dato parametro="String... fields" %}
* **String inStr**,  {% include w3api/param_description.html metodo=_dato parametro="String inStr" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [XMLParseException](/Java/XMLParseException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[DescriptorSupport](/Java/DescriptorSupport/)

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
