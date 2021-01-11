---
title: AttributeList.set()
permalink: Java/AttributeList-javax-management/set
date: 2021-01-11
key: JavaJava.A.AttributeList-javax-management
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributeList-javax-management.metodos valor="set" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object set(int index, Object element)
public void set(int index, Attribute object)
~~~

## Parámetros
* **Object element**,  {% include w3api/param_description.html metodo=_dato parametro="Object element" %}
* **Attribute object**,  {% include w3api/param_description.html metodo=_dato parametro="Attribute object" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

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
