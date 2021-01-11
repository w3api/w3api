---
title: AttributeList.addAll()
permalink: Java/AttributeList-javax-management/addAll
date: 2021-01-11
key: JavaJava.A.AttributeList-javax-management
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributeList-javax-management.metodos valor="addAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean addAll(int index, Collection<?> c)
public boolean addAll(int index, AttributeList list)
public boolean addAll(Collection<?> c)
public boolean addAll(AttributeList list)
~~~

## Parámetros
* **Collection&lt;?&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<?> c" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **AttributeList list**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeList list" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
