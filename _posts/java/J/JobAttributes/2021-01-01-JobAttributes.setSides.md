---
title: JobAttributes.setSides()
permalink: /Java/JobAttributes/setSides/
date: 2021-01-11
key: Java.J.JobAttributes
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JobAttributes.metodos valor="setSides" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSides(JobAttributes.SidesType sides)
~~~

## Parámetros
* **JobAttributes.SidesType sides**,  {% include w3api/param_description.html metodo=_dato parametro="JobAttributes.SidesType sides" %}

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
