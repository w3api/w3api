---
title: JobAttributes.setDefaultSelection()
permalink: /Java/JobAttributes/setDefaultSelection/
date: 2021-01-11
key: Java.J.JobAttributes
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JobAttributes.metodos valor="setDefaultSelection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setDefaultSelection(JobAttributes.DefaultSelectionType defaultSelection)
~~~

## Parámetros
* **JobAttributes.DefaultSelectionType defaultSelection**,  {% include w3api/param_description.html metodo=_dato parametro="JobAttributes.DefaultSelectionType defaultSelection" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JobAttributes](/Java/JobAttributes/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
