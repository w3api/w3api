---
title: ImmutableDescriptor.setFields()
permalink: Java/ImmutableDescriptor/setFields
date: 2021-01-11
key: JavaJava.I.ImmutableDescriptor
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImmutableDescriptor.metodos valor="setFields" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setFields(String[] fieldNames, Object[] fieldValues) throws RuntimeOperationsException
~~~

## Parámetros
* **String[] fieldNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] fieldNames" %}
* **Object[] fieldValues**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] fieldValues" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ImmutableDescriptor](/Java/ImmutableDescriptor/)

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
