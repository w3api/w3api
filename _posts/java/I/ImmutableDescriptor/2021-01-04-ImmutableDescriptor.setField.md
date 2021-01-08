---
title: ImmutableDescriptor.setField()
permalink: Java/ImmutableDescriptor/setField
date: 2021-01-04
key: JavaJava.I.ImmutableDescriptor
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImmutableDescriptor.metodos valor="setField" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setField(String fieldName, Object fieldValue) throws RuntimeOperationsException
~~~

## Parámetros
* **Object fieldValue**,  {% include w3api/param_description.html metodo=_data parametro="Object fieldValue" %}
* **String fieldName**,  {% include w3api/param_description.html metodo=_data parametro="String fieldName" %}

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
{%- for _ldc in site.data.Java.I.ImmutableDescriptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
