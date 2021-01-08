---
title: AttributeList.AttributeList()
permalink: Java/AttributeList-javax-management/AttributeList
date: 2021-01-04
key: JavaJava.A.AttributeList-javax-management
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributeList-javax-management.constructores valor="AttributeList" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AttributeList()
public AttributeList(int initialCapacity)
public AttributeList(List<Attribute> list)
public AttributeList(AttributeList list)
~~~

## Parámetros
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_data parametro="int initialCapacity" %}
* **AttributeList list**,  {% include w3api/param_description.html metodo=_data parametro="AttributeList list" %}
* **List&lt;Attribute&gt; list**,  {% include w3api/param_description.html metodo=_data parametro="List<Attribute> list" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AttributeList](/Java/AttributeList-javax-management/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AttributeList-javax-management.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
