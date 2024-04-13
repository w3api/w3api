---
title: ImmutableDescriptor.ImmutableDescriptor()
permalink: /Java/ImmutableDescriptor/ImmutableDescriptor/
date: 2021-01-11
key: Java.I.ImmutableDescriptor
category: Java
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
* **String[] fieldNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] fieldNames" %}
* **Object[] fieldValues**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] fieldValues" %}
* **?&gt; fields**,  {% include w3api/param_description.html metodo=_dato parametro="?> fields" %}
* **String... fields**,  {% include w3api/param_description.html metodo=_dato parametro="String... fields" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
