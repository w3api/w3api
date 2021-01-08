---
title: ImmutableDescriptor.ImmutableDescriptor()
permalink: Java/ImmutableDescriptor/ImmutableDescriptor
date: 2021-01-04
key: JavaJava.I.ImmutableDescriptor
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImmutableDescriptor.constructores valor="ImmutableDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ImmutableDescriptor(String... fields)
public ImmutableDescriptor(String[] fieldNames, Object[] fieldValues)
public ImmutableDescriptor(Map<String,?> fields)
~~~

## Parámetros
* **String[] fieldNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] fieldNames" %}
* **?&gt; fields**,  {% include w3api/param_description.html metodo=_data parametro="?> fields" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **Object[] fieldValues**,  {% include w3api/param_description.html metodo=_data parametro="Object[] fieldValues" %}
* **String... fields**,  {% include w3api/param_description.html metodo=_data parametro="String... fields" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
